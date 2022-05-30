from pathlib import Path

from starlette.config import Config


config = Config(Path("./").parent / ".env")
DEBUG = config.get("DEBUG", cast=bool)
HOST = config.get("HOST", default="127.0.0.1")
PORT = config.get("PORT", cast=int, default="8000")

DB_NAME = config.get("DB_NAME", default="recordings")
DB_USER = config.get("DB_USER")
DB_PASSWORD = config.get("DB_PASSWORD")
