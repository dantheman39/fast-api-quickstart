import contextlib
import typing as T

import asyncpg
from records.config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT


@contextlib.asynccontextmanager
async def get_connection() -> T.AsyncGenerator[asyncpg.connection.Connection, None]:
    conn = await asyncpg.connect(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    yield conn
    await conn.close()
    return
