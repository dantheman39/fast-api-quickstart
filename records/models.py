from asyncpg import Record
from pydantic import BaseModel


class ArtistIn(BaseModel):
    name: str


# Note that I could have this inherit
# from ArtistIn, but this is short
# just a little easier to read, and
# it's just so simple
class Artist(BaseModel):
    id: int
    name: str

    @classmethod
    def from_db(cls, row: Record):
        return cls(id=row["id"], name=row["name"])


class AlbumIn(BaseModel):
    name: str
    artist_id: int


class Album(BaseModel):
    id: int
    name: str
    artist: Artist

    @classmethod
    def from_db(cls, row: Record):
        return cls(
            id=row["album_id"],
            name=row["album_name"],
            artist=Artist(
                id=row["artist_id"],
                name=row["artist_name"],
            ),
        )
