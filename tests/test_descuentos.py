import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_precio_final,
)

from src import descuentos 

def test_aplicar_descuento_basico():
    # Arrange
    precio = 120
    porcentaje = 25

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == pytest.approx(90)


def test_aplicar_descuento_cero_por_ciento():
    # Arrange
    precio = 150
    porcentaje = 0

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == pytest.approx(150)


def test_aplicar_descuento_cien_por_ciento():
    # Arrange
    precio = 150
    porcentaje = 100

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == pytest.approx(0)


def test_precio_negativo_lanza_value_error():
    # Arrange
    precio = -50
    porcentaje = 10

    # Act / Assert
    with pytest.raises(ValueError, match="negativo"):
        aplicar_descuento(precio, porcentaje)


def test_porcentaje_superior_a_cien_lanza_value_error():
    # Arrange
    precio = 100
    porcentaje = 120

    # Act / Assert
    with pytest.raises(ValueError, match="porcentaje"):
        aplicar_descuento(precio, porcentaje)


def test_precio_final_aplica_impuesto_sobre_precio_descuentado():
    # Arrange
    precio = 100
    impuesto = 10
    descuento = 20

    # Act
    resultado = calcular_precio_final(
        precio, impuesto, descuento
    )

    # Assert
    assert resultado == pytest.approx(88)

@pytest.mark.parametrize("precio, porcentaje, esperado", [
    (200, 10, 20),
    (50, 0, 0),
])
def test_calcular_monto_descuento(precio, porcentaje, esperado):
    # Arrange
    # Act
    resultado = descuentos.calcular_descuento(precio, porcentaje)

    # Assert
    assert resultado == pytest.approx(esperado)


@pytest.mark.parametrize("precio, porcentaje", [
    (-1, 10),
    (100, -1),
    (100, 101),
])
def test_calcular_descuento_rechaza_datos_invalidos(precio, porcentaje):
    # Arrange, Act y Assert
    with pytest.raises(ValueError):
        descuentos.calcular_descuento(precio, porcentaje)


@pytest.mark.parametrize("precio, impuesto, descuento", [
    (-1, 10, 0),
    (100, -1, 0),
    (100, 10, -1),
    (100, 10, 101),
])
def test_precio_final_rechaza_datos_invalidos(precio, impuesto, descuento):
    # Arrange, Act y Assert
    with pytest.raises(ValueError):
        descuentos.calcular_precio_final(precio, impuesto, descuento)


@pytest.mark.parametrize("cantidad, precio_unitario, esperado", [
    (0, 100, 0),
    (10, 100, 950),
    (20, 100, 1800),
    (50, 100, 4250),
    (100, 100, 8000),
])
def test_descuento_por_volumen(cantidad, precio_unitario, esperado):
    # Arrange
    # Act
    resultado = descuentos.descuento_por_volumen(
        cantidad, precio_unitario
    )

    # Assert
    assert resultado == pytest.approx(esperado)


@pytest.mark.parametrize("cantidad, precio_unitario", [
    (-1, 100),
    (10, -100),
])
def test_descuento_por_volumen_rechaza_negativos(
    cantidad, precio_unitario
):
    # Arrange, Act y Assert
    with pytest.raises(ValueError):
        descuentos.descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_cumulativo_sin_descuentos():
    # Arrange
    precio = 100
    lista_descuentos = []

    # Act
    resultado = descuentos.descuento_cumulativo(
        precio, lista_descuentos
    )

    # Assert
    assert resultado == 100


def test_descuento_cumulativo_aplica_descuentos_secuenciales():
    # Arrange
    precio = 100
    lista_descuentos = [10, 20]

    # Act
    resultado = descuentos.descuento_cumulativo(
        precio, lista_descuentos
    )

    # Assert
    assert resultado == pytest.approx(72)


@pytest.mark.parametrize("precio, lista_descuentos", [
    (-1, [10]),
    (100, [-1]),
    (100, [101]),
])
def test_descuento_cumulativo_rechaza_datos_invalidos(
    precio, lista_descuentos
):
    # Arrange, Act y Assert
    with pytest.raises(ValueError):
        descuentos.descuento_cumulativo(precio, lista_descuentos)


def test_descuento_apilado_sin_descuentos():
    # Arrange
    precio = 100
    lista_descuentos = []

    # Act
    resultado = descuentos.descuento_apilado(
        precio, lista_descuentos
    )

    # Assert
    assert resultado == 100


def test_descuento_apilado_suma_porcentajes():
    # Arrange
    precio = 100
    lista_descuentos = [10, 20]

    # Act
    resultado = descuentos.descuento_apilado(
        precio, lista_descuentos
    )

    # Assert
    assert resultado == pytest.approx(70)


def test_descuento_apilado_rechaza_precio_negativo():
    # Arrange
    precio = -100
    lista_descuentos = [10]

    # Act y Assert
    with pytest.raises(ValueError):
        descuentos.descuento_apilado(precio, lista_descuentos)


def test_descuento_apilado_rechaza_total_superior_a_cien():
    # Arrange
    precio = 100
    lista_descuentos = [60, 50]

    # Act y Assert
    with pytest.raises(ValueError):
        descuentos.descuento_apilado(precio, lista_descuentos)
