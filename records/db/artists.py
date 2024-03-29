from .connection import get_connection
from records.errors import ArtistNotFound
from records import models


async def create_artist(artist: models.ArtistIn) -> models.Artist:
    async with get_connection() as conn:
        result = await conn.fetch(
            """
            INSERT INTO artists(name) VALUES($1) RETURNING id
        """,
            artist.name,
        )
        row = await conn.fetchrow(
            "SELECT * FROM artists WHERE id = $1", result[0]["id"]
        )
        return models.Artist.from_db(row)


async def get_artists() -> list[models.Artist]:
    async with get_connection() as conn:
        artists = await conn.fetch(
            """
            SELECT * FROM artists
        """
        )
        return [models.Artist(id=a["id"], name=a["name"]) for a in artists]


async def get_artist(artist_id: int) -> models.Artist:
    async with get_connection() as conn:
        artist = await conn.fetchrow(
            """
            SELECT * FROM artists
              WHERE id = $1
        """,
            artist_id,
        )
        if artist is None:
            raise ArtistNotFound()
        return models.Artist(id=artist["id"], name=artist["name"])
