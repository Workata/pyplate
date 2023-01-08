from utils import YamlReader
from typing import Any


class ConfigLoader:
    @classmethod
    def load(cls, config_file_path: str) -> Any:
        return YamlReader.read(file_path=config_file_path)
