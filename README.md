# lol-worlds-predictor

**TCC (Engenharia da Computação - Unijorge):** Modelo preditivo de Machine Learning para simulação de resultados do *League of Legends World Championship* (Worlds 2027), baseado em métricas de *early game*, *macro game* e taxas de vitória sazonais.

---

## 📌 Status do Projeto

- [x] **Ingestão de Dados:** Leitura e consolidação de históricos sazonais do Oracle's Elixir em Pandas DataFrames.
- [x] **Engenharia de Recursos (Feature Engineering):** Agrupamento por equipe e extração de deltas de performance (`golddiffat15`, `firstblood`, `firstdragon`, `firsttower`, `vspm`, `winrate`).
- [x] **Modelagem Preditiva:** Algoritmo de Regressão Logística treinado com **~62,7% de acurácia** em mais de 25.000 confrontos históricos. Modelo persistido via `joblib`.
- [x] **Integração em Tempo Real:** Consulta dinâmica de chaveamentos e elencos na API Cargo da Leaguepedia (`mwclient`).
- [x] **Tratamento de Divergências:** Mapeamento de nomes de equipes (*aliasing*) para padronização entre fontes de dados.
- [ ] **Próxima Etapa:** Desenvolvimento do simulador do torneio (Fase Suíça e Playoffs) via método de Monte Carlo.

---

## 🛠️ Stack Tecnológica & Arquitetura

- **Ambiente de Execução:** Google Colab
- **Armazenamento de Dados e Modelos:** Google Drive (arquivos `.csv` brutos e modelo `.pkl`)
- **Linguagem:** Python 3.10+
- **Análise & Manipulação de Dados:** `pandas`, `numpy`
- **Machine Learning:** `scikit-learn` (Regressão Logística), `joblib`
- **Integração Web:** `mwclient` (com trava `urllib3<2.0.0` para compatibilidade com a API MediaWiki/Cargo da Leaguepedia)
- **Controle de Versão:** GitHub

---

## 📁 Estrutura do Repositório

```text
lol-worlds-predictor/
├── .gitignore
├── README.md
├── requirements.txt
├── notebooks/
│   └── worlds_predictor_pipeline.ipynb   # Pipeline principal do Colab
├── src/
│   ├── data_loader.py                   # Módulos reutilizáveis (opcional)
│   ├── feature_engineering.py
│   └── predictor.py
└── data/
    └── .gitkeep                         # Mantém a pasta no Git sem subir CSVs
