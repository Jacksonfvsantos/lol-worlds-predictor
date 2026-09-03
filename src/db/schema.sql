-- Schema do projeto lol-worlds-predictor.
-- Normaliza o formato do Oracle's Elixir (12 linhas por jogo: 2 de time + 10 de jogador)
-- em três tabelas: games (1 por jogo), team_game_stats (2 por jogo) e player_game_stats (10 por jogo).

CREATE TABLE IF NOT EXISTS games (
    game_id         TEXT PRIMARY KEY,
    league          TEXT NOT NULL,
    year            INTEGER NOT NULL,
    split           TEXT,
    playoffs        INTEGER DEFAULT 0,
    date            TEXT,
    patch           TEXT,
    game_number     INTEGER,          -- número do game dentro do Bo (1, 2, 3...)
    game_length_s   INTEGER,
    blue_team       TEXT,
    red_team        TEXT,
    winner          TEXT              -- nome do time vencedor
);

CREATE TABLE IF NOT EXISTS team_game_stats (
    game_id         TEXT NOT NULL,
    team_name       TEXT NOT NULL,
    side            TEXT,             -- Blue / Red
    result          INTEGER,          -- 1 = vitória, 0 = derrota
    kills           INTEGER,
    deaths          INTEGER,
    assists         INTEGER,
    dragons         INTEGER,
    barons          INTEGER,
    towers          INTEGER,
    first_blood     INTEGER,
    first_dragon    INTEGER,
    first_baron     INTEGER,
    total_gold      INTEGER,
    PRIMARY KEY (game_id, team_name),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);

CREATE TABLE IF NOT EXISTS player_game_stats (
    game_id             TEXT NOT NULL,
    team_name           TEXT NOT NULL,
    player_name         TEXT NOT NULL,
    position            TEXT,          -- top, jng, mid, bot, sup
    champion            TEXT,
    kills               INTEGER,
    deaths              INTEGER,
    assists             INTEGER,
    total_gold          INTEGER,
    cs                  INTEGER,
    damage_to_champions INTEGER,
    vision_score        INTEGER,
    PRIMARY KEY (game_id, player_name),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- Tabela de saída do módulo de rating (Fase de modelagem).
-- Guarda o rating de cada time ao longo do tempo, um snapshot por jogo processado.
CREATE TABLE IF NOT EXISTS team_ratings (
    team_name       TEXT NOT NULL,
    as_of_game_id   TEXT NOT NULL,
    as_of_date      TEXT,
    rating          REAL NOT NULL,
    method          TEXT NOT NULL,     -- 'elo', 'bradley_terry', etc.
    PRIMARY KEY (team_name, as_of_game_id, method)
);

CREATE INDEX IF NOT EXISTS idx_games_league_year ON games(league, year);
CREATE INDEX IF NOT EXISTS idx_team_stats_team ON team_game_stats(team_name);
CREATE INDEX IF NOT EXISTS idx_player_stats_player ON player_game_stats(player_name);
