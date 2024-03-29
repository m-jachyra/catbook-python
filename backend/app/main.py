from fastapi import FastAPI
import uvicorn

from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

# from fastapi.security import OAuth2PasswordBearer

from rest.router import router
from core.config import settings

app = FastAPI()

origins = [
    "http://localhost:3000"
    "https://localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/storage', StaticFiles(directory=settings.IMAGES_DIR), name='static')

# oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(router, prefix=settings.API_V1_URL)

add_pagination(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
