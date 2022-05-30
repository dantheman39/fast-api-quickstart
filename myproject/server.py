from fastapi import FastAPI
import uvicorn

from .config import DEBUG, HOST, PORT


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome Home ya big lug"}


def main():
    uvicorn.run(app=__name__ + ":app", reload=DEBUG, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
