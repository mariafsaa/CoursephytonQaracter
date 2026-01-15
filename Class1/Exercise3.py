# Sistema de análisis de ventas

# Constantes
HIGH_LIMIT = 2000
MEDIUM_LIMIT = 1000

# Pedir datos al usuario
prod = input("Ingresa el nombre del producto: ")
units = int(input("Ingresa las unidades vendidas: "))
price_unit = float(input("Ingresa el precio por unidad: "))
act_inp = int(input("¿El producto está activo? (1 = Sí, 0 = No): "))

# Convertir 1 / 0 a boolean
act = act_inp == 1
total_sales = units * price_unit

# Clasificar desempeño
if total_sales >= HIGH_LIMIT and act:
    performance = "High Performance "
elif MEDIUM_LIMIT <= total_sales < HIGH_LIMIT:
    performance = "Medium Performance "
else:
    performance = "Low Performance "

# Mostrar reporte
print(f"""
--- ⭐ Reporte de Ventas  ⭐ ---
- Producto: {prod}
- Unidades vendidas: {units}
- Precio unitario: {price_unit:.2f}
- Producto activo: {act}

Total de ventas: {total_sales:.2f}
Desempeño: {performance}
""")
