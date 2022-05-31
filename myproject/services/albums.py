from myproject.db import albums as db_albums
from myproject.errors import AlbumNotFound
from myproject import models


async def get_albums() -> list[models.Album]:
    return await db_albums.get_albums()


async def get_album(album_id: int) -> models.Album:
    album = await db_albums.get_album(album_id=album_id)
    if album is None:
        raise AlbumNotFound()
    return album


async def create_album(album: models.AlbumIn) -> models.Album:
    return await db_albums.create_album(album=album)
