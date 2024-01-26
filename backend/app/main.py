from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import OAuth2PasswordBearer

from rest.router import router
# from .core.config import settings

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(router, prefix="/api")#settings.API_V1_URL)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
