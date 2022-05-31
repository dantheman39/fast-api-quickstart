from records.models import Artist, ArtistIn
from records.db import artists as db_artists
from records.errors import ArtistNotFound


async def get_artists() -> list[Artist]:
    return await db_artists.get_artists()


async def get_artist(artist_id: int) -> Artist:
    artist = await db_artists.get_artist(artist_id=artist_id)
    if artist is None:
        raise ArtistNotFound()
    return artist


async def create_artist(artist: ArtistIn) -> Artist:
    return await db_artists.create_artist(artist)
