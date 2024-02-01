from fastapi import FastAPI, HTTPException
import uvicorn

from .config import DEBUG, HOST, PORT
from .models import Artist, ArtistIn, AlbumIn, Album
from records.errors import AlbumNotFound, ArtistNotFound
from records.services import artists as artists_service, albums as albums_service

app = FastAPI()


@app.get("/artists", response_model=list[Artist])
async def get_artists() -> list[Artist]:
    return await artists_service.get_artists()


@app.get("/artists/{artist_id}", response_model=Artist)
async def get_artist(artist_id: int) -> Artist:
    try:
        return await artists_service.get_artist(artist_id=artist_id)
    except ArtistNotFound:
        raise HTTPException(
            status_code=400, detail=f"Artist not found for id: {artist_id}"
        )


@app.post("/artists", response_model=Artist, status_code=201)
async def post_artist(artist: ArtistIn) -> Artist:
    return await artists_service.create_artist(artist)


@app.get("/albums", response_model=list[Album])
async def get_albums() -> list[Album]:
    return await albums_service.get_albums()


@app.get("/albums/{album_id}", response_model=Album)
async def get_album(album_id: int) -> Album:
    try:
        return await albums_service.get_album(album_id=album_id)
    except AlbumNotFound:
        raise HTTPException(
            status_code=400, detail=f"Album not found for id: {album_id}"
        )


@app.post("/albums", response_model=Album, status_code=201)
async def post_album(album: AlbumIn) -> Album:
    try:
        return await albums_service.create_album(album)
    except ArtistNotFound:
        raise HTTPException(
            status_code=400,
            detail=f"Artist not found for id: {album.artist_id}, can't create Album",
        )


@app.get("/")
async def home():
    return {"message": "Welcome Home ya big lug"}


def main():
    uvicorn.run(app=__name__ + ":app", reload=DEBUG, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
