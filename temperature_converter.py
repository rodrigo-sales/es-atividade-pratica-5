def celsius_to_fahrenheit(celsius: float) -> float:
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius: float) -> float:
    """Converte Celsius para Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin: float) -> float:
    """Converte Kelvin para Celsius."""
    if kelvin < 0:
        raise ValueError("A temperatura em Kelvin não pode ser negativa.")
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Converte Fahrenheit para Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Converte Kelvin para Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))