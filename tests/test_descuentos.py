import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_precio_final,
)


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
