from utils import YamlReader
from unittest.mock import patch, mock_open, Mock, MagicMock
from assertpy import assert_that
import yaml
import pytest


def test_read_correct_yaml() -> None:
    with patch("builtins.open", mock_open(read_data="a: b\nc: d")) as _:
        content = YamlReader.read(file_path=Mock())
        assert_that(content).is_equal_to({"a": "b", "c": "d"})


@patch.object(yaml, "safe_load")
def test_read_incorrect_yaml(mock_safe_load: MagicMock) -> None:
    mock_safe_load.side_effect = yaml.YAMLError
    with patch("builtins.open", mock_open(read_data=None)) as _:
        with pytest.raises(yaml.YAMLError) as _:
            YamlReader.read(file_path=Mock())
