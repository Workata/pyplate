# fmt: off
logging_settings = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}][{asctime}] {message}",
            "style": "{",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "./logs/all.log",
            "formatter": "verbose"
        },
    },
    "loggers": {
        "general": {
            "handlers": ["console", "file"],
            "level": "INFO",
        }
    },
}
# fmt: on
