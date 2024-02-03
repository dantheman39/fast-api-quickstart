from pathlib import Path

from starlette.config import Config


config = Config(Path("./").parent / ".env")
DEBUG = config.get("DEBUG", cast=bool)
HOST = config.get("HOST", default="127.0.0.1")
PORT = config.get("PORT", cast=int, default="8000")
ENV = config.get("ENV", default="dev")

test_postfix = "_test" if ENV.lower() == "test" else ""
DB_NAME = config.get("DB_NAME", default="recordings") + test_postfix
DB_USER = config.get("DB_USER")
DB_PASSWORD = config.get("DB_PASSWORD")
# Default is the service name in docker compose
DB_HOST = config.get("DB_HOST", default="db")
DB_PORT = config.get("DB_PORT")
