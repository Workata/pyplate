import yaml


class YamlReader():

    @classmethod
    def read(cls, file_path: str) -> dict:
        with open(file_path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
