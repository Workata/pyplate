from pydantic import BaseSettings
from typing import Dict, Any


# fmt: off
class Settings(BaseSettings):
    environment: str

    logging: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{levelname}][{asctime}] {message}",
                "style": "{",
            },
            "simple": {
                "format": "[{levelname}] {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple"
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "./logs/all.log",
                "formatter": "verbose"
            },
        },
        "loggers": {
            "general": {
                "handlers": ["console", "file"],
                "level": "INFO",
            }
        },
    }

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
# fmt: on


def get_settings() -> Settings:
    return Settings()
