"""
Ponto de entrada da Fase 1: carrega os CSVs do Oracle's Elixir já baixados
manualmente em data/raw/oracles_elixir/ para o banco SQLite normalizado.

Uso:
    python main.py
"""

from src.ingestion import oracle_elixir_loader
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    logger.info("=== Carregando dados do Oracle's Elixir ===")
    oracle_elixir_loader.run()


if __name__ == "__main__":
    main()
