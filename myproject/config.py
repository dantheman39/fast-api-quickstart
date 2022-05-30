from pathlib import Path

from starlette.config import Config


config = Config(Path("./").parent / ".env")
DEBUG = config.get("DEBUG", cast=bool)
