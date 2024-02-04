import contextlib
import typing as T
import asyncpg

from records.config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT


pool = None


async def create_pool() -> None:
    global pool
    pool = await asyncpg.create_pool(get_connection_string())


async def close_pool() -> None:
    global pool
    if pool is not None:
        await pool.close()
    pool = None


@contextlib.asynccontextmanager
async def get_connection() -> T.AsyncGenerator[asyncpg.connection.Connection, None]:
    if pool is None:
        # For testing, due to the way pytest_asyncio and async event loops
        # work, it is challenging to maintain a connection pool during async tests
        # since it will error out if the pool is on another event loop.
        # For now, just default to a normal connection if there is no pool.
        cstring = get_connection_string()
        conn = await asyncpg.connect(cstring)
    else:
        conn = await pool.acquire()
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
