# lol-worlds-predictor
<<<<<<< HEAD

TCC: modelo de força de times de League of Legends profissional, validado
retroativamente contra edições passadas do Worlds, e aplicado ao vivo à
edição de 2027.

## Status atual

Este projeto está na **fase de ingestão de dados**. A modelagem (rating de
times e simulação de torneio) está deliberadamente deixada como stub —
ver `docs/reading-list.md` para o plano de leitura teórica que precede a
implementação dessa parte.

## Fonte de dados

- **[Oracle's Elixir](https://oracleselixir.com/tools/downloads)** — dados
  de partida profissional de LoL desde 2014, atualizados diariamente,
  distribuídos como CSV anual. Baixe os anos que interessam (recomendo
  pelo menos 2018 em diante, para cobrir várias edições de Worlds) e
  coloque os arquivos em `data/raw/oracles_elixir/`.
- **[Leaguepedia](https://lol.fandom.com/)** (via pacote `hextech`) — usado
  mais adiante para brackets e rosters atualizados de 2027, que o Oracle's
  Elixir não cobre antes da temporada acontecer.

## Estrutura

```
lol-worlds-predictor/
├── data/
│   ├── raw/oracles_elixir/   # CSVs anuais baixados manualmente
│   └── processed/            # banco SQLite consolidado
├── docs/
│   └── reading-list.md       # plano de leitura teórica
├── src/
│   ├── config.py
│   ├── ingestion/
│   │   ├── oracle_elixir_loader.py   # ETL do CSV para o SQLite
│   │   └── leaguepedia_client.py     # wrapper sobre o Leaguepedia
│   ├── db/
│   │   ├── schema.sql         # games / team_game_stats / player_game_stats / team_ratings
│   │   └── database.py
│   ├── rating/
│   │   └── elo.py             # STUB — implementar após leitura teórica
│   └── simulation/
│       └── bracket_simulator.py  # STUB — implementar após leitura teórica
├── main.py
└── requirements.txt
```

## Como rodar a ingestão

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# baixe manualmente os CSVs de https://oracleselixir.com/tools/downloads
# e coloque em data/raw/oracles_elixir/

python main.py
```

Isso cria `data/processed/lol_esports.db` com três tabelas normalizadas:
`games` (1 linha por jogo), `team_game_stats` (2 linhas por jogo) e
`player_game_stats` (10 linhas por jogo).

## Próximos passos (depois da leitura teórica)

1. Implementar `src/rating/elo.py` (ou trocar por Bradley-Terry, conforme
   a leitura indicar) e rodar sobre o histórico consolidado.
2. Fazer o backtest: para cada Worlds de 2018 a 2026, calcular o rating
   dos times classificados na véspera do torneio e comparar com o
   resultado real.
3. Implementar `src/simulation/bracket_simulator.py` (Monte Carlo sobre o
   bracket).
4. Repetir o processo em 2027 com dados atualizados como aplicação ao vivo.

Ver `docs/reading-list.md` para a bibliografia que sustenta essas decisões.
=======
Projeto para predição de partidas competitivas de League of Legends
>>>>>>> 8393e1d1fa54aac42dd8a60bd953b3d2f3d6e683
