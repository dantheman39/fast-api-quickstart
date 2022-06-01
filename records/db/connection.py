import contextlib
import typing as T

import asyncpg

from records.config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT
from records.errors import DBNotSetUp


CONNECTION_STRING: str | None = None


@contextlib.asynccontextmanager
async def get_connection() -> T.AsyncGenerator[asyncpg.connection.Connection, None]:
    if CONNECTION_STRING is None:
        raise DBNotSetUp("Call setup_db() before using this function")
    conn = await asyncpg.connect(CONNECTION_STRING)
    yield conn
    await conn.close()
    return


def setup_db(
    db_name: str = DB_NAME,
    user: str = DB_USER,
    password: str = DB_PASSWORD,
    host: str = DB_HOST,
    port: str | int = DB_PORT,
    force_new: bool = False,
) -> None:
    global CONNECTION_STRING
    if not force_new and CONNECTION_STRING is not None:
        # TODO logging
        print("Connection string already created and force_new is False, doing nothing")
        return None
    CONNECTION_STRING = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
