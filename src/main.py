from loaders import ConfigLoader
from utils import Logger


def main() -> None:
    logger = Logger(logs_location="default")
    logger.info("Hello python!")

    print("Hello python!")
    print(ConfigLoader.load(config_file_path="./config_example.yaml"))


if __name__ == "__main__":
    main()
