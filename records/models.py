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


class AlbumIn(BaseModel):
    name: str
    artist_id: int


class Album(BaseModel):
    id: int
    name: str
    artist: Artist
