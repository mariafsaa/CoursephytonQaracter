# Análisis y clasificación de clientes

# Pedir datos al usuario
n_client = input("Ingresa el nombre del cliente: ")
edad = int(input("Ingresa la edad: "))
gasto_mes = float(input("Ingresa el gasto mensual: "))

# Determinar si es adulto o menor
if edad >= 18:
    tipo_edad = "Adulto"
else:
    tipo_edad = "Menor"

# Clasificar al cliente según su gasto
if gasto_mes >= 1000:
    categoria = "Premium ⭐⭐"
elif gasto_mes >= 500 and gasto_mes < 1000:
    categoria = "Standard 👍"
else:
    categoria = "Basic 😉"

# Mostrar reporte final
print(f"""
--- Reporte del Cliente ---
Cliente: {n_client}
Edad: {edad} ({tipo_edad})
Gasto mensual: {gasto_mes:.1f}

Categoría: {categoria}
""")
