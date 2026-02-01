import re

from pyplate.settings import get_settings
from pyplate.shared import EnvType


def test_settings_values():
    pattern = r"^\d+\.\d+\.\d+$"

    settings = get_settings()

    assert settings.environment == EnvType.TEST
    assert re.match(pattern, settings.version)
