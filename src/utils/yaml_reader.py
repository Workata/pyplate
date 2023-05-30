import yaml
from typing import Any


class YamlReader:
    @classmethod
    def read(cls, file_path: str) -> Any:
        with open(file_path, "r") as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as exc:
                print(exc)
                raise
