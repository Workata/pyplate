from unittest import mock

from assertpy import assert_that

from settings import get_settings
from settings.components.logging import logging_settings


def test_settings_values(settings):
    assert_that(settings.environment).is_equal_to("test")
    assert_that(settings.environment).is_type_of(str)

    assert_that(settings.debug).is_equal_to(True)
    assert_that(settings.debug).is_type_of(bool)

    assert_that(settings.logging).is_equal_to(logging_settings)
    assert_that(settings.logging).is_type_of(dict)


@mock.patch("settings.base.Settings")
def test_get_settings_should_create_settings(mock_settings_cls):
    settings = get_settings()
    mock_settings_cls.assert_called_once_with()
    assert_that(settings).is_equal_to(mock_settings_cls.return_value)
