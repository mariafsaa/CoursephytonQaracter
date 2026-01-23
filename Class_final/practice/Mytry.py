# Objetivo 1 — Datos en bruto (10 puntos)
# =========================
# Crear una lista con al menos 12 registros de ventas en bruto como strings.
# Incluir:
# - espacios extra
# - diferencias entre mayúsculas y minúsculas
# - precios con comas
# - categorías inválidas
# - precios negativos
# - campos faltantes

# Ejemplo:
# "  T-shirt , Clothes , 19,99 "
# Crear la lista de datos en bruto
data_records = [
    "  T-shirt , Clothes , 19,99 ",
    "  Jeans , clothes , 29,99 ",
    "  Hat , AccessorieS , 14,99 ",
    "  Shoes , Footwear , 59,99 ",
    "  Dress , clothes , 39,99 ",
    "  Gloves , Accessories , 12,99 ",
    "  Socks ,  Clothes , 5,99 ",
    " ScarF , Accessories , 8,99 ",
    " Watch , Electronics , 100,00   ",
    "   Laptop , Electronics , -1000,00 ", # Invalid price
    "   Book , Books , 45,00 ", # Valid
    "   Pen , Stationery, 0 ",
    "shirt, clothes, 15.99"  # Missing spaces and different case
]

# Imprimir cuántos registros en bruto existen
print(f"Total raw data records: {len(data_records)}\n")
# Crear una función que limpie UN registro:
# - eliminar espacios extra
# - convertir el texto a minúsculas
# - reemplazar la coma por punto en los precios

# TODO:|
# Definir la función de limpieza
def clean_record(record):
    record = record.strip().lower()   
    record = record.replace(",", ".")  
    return record
# Crear una nueva lista con los registros limpios
cleaned_records = [clean_record(record) for record in data_records]
# Imprimir los dos primeros registros limpios
print("First two cleaned records:")
for i in range(2):
    print(f"Record {i+1}: {cleaned_records[i].capitalize()}")


