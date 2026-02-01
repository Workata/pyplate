from enum import Enum


class EnvType(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    TEST = "test"
    STAGING = "staging"
    ACCEPTANCE = "acceptane"
    PROD = "production"
