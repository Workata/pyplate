from loaders import ConfigLoader
import pytest
from assertpy import assert_that
from typing import Any


@pytest.fixture
def loaded_config_file() -> Any:
    return ConfigLoader.load(config_file_path="./config_example.yaml")


def test_config_example_content(loaded_config_file: Any) -> None:
    assert_that(loaded_config_file["instance_file_path"]).is_equal_to("./instances/example1.txt")
