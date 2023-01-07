from utils import YamlReader


class ConfigLoader():

    @classmethod
    def load(cls, config_file_path: str) -> dict:
        return YamlReader.read(file_path=config_file_path)
