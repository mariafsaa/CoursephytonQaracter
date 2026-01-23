"""
EXAMEN DE ANÁLISIS DE DATOS EN PYTHON
Escenario: Registros simples de ventas

Formato esperado después de la limpieza:
nombre_producto,categoría,precio
"""

# =========================
# Objetivo 1 — Datos en bruto (10 puntos)
# =========================
# Crear una lista con al menos 12 registros de ventas en bruto como strings.
# Incluir:
# - espacios extra
# - diferencias entre mayúsculas y minúsculas
# - precios con comas
# - categorías inválidas
# - precios negativos
# - campos faltantes

# Ejemplo:
# "  T-shirt , Clothes , 19,99 "

# TODO:
# Crear la lista de datos en bruto
# Imprimir cuántos registros en bruto existen


# =========================
# Objetivo 2 — Limpieza de datos (10 puntos)
# =========================
# Crear una función que limpie UN registro:
# - eliminar espacios extra
# - convertir el texto a minúsculas
# - reemplazar la coma por punto en los precios

# TODO:
# Definir la función de limpieza
# Crear una nueva lista con los registros limpios
# Imprimir los dos primeros registros limpios


# =========================
# Objetivo 3 — Validación (15 puntos)
# =========================
# Un registro es válido si:
# - tiene exactamente 3 campos
# - la categoría es válida
# - el precio es >= MIN_PRICE

# TODO:
# Crear listas para:
# - nombres de productos válidos
# - categorías válidas
# - precios válidos
# - registros inválidos
# Recorrer los registros limpios y separar los válidos de los inválidos
# Imprimir cuántos registros válidos e inválidos existen


# =========================
# Objetivo 4 — Filtro por categoría (10 puntos)
# =========================
# Extraer los precios de los productos que pertenecen a la categoría "food".

# TODO:
# Crear una lista con los precios de productos de comida
# Imprimir cuántos productos de comida existen


# =========================
# Objetivo 5 — Precio total y promedio (10 puntos)
# =========================
# Calcular:
# - precio total de los productos de comida
# - precio promedio de los productos de comida
# Si la lista está vacía, el resultado debe ser 0.

# TODO:
# Crear cálculos reutilizables
# Imprimir total y promedio


# =========================
# Objetivo 6 — Producto más caro (10 puntos)
# =========================
# Encontrar el producto con el precio más alto.
# Imprimir:
# - nombre del producto
# - categoría
# - precio

# TODO:
# Encontrar el precio máximo manualmente
# Recuperar los datos del producto relacionado
# Imprimir el resultado


# =========================
# Objetivo 7 — Clasificación de precios (10 puntos)
# =========================
# Contar cuántos productos son:
# - baratos (precio < HIGH_PRICE)
# - caros (precio >= HIGH_PRICE)

# TODO:
# Crear contadores
# Recorrer los precios y clasificar
# Imprimir resultados


# =========================
# Objetivo 8 — Productos sospechosos (10 puntos)
# =========================
# Un producto es sospechoso si:
# - el precio es 0
# O
# - la categoría es "electronics" y el precio < 10

# TODO:
# Crear una lista de mensajes de advertencia
# Imprimir cuántos productos sospechosos existen


# =========================
# Objetivo 9 — Resumen final (10 puntos)
# =========================
# Crear un resumen de texto multilínea que incluya:
# - total de registros en bruto
# - registros válidos
# - registros inválidos
# - precio total y promedio de comida
# - producto más caro
# - cantidad de productos sospechosos

# TODO:
# Construir el string del resumen
# Imprimirlo


# =========================
# Objetivo 10 — Consulta de categoría por el usuario (5 puntos)
# =========================
# Pedir al usuario una categoría.
# Si es válida, calcular e imprimir el precio total para esa categoría.
# Si no es válida, imprimir un mensaje de error.

# TODO:
# Pedir input al usuario
# Validar la categoría
# Calcular e imprimir el total
