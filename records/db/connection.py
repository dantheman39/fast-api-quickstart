import contextlib
import typing as T

import asyncpg

from records.config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT


@contextlib.asynccontextmanager
async def get_connection(
    db_name: str = DB_NAME,
    user: str = DB_USER,
    password: str = DB_PASSWORD,
    host: str = DB_HOST,
    port: str | int = DB_PORT,
) -> T.AsyncGenerator[asyncpg.connection.Connection, None]:
    conn = await asyncpg.connect(
        f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    )
    yield conn
    await conn.close()
    return
