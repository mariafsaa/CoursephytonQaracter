import pandas as pd
s = pd.Series([10, 15, 20, 25, 30], index=['a', 'b', 'c', 'd', 'e'])
print(s)
df = pd.read_csv("CoursephytonQaracter/Class5/temperaturas.csv")
print(df)
#Creamos una serie con la columna 'Temperatura'
temp_series = df['temperatura_c']

# Informavion Stadistica  de la serie
print("\nTemperature Series Overall Stats:")
print(temp_series.describe()) # count, mean, std, min, 25%, 50%, 75%, max

# Cantidad de datos en la serie
print(f"\n Total data points: {temp_series.count()}")

# Sacamos la media de la serie
temp_mean = temp_series.mean()
print(f"\nAverage temperature: {temp_mean:.2f} °C")
# Sacamos el valor máximo y mínimos de la serie
temp_max = temp_series.max()
temp_min = temp_series.min()
print(f""" \nTemperature Range:
- Max: {temp_max:.2f} °C   
- Min: {temp_min:.2f} °C""")