import tomllib
from functools import lru_cache

from pydantic import AliasChoices, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from pyplate.shared import EnvType


class Settings(BaseSettings):
    environment: EnvType = Field(default=EnvType.LOCAL, validation_alias=AliasChoices("environment", "env"))

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @computed_field
    @property
    def version(self) -> str:
        with open("./pyproject.toml", "rb") as f:
            version: str = tomllib.load(f)["project"]["version"]
            return version


@lru_cache
def get_settings() -> Settings:
    return Settings()
