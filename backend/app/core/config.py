import secrets
from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_URL: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    QUEUE_URL: str = "amqp://guest@queue//"

    AZURE_BLOB_URL: str

    STORAGE_DIR: str = '/app/storage/'
    IMAGES_DIR: str = '/app/storage/images/'


settings = Settings()
