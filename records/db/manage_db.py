from asyncpg import Connection
from pathlib import Path


async def drop_tables(connection: Connection) -> None:
    await connection.execute(_drop_sql)


async def create_tables(connection: Connection) -> None:
    await connection.execute(_create_sql)


async def recreate_tables(connection: Connection) -> None:
    await drop_tables(connection)
    await create_tables(connection)


_drop_sql = ""
_create_sql = ""


# These are small. We can just read them into memory at startup,
# so we don't have to read them every time we make a query.
def read_sql_files():
    global _drop_sql, _create_sql
    script_dir = Path(__file__).parent.parent.parent / "sql"
    with open(script_dir / "00-drop-tables.sql") as fh:
        _drop_sql = fh.read()
    with open(script_dir / "01-create-tables.sql") as fh:
        _create_sql = fh.read()


read_sql_files()
