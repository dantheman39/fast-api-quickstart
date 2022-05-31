from pydantic import BaseModel


class ArtistIn(BaseModel):
    name: str


class Artist(ArtistIn):
    id: int
    name: str


class _AlbumBase(BaseModel):
    name: str


class AlbumIn(_AlbumBase):
    artist_id: int


class Album(_AlbumBase):
    id: int
    name: str
    artist: Artist
