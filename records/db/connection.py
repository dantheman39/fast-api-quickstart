import contextlib
import typing as T

import asyncpg

from records.config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT


@contextlib.asynccontextmanager
async def get_connection() -> T.AsyncGenerator[asyncpg.connection.Connection, None]:
    cstring = get_connection_string()
    conn = await asyncpg.connect(cstring)
    yield conn
    await conn.close()
    return


def get_connection_string(
    db_name: str = DB_NAME,
    user: str = DB_USER,
    password: str = DB_PASSWORD,
    host: str = DB_HOST,
    port: str | int = DB_PORT,
) -> str | None:
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
