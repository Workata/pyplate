import yaml
from typing import Any


class YamlReader:
    @classmethod
    def read(cls, file_path: str) -> Any:
        with open(file_path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
