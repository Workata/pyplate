from functools import lru_cache
from typing import Any, Dict

from pydantic_settings import BaseSettings, SettingsConfigDict

from .components.logging import logging_settings


class Settings(BaseSettings):
    environment: str = "dev"
    debug: bool = False
    logging: Dict[str, Any] = logging_settings

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> BaseSettings:
    return Settings()
