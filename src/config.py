"""Configuração central do projeto lol-worlds-predictor."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Onde ficam os CSVs anuais baixados manualmente do Oracle's Elixir
# (https://oracleselixir.com/tools/downloads)
OE_RAW_DIR = BASE_DIR / "data" / "raw" / "oracles_elixir"

# Banco SQLite consolidado (times, partidas, jogadores)
SQLITE_PATH = BASE_DIR / "data" / "processed" / "lol_esports.db"

# Ligas consideradas "principais" (mandam representantes ao Worlds).
# Os nomes seguem exatamente a coluna `league` do Oracle's Elixir.
MAJOR_LEAGUES = [
    "LCK",   # Coreia
    "LPL",   # China
    "LEC",   # Europa
    "LTA N", # Américas - Norte (ex-LCS), nome mudou ao longo dos anos
    "LTA S", # Américas - Sul (ex-CBLOL/LLA)
    "LCS",   # nome usado em anos anteriores à unificação LTA
    "PCS",   # Ásia-Pacífico
    "VCS",   # Vietnã
]

# Nome dos torneios de Worlds no dataset (coluna `league`/`event` varia por ano)
WORLDS_EVENT_NAMES = ["WLDs", "WCS", "World Championship"]
