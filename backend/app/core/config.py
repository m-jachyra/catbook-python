import secrets
from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_URL: str = "/api"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str = "Catbook"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "Admin123"
    POSTGRES_DB: str = "catbook"

    QUEUE_URL: str = "amqp://guest@queue//"

    AZURE_BLOB_URL: str = ""
    AZURE_STORAGE_CONNECTION_STRING: str = ""

    STORAGE_DIR: str = '/app/storage/'
    IMAGES_DIR: str = '/app/storage/images/'


settings = Settings()
