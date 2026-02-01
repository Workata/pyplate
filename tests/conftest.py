import pytest
from pyplate.settings import Settings, get_settings
from pathlib import Path
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def set_env_vars():
    load_dotenv(Path("./tests/.env.test"))
    get_settings.cache_clear()


@pytest.fixture
def settings() -> Settings:
    return get_settings()
