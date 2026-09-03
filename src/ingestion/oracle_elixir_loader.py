"""
Carrega os CSVs anuais do Oracle's Elixir para o banco SQLite normalizado.

Como obter os arquivos (não há endpoint de download programático estável):
    1. Acesse https://oracleselixir.com/tools/downloads
    2. Baixe o CSV do(s) ano(s) desejado(s) (ex: 2023.csv, 2024.csv, 2025.csv, 2026.csv)
    3. Coloque os arquivos em data/raw/oracles_elixir/

Cada jogo no CSV original vem em 12 linhas: 10 de jogador (position = top/jng/mid/bot/sup)
e 2 de time (position = 'team'). Este loader separa isso em três tabelas normalizadas
(games, team_game_stats, player_game_stats) — ver src/db/schema.sql.

Uso:
    python -m src.ingestion.oracle_elixir_loader
"""

import pandas as pd

from src.config import OE_RAW_DIR
from src.db.database import get_connection, init_db
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Colunas do CSV do Oracle's Elixir usadas neste projeto.
# O arquivo real tem 100+ colunas; aqui pegamos só o essencial para
# a Fase 1 (rating de força de time). Outras colunas (objetivos, gold
# por minuto, diffs em 10/15/20min etc.) podem ser incorporadas depois
# conforme a leitura teórica indicar quais features valem a pena.
TEAM_COLUMNS = [
    "gameid", "league", "year", "split", "playoffs", "date", "patch",
    "game", "gamelength", "side", "teamname", "result",
    "kills", "deaths", "assists", "dragons", "barons", "towers",
    "firstblood", "firstdragon", "firstbaron", "totalgold",
]

PLAYER_COLUMNS = [
    "gameid", "teamname", "playername", "position", "champion",
    "kills", "deaths", "assists", "totalgold", "total cs",
    "damagetochampions", "visionscore",
]

INSERT_GAME_SQL = """
INSERT OR IGNORE INTO games
    (game_id, league, year, split, playoffs, date, patch, game_number,
     game_length_s, blue_team, red_team, winner)
VALUES (:game_id, :league, :year, :split, :playoffs, :date, :patch, :game_number,
        :game_length_s, :blue_team, :red_team, :winner)
"""

INSERT_TEAM_STATS_SQL = """
INSERT OR IGNORE INTO team_game_stats
    (game_id, team_name, side, result, kills, deaths, assists,
     dragons, barons, towers, first_blood, first_dragon, first_baron, total_gold)
VALUES (:game_id, :team_name, :side, :result, :kills, :deaths, :assists,
        :dragons, :barons, :towers, :first_blood, :first_dragon, :first_baron, :total_gold)
"""

INSERT_PLAYER_STATS_SQL = """
INSERT OR IGNORE INTO player_game_stats
    (game_id, team_name, player_name, position, champion, kills, deaths,
     assists, total_gold, cs, damage_to_champions, vision_score)
VALUES (:game_id, :team_name, :player_name, :position, :champion, :kills, :deaths,
        :assists, :total_gold, :cs, :damage_to_champions, :vision_score)
"""


def _load_year_csv(path) -> pd.DataFrame:
    logger.info("Lendo %s...", path.name)
    return pd.read_csv(path, low_memory=False)


def _split_team_and_player_rows(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    team_rows = df[df["position"].str.lower() == "team"].copy()
    player_rows = df[df["position"].str.lower() != "team"].copy()
    return team_rows, player_rows


def _build_games_rows(team_rows: pd.DataFrame) -> list[dict]:
    rows = []
    for game_id, group in team_rows.groupby("gameid"):
        if len(group) != 2:
            # jogo incompleto no dataset (ex: dado parcial) — pula
            continue

        blue = group[group["side"].str.lower() == "blue"].iloc[0]
        red = group[group["side"].str.lower() == "red"].iloc[0]
        winning_teams = group[group["result"] == 1]
        if winning_teams.empty:
            continue
        winner_row = winning_teams.iloc[0]

        rows.append(
            {
                "game_id": game_id,
                "league": blue["league"],
                "year": int(blue["year"]),
                "split": blue.get("split"),
                "playoffs": int(blue.get("playoffs", 0) or 0),
                "date": blue.get("date"),
                "patch": blue.get("patch"),
                "game_number": 1 if pd.isna(blue.get("game")) else int(blue.get("game")),
                "game_length_s": int(blue.get("gamelength", 0) or 0),
                "blue_team": blue["teamname"],
                "red_team": red["teamname"],
                "winner": winner_row["teamname"],
            }
        )
    return rows


def _build_team_stats_rows(team_rows: pd.DataFrame) -> list[dict]:
    rows = []
    for _, r in team_rows.iterrows():
        rows.append(
            {
                "game_id": r["gameid"],
                "team_name": r["teamname"],
                "side": r["side"],
                "result": int(r.get("result", 0) or 0),
                "kills": r.get("kills"),
                "deaths": r.get("deaths"),
                "assists": r.get("assists"),
                "dragons": r.get("dragons"),
                "barons": r.get("barons"),
                "towers": r.get("towers"),
                "first_blood": r.get("firstblood"),
                "first_dragon": r.get("firstdragon"),
                "first_baron": r.get("firstbaron"),
                "total_gold": r.get("totalgold"),
            }
        )
    return rows


def _build_player_stats_rows(player_rows: pd.DataFrame) -> list[dict]:
    rows = []
    for _, r in player_rows.iterrows():
        rows.append(
            {
                "game_id": r["gameid"],
                "team_name": r["teamname"],
                "player_name": r["playername"],
                "position": r["position"],
                "champion": r.get("champion"),
                "kills": r.get("kills"),
                "deaths": r.get("deaths"),
                "assists": r.get("assists"),
                "total_gold": r.get("totalgold"),
                "cs": r.get("total cs"),
                "damage_to_champions": r.get("damagetochampions"),
                "vision_score": r.get("visionscore"),
            }
        )
    return rows


def load_file(path) -> None:
    df = _load_year_csv(path)
    df.columns = [c.strip() for c in df.columns]

    team_rows, player_rows = _split_team_and_player_rows(df)

    games = _build_games_rows(team_rows)
    team_stats = _build_team_stats_rows(team_rows)
    player_stats = _build_player_stats_rows(player_rows)

    with get_connection() as conn:
        conn.executemany(INSERT_GAME_SQL, games)
        conn.executemany(INSERT_TEAM_STATS_SQL, team_stats)
        conn.executemany(INSERT_PLAYER_STATS_SQL, player_stats)

    logger.info(
        "%s: %s jogos, %s linhas de time, %s linhas de jogador carregados.",
        path.name, len(games), len(team_stats), len(player_stats),
    )


def run() -> None:
    init_db()
    csv_files = sorted(OE_RAW_DIR.glob("*.csv"))

    if not csv_files:
        logger.warning(
            "Nenhum CSV encontrado em %s. Baixe os arquivos em "
            "https://oracleselixir.com/tools/downloads e coloque-os nessa pasta.",
            OE_RAW_DIR,
        )
        return

    for path in csv_files:
        load_file(path)


if __name__ == "__main__":
    run()
