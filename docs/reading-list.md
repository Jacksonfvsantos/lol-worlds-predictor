# Lista de Leitura — Fase Teórica

Ordem sugerida de leitura, do mais fundamental ao mais específico. A ideia é
sair dessa fase com clareza sobre: (1) como sistemas de rating funcionam,
(2) o que já foi tentado em predição de MOBA, e (3) como simular um torneio
de forma estatisticamente defensável.

## 1. Fundamentos de sistemas de rating (base teórica, ler primeiro)

- **Elo, A. (1978)** — *The Rating of Chessplayers, Past and Present*. O
  sistema original. Mesmo sendo de xadrez, é a base de tudo que vem depois.
- **Bradley, R. & Terry, M. (1952)** — *Rank Analysis of Incomplete Block
  Designs*. O paper original do modelo Bradley-Terry — alternativa
  probabilística mais formal ao Elo, muito usada em esportes.
- Procure também por resumos/tutoriais modernos de **TrueSkill** (Microsoft,
  usado em matchmaking do Xbox Live) — não precisa ler o paper completo,
  mas entender a ideia de incerteza sobre o rating (não só o valor médio)
  é relevante para justificar escolhas de modelagem depois.

## 2. Predição de resultado em MOBA (linha histórica)

- **Conley, K. & Perry, D. (2013)** — *How Does He Saw Me? A Recommendation
  Engine for Picking Heroes in Dota 2*. Um dos primeiros trabalhos da área;
  bom para contextualizar de onde a pesquisa partiu.
- **Kalyanaraman, K. (2014)** — trabalho de predição de resultado via draft
  em Dota 2, citado por praticamente todo trabalho posterior.
- **"Using Machine Learning to Predict Game Outcomes Based on
  Player-Champion Experience in League of Legends"** (arXiv 2108.02799) —
  específico de LoL, usa dados via API oficial, boa referência metodológica
  próxima do que você vai fazer (mesmo focando em jogador, não time).
- **"Machine Learning Methods for Predicting League of Legends Game
  Outcome"** (IEEE, 2021) — foco em dados pré-jogo/draft, métricas de
  avaliação bem documentadas.

## 3. Nível time / competitivo (mais próximo do seu escopo real)

- **"Predicting League of Legends Match Outcomes Through ML Using Past
  Match Player Performance"** (IEEE) — usa histórico de desempenho de
  jogadores para prever partidas competitivas, não só ranqueada.
- **DraftRec** (ACM WWW '22) — mais avançado (recomendação hierárquica de
  pick), mas a seção de trabalhos relacionados é um ótimo mapa da
  literatura de predição em MOBA.
- Procure por trabalhos que citem o **Oracle's Elixir** diretamente como
  fonte — eles vão ter lidado com as mesmas particularidades de dados que
  você vai enfrentar (rebrands de time, mudança de liga, etc.).

## 4. Previsão/simulação de torneio (o problema estatístico "campeão único")

- Procure por artigos/posts técnicos do **FiveThirtyEight sobre o método
  SPI** (Soccer Power Index) usado para simular a Copa do Mundo — não é
  paper acadêmico formal, mas é a referência mais citada de "como simular
  um torneio de eliminação a partir de um rating de força de time via
  Monte Carlo". Muito aplicável ao seu caso.
- Pesquise também **"bracket prediction" OR "tournament simulation"
  "Monte Carlo"** em conjunto com esportes de eliminação simples/dupla —
  a lógica é a mesma independente do esporte.

## 5. Antes de sair lendo tudo de uma vez

Vale ler com uma pergunta guia na cabeça: **"o que esse paper faria
diferente se os dados fossem de LoL profissional e o objetivo fosse
simular quem ganha o Worlds, não só quem ganha uma partida?"** Isso ajuda
a filtrar o que é diretamente aplicável do que é só contexto.

## Onde buscar

- Google Scholar, arXiv, IEEE Xplore, ACM Digital Library — sua faculdade
  provavelmente tem acesso institucional a IEEE/ACM via CAPES/portal de
  periódicos; vale checar antes de esbarrar em paywall.
