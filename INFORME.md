# Informe: Análisis y mejora de pruebas unitarias

## 1\. Datos

* **Estudiante:** Juan Sebastian Rios Chalarca
* **Fecha:** 17/10/2026
* **Grupo:** DevOps grupo 1
* **Repositorio:** https://github.com/sebasrioscv/pruebas\_unitarias\_devops

## 2\. Objetivo

El objetivo de este trabajo fue analizar módulos de un proyecto en Python mediante pruebas unitarias con estructura Arrange-Act-Assert (AAA), identificar errores a través de casos límite, corregirlos y medir la cobertura de las pruebas.

## 3\. Pruebas implementadas y análisis por módulo

### 3.1. `calculadora.py`

Este módulo contiene operaciones matemáticas. Se probaron operaciones aritméticas, división por cero, raíz cuadrada, potencia, promedio, máximo y mínimo de listas, y cálculos de área y perímetro de rectángulos. Se incluyeron entradas límite, como listas vacías y valores negativos cuando la operación debe rechazarlos. Las pruebas buscan verificar tanto resultados habituales como el comportamiento ante entradas no válidas.

Archivo(s) de prueba: `tests/test\_calculadora.py` y `tests/test\_calculadora\_cobertura.py`.

### 3.2. `conversor.py`

Este módulo realiza conversiones entre unidades y temperaturas. Se probaron conversiones entre Celsius, Fahrenheit y Kelvin, así como conversiones de distancia y otras unidades. Se incluyeron casos de valores conocidos, distancias negativas y temperatura Kelvin negativa. Estas pruebas permiten comprobar los factores de conversión y las validaciones de entradas no permitidas.

Archivo de prueba: `tests/test\_conversor.py`.

### 3.3. `descuentos.py`

Este módulo calcula descuentos, precios finales e impuestos, y contempla descuentos por volumen y combinaciones de descuentos. Se probaron descuentos del 0 % y 100 %, precios negativos, porcentajes fuera de rango, aplicación de impuestos después del descuento y validaciones de los cálculos combinados. También se incluyeron casos sin descuentos y entradas inválidas para comprobar los límites de cada función.

Archivo de prueba: `tests/test\_descuentos.py`.

### 3.4. Organización de las pruebas

Las pruebas siguen la estructura AAA:

* **Arrange (Preparar):** se definen los datos de entrada y el resultado esperado.
* **Act (Actuar):** se invoca la función que se está probando.
* **Assert (Comprobar):** se compara el resultado obtenido con el esperado o se verifica que se lance una excepción cuando corresponde.

Las pruebas se ejecutaron con `pytest` y el complemento `pytest-cov`.

## 4\. Tabla de bugs encontrados y corregidos

|Función / módulo|Entrada que revela el bug|Resultado erróneo|Resultado esperado y corrección|
|-|-|-|-|
|`raiz\_cuadrada` en `calculadora.py`|Un número negativo, por ejemplo `-4`|No se rechazaba el valor negativo mediante `ValueError`.|Lanzar `ValueError` cuando el argumento es menor que cero.|
|`minimo` en `calculadora.py`|Una lista positiva, por ejemplo `\[3, 8, 1, 5]`|La inicialización en `0` podía devolver `0`, aunque no perteneciera a la lista.|Inicializar el mínimo con el primer elemento de la lista.|
|`kelvin\_a\_celsius` en `conversor.py`|`-1` Kelvin|No se rechazaba una temperatura Kelvin negativa.|Lanzar `ValueError` si Kelvin es menor que cero.|
|`kilometros\_a\_millas` en `conversor.py`|`1` kilómetro|Se multiplicaba por `1.60934`, devolviendo aproximadamente `1.60934` millas.|Dividir los kilómetros entre `1.60934`; un kilómetro equivale aproximadamente a `0.62137` millas.|
|`calcular\_precio\_final` en `descuentos.py`|Precio `100`, impuesto `10 %` y descuento `20 %`|El impuesto se calculaba sobre el precio original y el resultado era `90`.|Primero aplicar el descuento: `100 - 20 % = 80`; luego calcular el impuesto sobre `80`: `80 + 10 % = 88`. La corrección calcula el impuesto sobre `precio\_con\_descuento`.|

## 5\. Cobertura de pruebas

Comando ejecutado:

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

Resultado de cobertura obtenido:

```text
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/\_\_init\_\_.py                0      0   100%
src/autenticacion.py          42     42     0%   6-77
src/calculadora.py            44      0   100%
src/conversor.py              58      1    98%   71
src/csv\_parser.py             76     76     0%   6-127
src/descuentos.py             58      0   100%
src/fibonacci.py              42     42     0%   6-73
src/manipulador\_texto.py      93     93     0%   6-156
src/procesador\_texto.py       49     49     0%   6-84
src/utils.py                  53     53     0%   6-92
src/validador.py              64     64     0%   6-117
--------------------------------------------------------
TOTAL                        579    420    27%
```

### Interpretación

Los módulos trabajados superan la meta del 85 % indicada en el taller: `calculadora.py` alcanzó 100 %, `conversor.py` alcanzó 98 % y `descuentos.py` alcanzó 100 %. En `conversor.py` quedó una línea sin cubrir, la línea 71. La cobertura global del proyecto fue 27 %, porque otros módulos no fueron incluidos en el alcance de estas pruebas y permanecen con 0 % de cobertura.

La cobertura indica cuánto código fue ejecutado durante las pruebas, pero no demuestra por sí sola que el código esté libre de errores. También es importante elegir casos representativos, comprobar resultados esperados y probar entradas límite.

Se ejecutaron 77 casos, contando individualmente los escenarios parametrizados. Confirma la cifra ejecutando `pytest tests/ -v` antes de entregar y ajusta este dato si la salida final muestra otro total.

## 6\. Reflexión final

El trabajo mostró que las pruebas unitarias ayudan a detectar errores que no necesariamente aparecen con entradas habituales. Los casos negativos y los valores límite permitieron encontrar problemas de validación y errores en los cálculos. La estructura AAA facilitó separar la preparación de datos, la ejecución y la verificación del resultado.

También aprendí que corregir una función debe ir acompañado de una prueba que reproduzca el defecto y que compruebe el comportamiento esperado. Finalmente, una cobertura alta es útil, pero no reemplaza el análisis de los casos de prueba ni garantiza que todas las reglas del negocio estén verificadas.

