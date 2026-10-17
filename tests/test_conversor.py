import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    kelvin_a_celsius,
    metros_a_kilometros,
    kilometros_a_millas,
)


def test_cero_celsius_a_fahrenheit():
    # Arrange
    temperatura = 0

    # Act
    resultado = celsius_a_fahrenheit(temperatura)

    # Assert
    assert resultado == pytest.approx(32)


def test_punto_congelacion_fahrenheit_a_celsius():
    # Arrange
    temperatura = 32

    # Act
    resultado = fahrenheit_a_celsius(temperatura)

    # Assert
    assert resultado == pytest.approx(0)


def test_metros_a_kilometros():
    # Arrange
    distancia = 1500

    # Act
    resultado = metros_a_kilometros(distancia)

    # Assert
    assert resultado == pytest.approx(1.5)


def test_distancia_negativa_lanza_value_error():
    # Arrange
    distancia = -10

    # Act / Assert
    with pytest.raises(ValueError):
        metros_a_kilometros(distancia)


def test_kelvin_negativo_lanza_value_error():
    # Arrange
    temperatura = -1

    # Act / Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(temperatura)


def test_un_kilometro_a_millas():
    # Arrange
    distancia = 1

    # Act
    resultado = kilometros_a_millas(distancia)

    # Assert
    assert resultado == pytest.approx(1 / 1.60934)
