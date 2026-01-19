import numpy as np
# Matriz
data = np.array([
    [80, 75, 90, 85, 70],
    [65, 88, 78, 72, 85],
    [90, 70, 85, 88, 60],
    [72, 82, 80, 75, 78]
])

#  Recorrer las columnas para calcular el promedio de cada atleta
# axis = 0 - columnas  ; axis = 1 : filas
print(data)
print(type(data))
print(data.shape)

#Rendimientos promedios de atletas
mean_athlete = np.mean(data, axis=1)
#Rendimientos promedios de cada metrica (Strength, Speed, Stamina, Durability, Agility)
mean_metric = np.mean(data, axis=0)

#Arrays de nombres de atletas
athlete_names = np.array([
    "Athleta A", "Athleta B", "Athleta C", "Athleta D"
])
#Arrays de nombres de métricas
metrics = ["Strength", "Speed", "Stamina", "Durability", "Agility"]

print("\n1. Average performance of each athlete:")
# ZIP : Toma dos o más iterables y los recorre en paralelo, emparejando sus elementos.
for name, mean in zip(athlete_names, mean_athlete):
    print(f"{name}  : Average performance: {mean:.2f}")

print("\n2. Average performance for each metric:")
for metric, mean in zip(metrics, mean_metric):
    print(f"{metric:<10} : Average: {mean:.1f}")

#----------------------------------------------------------
# Identificar al atleta con el mejor rendimiento promedio
print("\n3. Maximun and Minimun for each metric:")
max_values = np.max(data, axis=0)
min_values = np.min(data, axis=0)
for metric, max_v, min_v in zip(metrics, max_values, min_values):
    print(f"{metric:<10}   | Max: {max_v:>3} | Min: {min_v:>3}")
    
#----------------------------------------------------------
# Desviacion Standard for each athlete
# Dispersión de los rendimientos en cada métrica
std_dev_athlete = np.std(data, axis=1)
std_per_athlete = np.std(data, axis=1)
print("\n4. Consistency (Standard Deviation) of each athlete:")
for name, std in zip(athlete_names, std_per_athlete):
    print(f"{name:<10} : Consistency (std): {std:.1f}")
    
# Normalizar los datos (Min-Max Scaling) entre 0 y 1
# Formula: (x - min) / (max - min)
min_vals_metrics = np.min(data, axis=0)
max_vals_metrics = np.max(data, axis=0)
normalized_data = (data - min_vals_metrics) / (max_vals_metrics - min_vals_metrics)
print("\n5. Normalized Data (Min-Max Scaling):")
print(np.round(normalized_data, 1))

#----------------------------------------------------------
# Dar calificaciones por metrica
scores =np.array([0.20,0.30,0.25,0.15,0.10])  # Weights for each metric
# dot :  es la multiplicacion punto por punto, multiplica filas por columnas de los datos normalizados por los scores
final_scores = np.dot(normalized_data, scores)
print("\n6. Final Scores for each athlete: (out 1-10)")
for name, score in zip(athlete_names, final_scores):
    print(f"{name:<10} : Final Score: {score*10:.2f}")
    
# Obtener los indices de ordenamiento organizandolos de menor a mayor 
ranking_indices = np.argsort(final_scores)[::-1]  # [::-1] para orden de mayor a menor
ranking_indices = np.argsort(final_scores)[::-1]  # de mayor a menor

print("\n7. Ranking of Athletes:")

rank = 1
for index in ranking_indices:
    print(
        f"Rank {rank}: {athlete_names[index]} "
        f"with Final Score: {final_scores[index] * 10:.1f}"
    )
    rank += 1

#-----------------------------------------------------------
# Revisar que atleta tiene mejor rendimiento en cada metrica
contador = 0

print("\n 8. Athlete Strengths and Weaknesses")

for name in athlete_names:
    strongest_idx = np.argmax(data[contador])
    weakest_idx = np.argmin(data[contador])

    strongest = metrics[strongest_idx]
    weakest = metrics[weakest_idx]

    print(f"{name}")
    print(f"  Strongest metric: {strongest}")
    print(f"  Weakest metric:  {weakest}")
    contador += 1
#-----------------------------------------------------------
# Desviacion standars for earch athlete
stds =np.std(data, axis=1)
# Obtener el indice del atleta con menor desviacion standard
idx_best =np.argmin(stds)
idx_worst = np.argmax(stds)
print(f"""
9. Most Consistent and Least Consistent Athletes:
  Most Consistent: {athlete_names[idx_best]}
  Least Consistent: {athlete_names[idx_worst]}
""")