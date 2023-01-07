from loaders import ConfigLoader


def main() -> None:
    print("Hello python!")
    print(ConfigLoader.load(config_file_path="./config.yaml"))


if __name__ == "__main__":
    main()
