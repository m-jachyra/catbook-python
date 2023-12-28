import secrets
from typing import List

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    API_V1_URL: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_SERVER: str = "127.0.0.1:5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "Admin123"
    POSTGRES_DB: str = "catbook"

    QUEUE_URL: str = "amqp://guest@queue//"

    AZURE_BLOB_URL: str

settings = Settings()
