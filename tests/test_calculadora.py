import pytest
from src.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    raiz_cuadrada,
    minimo,
)


def test_sumar_dos_positivos():
    # Arrange
    a, b = 7, 5

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == 12


def test_restar_con_resultado_negativo():
    # Arrange
    a, b = 3, 8

    # Act
    resultado = restar(a, b)

    # Assert
    assert resultado == -5


def test_multiplicar_por_cero():
    # Arrange
    a, b = 0, 9

    # Act
    resultado = multiplicar(a, b)

    # Assert
    assert resultado == 0


def test_dividir_por_cero_lanza_value_error():
    # Arrange
    a, b = 10, 0

    # Act / Assert
    with pytest.raises(ValueError, match="cero"):
        dividir(a, b)


def test_raiz_cuadrada_de_negativo_lanza_value_error():
    # Arrange
    numero = -4

    # Act / Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


def test_minimo_de_lista_positiva():
    # Arrange
    numeros = [3, 8, 1, 5]

    # Act
    resultado = minimo(numeros)

    # Assert
    assert resultado == 1
