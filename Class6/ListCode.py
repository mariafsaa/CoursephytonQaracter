# Reglas
# "stop"  : break
# "error" : continue
# "rest"  : cuenta como día válido, suma 0
# cualquier otro texto : lo ignoramos (por seguridad)

data = ["rest", 45, 0, "error", 60, -10, 90, "stop", 30]

total_minutes = 0
valid_days = 0
intense_days = 0

# Recorrer la lista de data
for idx in data:

    # Caso 1: es texto (str)
    if type(idx) == str:

        if idx == "stop":
            print("Data processing stopped")
            break

        elif idx == "error":
            print("Invalid data encountered, skipping entry.")
            continue

        elif idx == "rest":
            print("Rest day, valid day with 0 minutes.")
            valid_days += 1
            # suma 0, así que no tocamos total_minutes
            continue

        else:
            print(f"Unknown message '{idx}' ignored.")
            continue

    # Caso 2: es número (int o float)
    elif type(idx) == int or type(idx) == float:

        # validar el dato numérico
        # number < 0 : inválido
        if idx < 0:
            print(f"Negative value {idx} is invalid, skipping entry.")
            continue

        # Clasificar primero (como tú lo entiendes)
        # number > 60 : entrenamiento intenso
        # number = 0  : día válido sin ejercicio
        if idx > 60:
            intense_days += 1
            print(f"Intense workout recorded: {idx} minutes.")
        elif idx == 0:
            print("Zero minutes recorded, valid day with 0 minutes.")
        else:
            print(f"Workout mid recorded: {idx} minutes.")

        # al ser valido cuenta el día y suma minutos (0 suma 0)
        valid_days += 1
        total_minutes += idx

    # otro tipo de dato raro
    else:
        print(f"Unknown data type '{type(idx)}' ignored.")

# Calcular el promedio (evitar división por cero)
if valid_days > 0:
    average_minutes = total_minutes / valid_days
else:
    average_minutes = 0

# Resultados finales
print(
    "\n--- Summary ---"
    f"\nTotal valid days: {valid_days}"
    f"\nTotal exercise minutes: {total_minutes}"
    f"\nNumber of intense workout days: {intense_days}"
    f"\nAverage minutes per day: {average_minutes}"
)
