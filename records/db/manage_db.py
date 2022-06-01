from asyncpg import Connection


async def drop_tables(connection: Connection) -> None:
    await connection.execute(
        """
        DROP TABLE IF EXISTS artists CASCADE;
        DROP TABLE IF EXISTS albums;
    """
    )


async def create_tables(connection: Connection) -> None:
    await connection.execute(
        """
        CREATE TABLE artists(
            id INT GENERATED ALWAYS AS IDENTITY,
            name VARCHAR(255) NOT NULL,
            PRIMARY KEY(id)
        );

        CREATE TABLE albums(
            id INT GENERATED ALWAYS AS IDENTITY,
            name VARCHAR(255) NOT NULL,
            artist_id INT,
            PRIMARY KEY(id),
            CONSTRAINT fk_artist
              FOREIGN KEY(artist_id)
                REFERENCES artists(id)
        )
    """
    )


async def recreate_tables(connection: Connection) -> None:
    await drop_tables(connection)
    await create_tables(connection)
