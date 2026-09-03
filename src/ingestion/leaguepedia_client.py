"""
Wrapper fino sobre o pacote `hextech`, usado para buscar metadados que o
Oracle's Elixir não cobre bem: nome oficial de torneios, chaveamento
(bracket) e rosters mais atualizados — útil sobretudo mais perto do
Worlds 2027, quando precisarmos saber quem se classificou.

Este módulo é só um ponto de entrada fino; a lógica pesada de matching
entre nomes de time do Oracle's Elixir e do Leaguepedia (nem sempre
idênticos) fica para quando essa necessidade aparecer de fato — não
antecipar aqui.

Uso:
    from src.ingestion.leaguepedia_client import get_tournament_matches
    matches = get_tournament_matches("Worlds 2025")
"""

import hextech

from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_tournament_matches(tournament_name: str):
    """Retorna as partidas (Match objects) de um torneio pelo nome exato do Leaguepedia."""
    tournaments = hextech.getTournaments()
    if tournament_name not in tournaments:
        logger.warning("Torneio '%s' não encontrado no Leaguepedia.", tournament_name)
        return []
    return list(tournaments[tournament_name].getMatches().values())
