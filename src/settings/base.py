from functools import lru_cache
from typing import Any, Dict

from pydantic_settings import BaseSettings

from .components.logging import logging_settings


class Settings(BaseSettings):
    environment: str
    debug: bool

    logging: Dict[str, Any] = logging_settings

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> BaseSettings:
    return Settings()
