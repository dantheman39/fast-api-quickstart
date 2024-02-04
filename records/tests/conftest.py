from os import environ

import asyncpg
import pytest_asyncio

environ["ENV"] = "test"

# We have to update the ENV before importing, so ignore flake8's complaints.
# See docs for starlette config.
from records.config import DB_NAME, DB_USER, DB_HOST, DB_PORT, DB_PASSWORD  # noqa: E402
from records.db.connection import get_connection  # noqa: E402
from records.db.manage_db import recreate_tables  # noqa: E402


@pytest_asyncio.fixture
async def test_db():
    if "test" not in DB_NAME:
        raise ValueError(
            f"Expected the db name to contain 'test', stopping for safety: {DB_NAME}"
        )
    sys_conn: asyncpg.Connection | None = None
    try:
        sys_conn = await asyncpg.connect(
            database="template1",
            user=DB_USER,
            host=DB_HOST,
            port=DB_PORT,
            password=DB_PASSWORD,
        )
        # Must be run separately as postgres will automatically
        # create a transaction block if there's more than one
        await sys_conn.execute(
            f"""
            DROP DATABASE IF EXISTS {DB_NAME};
        """
        )
        await sys_conn.execute(
            f"""
            CREATE DATABASE {DB_NAME};
        """
        )
        async with get_connection() as conn:
            await recreate_tables(connection=conn)
        yield
    finally:
        if sys_conn is not None:
            await sys_conn.execute(
                f"""
                DROP DATABASE IF EXISTS {DB_NAME};
            """
            )
            await sys_conn.close()
