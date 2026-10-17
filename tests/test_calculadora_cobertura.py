import pytest
from src.calculadora import (
    dividir,
    potencia,
    raiz_cuadrada,
    promedio,
    maximo,
    minimo,
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo,
)


def test_dividir_numeros_validos():
    # Arrange
    a, b = 10, 2

    # Act
    resultado = dividir(a, b)

    # Assert
    assert resultado == 5


def test_calcular_potencia():
    # Arrange
    base, exponente = 2, 3

    # Act
    resultado = potencia(base, exponente)

    # Assert
    assert resultado == 8


def test_raiz_cuadrada_de_numero_positivo():
    # Arrange
    numero = 25

    # Act
    resultado = raiz_cuadrada(numero)

    # Assert
    assert resultado == 5


def test_promedio_lista_valida():
    # Arrange
    numeros = [2, 4, 6]

    # Act
    resultado = promedio(numeros)

    # Assert
    assert resultado == 4


def test_promedio_lista_vacia():
    # Arrange
    numeros = []

    # Act / Assert
    with pytest.raises(ValueError):
        promedio(numeros)


def test_maximo_lista_valida():
    # Arrange
    numeros = [3, 9, 1, 5]

    # Act
    resultado = maximo(numeros)

    # Assert
    assert resultado == 9


def test_maximo_lista_vacia():
    # Arrange
    numeros = []

    # Act / Assert
    with pytest.raises(ValueError):
        maximo(numeros)


def test_minimo_lista_vacia():
    # Arrange
    numeros = []

    # Act / Assert
    with pytest.raises(ValueError):
        minimo(numeros)


def test_area_rectangulo_valida():
    # Arrange
    base, altura = 5, 3

    # Act
    resultado = calcular_area_rectangulo(base, altura)

    # Assert
    assert resultado == 15


def test_area_rectangulo_con_base_negativa():
    # Arrange
    base, altura = -5, 3

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)


def test_perimetro_rectangulo_valido():
    # Arrange
    base, altura = 5, 3

    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)

    # Assert
    assert resultado == 16


def test_perimetro_rectangulo_con_altura_negativa():
    # Arrange
    base, altura = 5, -3

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)
