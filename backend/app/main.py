from fastapi import FastAPI
# from fastapi.security import OAuth2PasswordBearer

from rest.router import router
# from .core.config import settings

app = FastAPI()

# oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(router, prefix="/api")#settings.API_V1_URL)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
