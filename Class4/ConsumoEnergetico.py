import numpy as np

# Matriz de consumo energético (kWh)
# Filas = apartamentos
# Columnas = intervalos de medición (1 a 24)

consumo = np.array([
    [0.8, 0.7, 0.7, 0.6, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 0.9, 0.8,
     0.8, 0.9, 1.0, 1.0, 0.9, 0.8, 0.8, 0.7, 0.7, 0.7, 0.7, 0.6],

    [0.6, 0.5, 0.5, 0.5, 0.5, 0.6, 0.8, 1.2, 3.5, 3.8, 3.6, 1.5,
     1.0, 1.1, 1.2, 1.3, 3.9, 4.2, 4.0, 1.5, 1.0, 0.8, 0.7, 0.6],

    [1.8, 1.7, 1.7, 1.6, 1.6, 1.7, 1.9, 2.1, 2.3, 2.4, 2.3, 2.2,
     2.2, 2.3, 2.4, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.9, 1.8, 1.7],

    [0.4, 0.4, 0.3, 0.3, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7, 0.6, 0.5,
     0.5, 0.6, 0.7, 0.7, 0.6, 0.5, 0.5, 0.4, 0.4, 0.4, 0.4, 0.3],

    [0.7, 0.6, 0.6, 0.6, 0.6, 0.7, 1.0, 1.4, 1.8, 1.2, 1.0, 0.9,
     0.8, 1.0, 1.6, 2.0, 1.7, 1.3, 1.1, 0.9, 0.8, 0.7, 0.7, 0.6]
])

number_of_apartments = np.array([
    "Apt 201",
    "Apt 202",
    "Apt 203",
    "Apt 204",
    "Apt 205"
])

# 1. Consumo promedio diario por apartamento
mean_consumo_apartamento = np.mean(consumo, axis=1)

print("1. Average daily energy consumption per apartment:")
for apartment, mean_consumo in zip(number_of_apartments, mean_consumo_apartamento):
    print(f"   {apartment}: {mean_consumo:.1f} kWh")

# Identificar qué apartamentos consumen significativamente más que el resto
overall_mean_consumo = np.mean(consumo)

print(f"\nOverall average daily consumption: {overall_mean_consumo:.1f} kWh")

condition = mean_consumo_apartamento > overall_mean_consumo

for apartment, mean_consumo, high in zip(
        number_of_apartments,
        mean_consumo_apartamento,
        condition
    ):
    if high:
        print(
            f"   {apartment} consumes significantly more than average: "
            f"{mean_consumo:.1f} kWh"
        )

# 2. Identificación de horas pico de consumo
peak_hours = consumo.sum(axis=0)
top = 3

idx_top_hours = np.argsort(peak_hours)[-top:][::-1]

print(f"\n2. Top {top} peak consumption intervals:")

for idx in idx_top_hours:
    print(
        f"\n   Interval {idx + 1}: "
        f"Total Consumption = {peak_hours[idx]:.1f} kWh"
    )

    # Consumo de cada apartamento en ese intervalo
    consumo_intervalo = consumo[:, idx]

    # Mostrar consumo por apartamento
    for apt, value in zip(number_of_apartments, consumo_intervalo):
        print(f"      {apt}: {value:.1f} kWh")

    promedio_intervalo = np.mean(consumo_intervalo)

    # Contar cuántos apartamentos tienen consumo alto
    contador_altos = 0
    for value in consumo_intervalo:
        if value > promedio_intervalo:
            contador_altos += 1

    total_apartamentos = len(consumo_intervalo)

    print("\n      Conclusion:")
    print(
        f"      There are {contador_altos} apartments with high consumption "
        f"out of {total_apartamentos}."
    )

    if contador_altos >= total_apartamentos / 2:
        print("      Many apartments with normal consumption")
    else:
        print("      Few apartments with extremely high consumption")
        
    # Comparar estabilidad del consumo
    # Analizar qué apartamentos presentan consumo regular
# Comparar estabilidad del consumo
std_consumo = np.std(consumo, axis=1)
std_promedio = np.mean(std_consumo)

print("\n3. Consumption stability analysis:")

for apt, std_value in zip(number_of_apartments, std_consumo):
    if std_value <= std_promedio:
        label = "Regular / Stable consumption"
        explanation = "Low variation over time"
    else:
        label = "Irregular / Variable consumption"
        explanation = "High variation over time"

    print(f"\n   Apartment: {apt}")
    print(f"   Standard deviation: {std_value:.2f} kWh")
    print(f"   Pattern: {label}")
    print(f"   Reason: {explanation}")
    
# Crear perfiles de consumo normalizados
# Normalizar el consumo promedio
min_consumo = mean_consumo_apartamento.min()
max_consumo = mean_consumo_apartamento.max()
mean_norm = (mean_consumo_apartamento - min_consumo) / (max_consumo - min_consumo)
print("\n4. Normalized average consumption profile:")

for apt, original, normalized in zip( number_of_apartments,mean_consumo_apartamento, mean_norm
    ):
    print(
        f"\n   Apartment: {apt}"
        f"\n   Original average consumption: {original:.2f} kWh"
        f"\n   Normalized consumption level: {normalized:.2f}"
    )

