# Un sistema de monitoreo recibe datos mixtos de sensores desde un edificio inteligente
print("Monitoring System Data Analysis")
data = [22, "ok", 30, -5, 28, "maintenance", 35, "offline", 40]
data_cleaned = []

# Recorrer cada elemento de la lista
for item in data:
    # 1) Caso: es texto (str)
    if isinstance(item, str):
        if item == "offline":
            print("System is offline. Stopping data processing.")
            break
        else:
            # Es texto pero no es 'offline' -> se ignora
            print(f"Ignored message: {item}")
            continue

    # 2) Caso: es número (int o float)
    elif isinstance(item, (int, float)):
        if item < 0:
            # Número negativo -> inválido, se ignora
            print(f"Ignored invalid temperature: {item}")
            continue
        else:
            # Número positivo -> temperatura válida
            print(f"Valid temperature added: {item}")
            data_cleaned.append(item)

    # 3) Caso: otro tipo de dato raro (por si aparece)
    else:
        print(f"Unknown data type ignored: {item}")


print(f"\nCleaned Data: {data_cleaned}")

# --- Cálculos finales ---
# 1. Cantidad de temperaturas válidas
count_temp = len(data_cleaned)

# 2. Promedio de temperatura
average_temp = sum(data_cleaned) / count_temp

# 3. Cantidad de temperaturas por encima del promedio
above_average = 0
for temp in data_cleaned:
    if temp > average_temp:
        above_average += 1

# Resultados
print(f"""
Results:
-------------------------
Number of valid temperatures: {count_temp}
Average temperature: {average_temp:.2f} °C
Temperatures above average: {above_average}
""")

