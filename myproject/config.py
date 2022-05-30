from pathlib import Path

from starlette.config import Config


config = Config(Path("./").parent / ".env")
DEBUG = config.get("DEBUG", cast=bool)
HOST = config.get("HOST", default="127.0.0.1")
PORT = config.get("PORT", cast=int, default="8000")
