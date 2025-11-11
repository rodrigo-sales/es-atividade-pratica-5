import pytest
from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 2) == 0
    assert round(fahrenheit_to_celsius(212), 2) == 100

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(-273.15) == 0

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)

def test_cross_conversions():
    f = 451
    k = fahrenheit_to_kelvin(f)
    f2 = kelvin_to_fahrenheit(k)
    assert abs(f - f2) < 1e-6