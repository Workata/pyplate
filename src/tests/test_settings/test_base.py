from assertpy import assert_that
from settings import get_settings
from settings.base import Settings
from settings.components.logging import logging_settings


def test_settings_values(settings):
    assert_that(settings.environment).is_equal_to("test")
    assert_that(settings.environment).is_type_of(str)

    assert_that(settings.debug).is_equal_to(True)
    assert_that(settings.debug).is_type_of(bool)

    assert_that(settings.logging).is_equal_to(logging_settings)
    assert_that(settings.logging).is_type_of(dict)


def test_get_settings_should_return_settings():
    settings = get_settings()
    assert_that(settings).is_type_of(Settings)
