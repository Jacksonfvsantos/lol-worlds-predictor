import sqlite3
from contextlib import contextmanager
from pathlib import Path

from src.config import SQLITE_PATH
from src.utils.logger import get_logger

logger = get_logger(__name__)
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


@contextmanager
def get_connection():
    SQLITE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    with get_connection() as conn:
        with open(SCHEMA_PATH, encoding="utf-8") as f:
            conn.executescript(f.read())
    logger.info("Banco inicializado em %s", SQLITE_PATH)


if __name__ == "__main__":
    init_db()
