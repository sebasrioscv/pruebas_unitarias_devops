import pytest
from src import conversor
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

# Arrange: preparamos datos. Act: convertimos. Assert: comprobamos el resultado.
@pytest.mark.parametrize("funcion, entrada, esperado", [
    (conversor.celsius_a_kelvin, 0, 273.15),
    (conversor.kelvin_a_celsius, 273.15, 0),
    (conversor.kilometros_a_metros, 2, 2000),
    (conversor.libras_a_kilogramos, 10, 4.53592),
    (conversor.kilogramos_a_libras, 1, 1 / 0.453592),
    (conversor.galones_a_litros, 1, 3.78541),
    (conversor.litros_a_galones, 3.78541, 1),
    (conversor.millas_a_kilometros, 1, 1.60934),
    (conversor.pies_a_metros, 1, 0.3048),
    (conversor.metros_a_pies, 0.3048, 1),
    (conversor.onzas_a_gramos, 1, 28.3495),
    (conversor.gramos_a_onzas, 28.3495, 1),
])

def test_conversiones_adicionales(funcion, entrada, esperado):
    # Arrange
    # Los datos de entrada y el resultado esperado vienen parametrizados.

    # Act
    resultado = funcion(entrada)

    # Assert
    assert resultado == pytest.approx(esperado)

@pytest.mark.parametrize("funcion", [
    conversor.kilometros_a_metros,
    conversor.libras_a_kilogramos,
    conversor.kilogramos_a_libras,
    conversor.galones_a_litros,
    conversor.litros_a_galones,
    conversor.millas_a_kilometros,
    conversor.pies_a_metros,
    conversor.metros_a_pies,
    conversor.onzas_a_gramos,
    conversor.gramos_a_onzas,
])
def test_conversiones_rechazan_valores_negativos(funcion):
    # Arrange
    entrada = -1

    # Act y Assert
    with pytest.raises(ValueError):
        funcion(entrada)
