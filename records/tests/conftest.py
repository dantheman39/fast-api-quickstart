from pathlib import Path

from alembic import command
from alembic.config import Config
import asyncpg
import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    create_async_engine,
    async_engine_from_config,
)
from sqlalchemy import pool

from records.config import DB_NAME, DB_USER, DB_HOST, DB_PORT, DB_PASSWORD
from records.db.connection import get_connection
from records.db.manage_db import recreate_tables


ALEMBIC_CONFIG_PATH = (Path(__file__).parent.parent.parent / "alembic.ini").resolve()


def run_migrations(connection: AsyncEngine, cfg: Config):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


def clear_db(connection: AsyncEngine, cfg: Config):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "base")


@pytest_asyncio.fixture
async def test_db():
    if "test" not in DB_NAME:
        raise ValueError(
            f"Expected the db name to contain 'test', stopping for safety: {DB_NAME}"
        )

    alembic_cfg = Config(str(ALEMBIC_CONFIG_PATH))
    sys_conn: asyncpg.Connection | None = None
    conn: AsyncConnection | None = None
    try:
        # sys_conn = await asyncpg.connect(
        #     database="template1",
        #     user=DB_USER,
        #     host=DB_HOST,
        #     port=DB_PORT,
        #     password=DB_PASSWORD,
        # )
        # Must be run separately as postgres will automatically
        # create a transaction block if there's more than one
        # await sys_conn.execute(
        #     f"""
        #     DROP DATABASE IF EXISTS {DB_NAME};
        # """
        # )
        # await sys_conn.execute(
        #     f"""
        #     CREATE DATABASE {DB_NAME};
        # """
        # )
        engine = create_async_engine(
            f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
            echo=True,
        )
        async with engine.begin() as conn:
            await conn.run_sync(run_migrations, alembic_cfg)
        # async with get_connection() as conn2:
        #     await recreate_tables(connection=conn2)
        yield
    finally:
        engine = create_async_engine(
            f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
            echo=True,
        )
        async with engine.begin() as conn:
            await conn.run_sync(clear_db, alembic_cfg)
        # if sys_conn is not None:
        #     others = await sys_conn.fetch("SELECT * FROM pg_stat_activity WHERE datname='recordings_test'")
        #     await sys_conn.execute(
        #         f"""
        #         DROP DATABASE IF EXISTS {DB_NAME};
        #     """
        #     )
        #     await sys_conn.close()
