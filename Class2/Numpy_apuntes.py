# NumPy es una librería de Python : 
# Se usa para trabajar con números y grandes cantidades de datos
# Es más rápida y eficiente que las listas normales de Python

# NumPy Usos:
# - Data Science
# - Machine Learning

## Muchas librerías importantes dependen de NumPy: pandas

import numpy as np
print(f"""Version Actual de Numpy: {np.__version__} """)

# Crear un array de NumPy
#normalmente es un solo (tipo de dato), y en este las matemáticas directas a comparacion de listas normales que se relalizan con
# for loops:
nums_array = np.array([1, 2, 3, 4])

# Operaciones con arrays
#Multiplicación por un escalar
result = (nums_array * 2 )  # multiplica todos por 2
print(f"""
Array original:
{nums_array}

Array multiplicado por 2:
{result}
""")
#División por un escalar
# NumPy devuelve decimales aunque los números sean enteros.
nums_array2 = np.array([10, 20, 30, 40])
result2 = nums_array2 / 2  # divide todos por 2
print(f""" 
Array original:
{nums_array2}

Array dividido por 2:
{result2}
""")

#Redondeo de decimales
nums_array3 = np.array([10, 20, 30, 40])
result3 = nums_array2 / 3
result3_rounded = np.round(result3, 2)  # redondea a 2 decimales
print(f""" Array original:
{nums_array3}   


Array dividido por 3 y redondeado a 2 decimales:
{result3_rounded}       """)

# Acceder a elementos
print("Acceder a elementos del array:")
print(f"""Primer elemento : {nums_array2[0]}""")  # Primer elemento
print(f"""Elementos del índice 1 al 2 (Slicing): {nums_array2[1:3]}""")
print(f"""Último elemento : {nums_array2[-1]}""")

# Reordenar elementos
# Invertir = poner el último primero y el primero último
nums4 = np.array([12, 42, 32, 40])
reversed_nums = nums4[::-1]
print("Array invertido:")
print(reversed_nums)
print("Array original:")
print(nums4)

# Ordenar de menor a mayor (np.sort)
sorted_nums = np.sort(nums4)
print("Array original:")
print(nums4)    
print("Array ordenado de menor a mayor:")
print(sorted_nums)

#Puedes hacer dos operacion al tiempo como invertir y ordenar 
# Por ejemplo, ordenar de mayor a menor y luego invertir
sorted_descendente = np.sort(nums4)[::-1]

# Arrrays multidimensionales
# Matrices (2D arrays)
A = np.array([
    [1, 15, 3],
    [4, 5, 60],
])
print(f"""Matriz A:
      {A}""")

#shape: cuántas filas y columnas tiene → (filas, columnas)
# ndim: cuántas dimensiones tiene → en 2D es 2
#size: cuántos elementos totales tiene → filas * columnas
#dtype: tipo de dato → int32, float64, etc.
print(f"""Características de la matriz A:
      Shape (filas, columnas): {A.shape}
      Dimensiones: {A.ndim}
      Tamaño (número total de elementos): {A.size}
      Tipo de dato: {A.dtype}
""")

#Acceder a elementos en matrices
print(f"""Elemento en fila 1, columna 2 de A: {A[0, 1]}""")  # Recuerda que los índices empiezan en 0

#Imprimir una fila completa
print(f"""Fila 2 completa de A: {A[1, :]}""")  # Fila 2 completa
#Imprimir una columna completa
print(f"""Columna 3 completa de A: {A[:, 2]}""")  # Columna 3 completa
# Imprimir columna vertical 
print("Columna 3 completa de A:")
for value in A[:, 2]:
    print(f"[ {value} ]")
# Creacion de matrices de ceros y unos
zeros_matrix = np.zeros((2, 3))  # Matriz de 2 filas y 3 columnas llena de ceros
ones_matrix = np.ones((3, 2))    # Matriz de 3 filas y 2 columnas llena de unos

# zip es una función de Python que permite recorrer dos o más listas/arrays al mismo tiempo, 
# emparejando sus elementos por posición.<
names = ["A", "B", "C"]
scores = [80, 90, 70]

for name, score in zip(names, scores):
    print(name, score)


# ORDENACION DE MATRICES
# En matrices NO se ordena “toda la matriz” como un solo bloque.
# Siempre debes decidir:
# - ¿por filas?
# - ¿por columnas?
# - ¿o solo una fila/columna específica?


M = np.array([
    [30, 10, 20],
    [60, 40, 50],
    [90, 70, 80]
])

print("Matriz original:")
print(M)

# -----------------------------------------
# 1) ORDENAR POR COLUMNAS (axis = 0)
# Cada columna se ordena de forma independiente
# -----------------------------------------
sorted_by_columns = np.sort(M, axis=0)
print("\nOrdenada por columnas (axis=0):")
print(sorted_by_columns)

# -----------------------------------------
# 2) ORDENAR POR FILAS (axis = 1)
# Cada fila se ordena de forma independiente
# -----------------------------------------
sorted_by_rows = np.sort(M, axis=1)
print("\nOrdenada por filas (axis=1):")
print(sorted_by_rows)

# -----------------------------------------
# 3) OBTENER ÍNDICES DE ORDENACIÓN (argsort)
# IMPORTANTE: devuelve POSICIONES, no valores
# -----------------------------------------
row = M[0]  # primera fila
order_idx = np.argsort(row)
print("\nFila original:", row)
print("Índices de orden:", order_idx)
print("Fila ordenada usando índices:", row[order_idx])

# -----------------------------------------
# 4) RANKING EN MATRICES (mayor a menor)
# Se invierte con [::-1]
# -----------------------------------------
ranking_idx = np.argsort(row)[::-1]
print("\nRanking de la fila (mayor a menor):", row[ranking_idx])
