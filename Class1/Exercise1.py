# Pedir datos al usuario
nombre_producto = input("Ingresa el nombre del producto: ")
unidades_vendidas = int(input("Ingresa las unidades vendidas: "))
precio_unitario = float(input("Ingresa el precio por unidad: "))

# Calcular el ingreso total
ingreso_tot = unidades_vendidas * precio_unitario

# Mostrar resumen
print(f"""
--- Resumen de Ventas ---
Producto: {nombre_producto}
Unidades vendidas: {unidades_vendidas}
Precio unitario: {precio_unitario:.2f}
Ingreso total: {ingreso_tot:.2f}
""")
