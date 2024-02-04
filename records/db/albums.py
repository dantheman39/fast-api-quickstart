from records.errors import AlbumNotFound, ArtistNotFound
from records import models
from .connection import get_connection


async def get_album(album_id: int) -> models.Album:
    async with get_connection() as conn:
        result = await conn.fetchrow(
            """
            SELECT
              ar.id AS artist_id,
              ar.name AS artist_name,
              al.id AS album_id,
              al.name AS album_name
            FROM albums AS al
            LEFT JOIN artists AS ar ON al.artist_id = ar.id
            WHERE al.id = $1
        """,
            album_id,
        )
        if result is None:
            raise AlbumNotFound()
        return models.Album.from_db(result)


async def get_albums() -> list[models.Album]:
    async with get_connection() as conn:
        result = await conn.fetch(
            """
            SELECT
              ar.id AS artist_id,
              ar.name AS artist_name,
              al.id AS album_id,
              al.name AS album_name
            FROM albums AS al
              LEFT JOIN artists AS ar ON al.artist_id = ar.id
        """
        )
        return [models.Album.from_db(row) for row in result]


async def create_album(album: models.AlbumIn) -> models.Album:
    async with get_connection() as conn:
        artist = await conn.fetchrow(
            """
            SELECT id FROM artists WHERE id = $1
        """,
            album.artist_id,
        )
        if artist is None:
            raise ArtistNotFound()
        result = await conn.fetch(
            """
            INSERT INTO albums(
                name,
                artist_id
            ) VALUES($1, $2) RETURNING id
        """,
            album.name,
            album.artist_id,
        )

        out = await conn.fetchrow(
            """
            SELECT
              ar.id AS artist_id,
              ar.name AS artist_name,
              al.id AS album_id,
              al.name AS album_name
            FROM albums AS al
            LEFT JOIN artists AS ar ON al.artist_id = ar.id
            WHERE al.id = $1
        """,
            result[0]["id"],
        )

        return models.Album.from_db(out)
