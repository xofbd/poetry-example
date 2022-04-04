import pytest

from tempconv import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
)


@pytest.mark.parametrize('deg_F,deg_C', [(-40, -40), (32, 0), (212, 100)])
def test_fahrenheit_to_celsius(deg_F, deg_C):
    """
    GIVEN a temperature in Fahrenheit
    WHEN fahrenheit_to_celsius is called
    THEN the converted temperature in Celsius is returned
    """

    assert deg_C == fahrenheit_to_celsius(deg_F)


@pytest.mark.parametrize('deg_C,deg_F', [(-40, -40), (0, 32), (100, 212)])
def test_celsius_to_fahrenheit(deg_C, deg_F):
    """
    GIVEN a temperature in Celsius
    WHEN celsius_to_fahrenheit is called
    THEN the converted temperature in Fahrenheit is returned
    """
    assert deg_F == celsius_to_fahrenheit(deg_C)


@pytest.mark.parametrize('deg_C,temp_kelvin', [
    (-273.15, 0),
    (0, 273.15),
    (100, 373.15)
])
def test_celsius_to_kelvin(deg_C, temp_kelvin):
    """
    GIVEN a temperature in Celsius
    WHEN celsius_to_kelvin is called
    THEN the converted temperature in Kelvin is returned
    """
    assert temp_kelvin == celsius_to_kelvin(deg_C)


@pytest.mark.parametrize('deg_F,temp_kelvin', [
    (-459.67, 0),
    (32, 273.15),
    (212, 373.15)
])
def test_fahrenheit_to_kelvin(deg_F, temp_kelvin):
    """
    GIVEN a temperature in Fahrenheit
    WHEN fahrenheit_to_kelvin is called
    THEN the converted temperature in Kelvin is returned
    """
    assert temp_kelvin == pytest.approx(fahrenheit_to_kelvin(deg_F))
