LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}][{name}][{asctime}] {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
        "file": {"class": "logging.FileHandler", "filename": "./logs/all.log", "formatter": "verbose"},
    },
    "loggers": {
        "root": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
        "googleapiclient.discovery_cache": {"level": "WARNING"},
    },
}
