from fastapi import FastAPI
import uvicorn

from .config import DEBUG


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome Home"}


def main():
    uvicorn.run(
        app=__name__ + ":app",
        reload=DEBUG,
    )


if __name__ == "__main__":
    main()
