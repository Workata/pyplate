from pathlib import Path

import pytest
from dotenv import load_dotenv

from pyplate.settings import Settings, get_settings


@pytest.fixture(scope="session", autouse=True)
def set_env_vars():
    load_dotenv(Path("./tests/.env.test"))
    get_settings.cache_clear()


@pytest.fixture
def settings() -> Settings:
    return get_settings()
