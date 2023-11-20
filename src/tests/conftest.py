import pytest
from dotenv import find_dotenv

from settings.base import Settings


@pytest.fixture
def settings():
    """
    Overwrite config source for testing
    https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
    """
    return Settings(_env_file=find_dotenv(".env.test"))
