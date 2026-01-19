# CONSTANTES
ADULT_EDAD = 18
INGRESO_ACCESO_TOTAL = 2000
MAX_INTENT_FALLIDOS_TOTAL = 3
MAX_INTENT_FALLIDOS_LIMITADO = 1


def evaluar_acceso(edad: int, ingreso: float, fallidos: int) -> str:
    if edad < ADULT_EDAD:
        return "Sin Acceso 🚫"

    if ingreso >= INGRESO_ACCESO_TOTAL:
        if fallidos <= MAX_INTENT_FALLIDOS_TOTAL:
            return "Acceso Total ⭐⭐"
        return "Acceso Restringido 🤨🤨"

    # ingreso < 2000
    if fallidos <= MAX_INTENT_FALLIDOS_LIMITADO:
        return "Acceso Limitado ✅"
    return "Sin Acceso 🚫"


# Pedir datos al usuario
user_id = input("Ingresa tu ID de usuario: ").strip()
edad = int(input("Ingresa tu edad: "))
ing_mensual = float(input("Ingresa tu ingreso mensual: "))
ing_fallidos = int(input("Ingresa el número de intentos fallidos de acceso: "))

# Evaluar
acceso = evaluar_acceso(edad, ing_mensual, ing_fallidos)

# Salidas
print(f"""
--- Resumen de Acceso ➡️ ---
ID de Usuario: {user_id}
Edad: {edad}
Ingreso Mensual: ${ing_mensual:.2f}
Intentos Fallidos: {ing_fallidos}
Resultado: {acceso}
""")
