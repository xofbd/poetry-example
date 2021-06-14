def fahrenheit_to_celsius(deg_F):
    """Convert degrees Fahrenheit to Celsius."""
    return (5 / 9) * (deg_F - 32)


def celsius_to_fahrenheit(deg_C):
    """Convert degrees Celsius to Fahrenheit."""
    return (9 / 5) * deg_C + 32


def celsius_to_kelvin(deg_C):
    """Convert degree Celsius to Kelvin."""
    return deg_C + 273.15


def fahrenheit_to_kelvin(deg_F):
    """Convert degree Fahrenheit to Kelvin."""
    deg_C = fahrenheit_to_celsius(deg_F)

    return celsius_to_kelvin(deg_C)
