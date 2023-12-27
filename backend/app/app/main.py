from fastapi import FastAPI
# from fastapi.security import OAuth2PasswordBearer

# from .rest.router import router
#from .core.config import settings
# from .db_context.context import SessionLocal


app = FastAPI()

# oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


# def get_db():
#     print("DUPA")
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# app.include_router(router, prefix="/")#settings.API_V1_URL)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
