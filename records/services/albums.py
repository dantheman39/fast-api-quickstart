from records.db import albums as db_albums
from records import models


async def get_albums() -> list[models.Album]:
    return await db_albums.get_albums()


async def get_album(album_id: int) -> models.Album:
    return await db_albums.get_album(album_id=album_id)


async def create_album(album: models.AlbumIn) -> models.Album:
    return await db_albums.create_album(album=album)
