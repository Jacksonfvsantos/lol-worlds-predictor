"""
Módulo de rating de força de times via sistema Elo.

INTENCIONALMENTE NÃO IMPLEMENTADO AINDA.

Este é só o esqueleto da interface que o resto do pipeline vai chamar.
A implementação (fórmula de atualização, K-factor, tratamento de
vantagem de lado azul/vermelho, decaimento entre splits, etc.) deve
vir depois da leitura sobre sistemas de rating — ver docs/reading-list.md.

Perguntas para responder com a leitura antes de implementar:
- Qual K-factor faz sentido para o volume de jogos por time em LoL pro
  (bem menor que em xadrez, por exemplo)?
- Vale a pena resetar/regredir o rating parcialmente entre splits
  (jogadores e composições mudam)?
- Como tratar times novos/promovidos sem histórico (rating inicial)?
"""

from dataclasses import dataclass


@dataclass
class EloConfig:
    k_factor: float
    initial_rating: float = 1500.0


class EloRatingModel:
    def __init__(self, config: EloConfig):
        self.config = config
        self.ratings: dict[str, float] = {}

    def get_rating(self, team_name: str) -> float:
        return self.ratings.get(team_name, self.config.initial_rating)

    def expected_score(self, team_a: str, team_b: str) -> float:
        """Probabilidade esperada de team_a vencer team_b, dado o rating atual."""
        raise NotImplementedError("Implementar após leitura sobre sistemas Elo.")

    def update(self, winner: str, loser: str) -> None:
        """Atualiza os ratings de winner e loser após uma partida."""
        raise NotImplementedError("Implementar após leitura sobre sistemas Elo.")
