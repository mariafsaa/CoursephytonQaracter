# Auditoría simplificada de registros de pedidos de e-commerce.
# Crear lista con mínimo 14 registros crudos (buenos y malos) + imprimir cantidad.

registers = [
    " order_0001; user0159@hotmail.com ; 250,75 ; completed ",
    "order_0002 ; user0125@gmail.com ; 120,50 ; pending",
    "order_0003; user0125gmail.com ; 120,50 ; pending  ",
    "order_0004; USER0125@gmail.com ; 120,50 ; pending",
    "order_0005 ; user0125@gmail.com ; -120,50 ; shipped   ",
    "order_0006; user0125@gmail.com ; 520,50 ; completed",
    "order_0007; user0125@gmail.com ; 0 ; pending",
    "order_008; user9999@gmail.com ; 349,99 ; completed  ",
    "order_999; user8888@gmail.com ; 449,99 ; completed  ",
    "order_777; user7777@gmail.com ; €349.99 ; completed",
    "order_666; user6666@gmail.com ; 349,99 COP ;  Completed",
    "order_555; user5555@gmail.com ; 349.99",
    "order_444; user4444@gmail.com ; COP abc ; shipped",
    "order_333 user3333@gmail.com ; 349.99 ; completed",
    "order_1010; user1010@gmail.com ; 200,00 ; shipped"
]

print(f"The total raw registers: {len(registers)}")

# =========================
# Objective 2 — Cleaning records
# =========================
# No usar try / except

def clean_record(record):
    cleaned = record.strip().lower()

    cleaned = cleaned.replace("€", "")
    cleaned = cleaned.replace("$", "")
    cleaned = cleaned.replace("usd", "")
    cleaned = cleaned.replace("cop", "")

    cleaned = cleaned.replace(",", ".")
    cleaned = cleaned.replace(" ;", ";")
    cleaned = cleaned.replace("; ", ";")

    return cleaned

cleaned_orders = []
for record in registers:
    cleaned_orders.append(clean_record(record))

print("First three cleaned records:")
for i in range(3):
    print(f"Record {i+1}: {cleaned_orders[i]}")

# =========================
# Objective 3 — Validation and separation
# =========================
# Tomar los registros ya limpios (cleaned_orders) y Validar cada registro
# - Separar los datos válidos e inválidos
# - Guardar los datos válidos en listas separadas
# Not try / except

VALID_STATUSES = ["completed", "pending", "shipped"]
MIN_VALID_AMOUNT = 0

order_ids = []
emails = []
amounts = []
status_amounts = []   # aquí guardo los status válidos (completed/pending/shipped)

invalid_registers = []

for record in cleaned_orders:

    # Regla 1: el registro debe tener exactamente 4 campos
    fields = record.split(";")
    if len(fields) != 4:
        invalid_registers.append(record)
        continue

    order_id = fields[0]
    email = fields[1]
    amount_str = fields[2]
    status_value = fields[3]

    # Regla 2: el order_id debe comenzar por "order_"
    if order_id.startswith("order_") == False:
        invalid_registers.append(record)
        continue

    # Regla 3: el email debe contener "@"
    if email.count("@") == 0:
        invalid_registers.append(record)
        continue

    # Regla 4: el estado debe ser válido
    if (status_value in VALID_STATUSES) == False:
        invalid_registers.append(record)
        continue

    # Regla 5: el monto debe ser numérico (sin letras ni símbolos)
    if amount_str.replace(".", "", 1).isdigit() == False:
        invalid_registers.append(record)
        continue

    # Regla 6: el monto no puede tener más de un punto decimal
    if amount_str.count(".") > 1:
        invalid_registers.append(record)
        continue

    # Regla 7: el monto no puede estar vacío
    if amount_str == "":
        invalid_registers.append(record)
        continue

    amount = float(amount_str)

    # Regla 8: el monto debe ser mayor o igual al mínimo permitido
    if amount < MIN_VALID_AMOUNT:
        invalid_registers.append(record)
        continue

    # Si pasa todas las reglas, el registro es válido
    order_ids.append(order_id)
    emails.append(email)
    amounts.append(amount)
    status_amounts.append(status_value)

print(f"""
Results:
-------------------------
Number of valid registers: {len(order_ids)}
Number of invalid registers: {len(invalid_registers)}
""")

# =========================
# Objective 4 — Filter completed orders (10 points)
# =========================
# 1) Create a list with amounts of completed orders
# 2) Print how many completed orders exist

completed_orders = []
completed_indexes = []

for i in range(len(status_amounts)):
    if status_amounts[i] == "completed":
        completed_orders.append(amounts[i])
        completed_indexes.append(i)

print(f"The Numbers Of Completed Orders: {len(completed_orders)}")

# =========================
# Objective 5 — Total and average calculation (12 points)
# =========================
# Create reusable functions to calculate:
# - total
# - average
# If a list is empty, return 0.

# 1) Define a function to calculate a total
def calculate_total(values):
    total = 0
    for v in values:
        total = total + v
    return total

# 2) Define a function to calculate an average
def calculate_average(values):
    if len(values) == 0:
        return 0
    total = calculate_total(values)
    average = total / len(values)
    return average

# 3) Calculate and print total and average of completed orders
completed_total = calculate_total(completed_orders)
completed_average = calculate_average(completed_orders)
print(f"""Completed Orders Summary:
-------------------------
Total Amount: {completed_total:.1f}
Average Amount: {completed_average:.1f}
""")

# =========================
# Objective 6 — Highest completed order (10 points)
# =========================
# Find the completed order with the highest amount.


highest_text = "No completed orders exist."

# 1) Check if completed orders exist
if len(completed_orders) == 0:
    print("No completed orders exist.")
else:
    # 2) Supones que el primer pedido completado es el más alto para luego analizar y comparar
    high_amount = completed_orders[0]
    high_index = 0

    # 3) Recorremos todo el range del array para comparar cada uno
    for i in range(len(completed_orders)):
        if completed_orders[i] > high_amount:
            high_amount = completed_orders[i]
            high_index = i  # guardo el índice del más alto (en completed_orders)

    # 4) Busco el índice real en las listas válidas usando completed_indexes
    real_index = completed_indexes[high_index]

    # 5) Busco el order_id y email usando el índice real
    highest_order_id = order_ids[real_index]
    highest_email = emails[real_index]

    highest_text = f"Order ID: {highest_order_id}\nEmail: {highest_email}\nAmount: {high_amount:.2f}"

    print(f"""Highest Completed Order:
-------------------------
Order ID: {highest_order_id}
Email: {highest_email}
Amount: {high_amount:.2f}
""")

# =========================
# Objective 7 — Email domain analysis (8 points)
# =========================
# cuantos son gmail y cuantos no

gmail_count = 0
non_gmail_count = 0

for email in emails:
    if email.endswith("@gmail.com"):
        gmail_count = gmail_count + 1
    else:
        non_gmail_count = non_gmail_count + 1

print(f"""
Number Of Valid Emails
--------------------------------
Gmails : {gmail_count}
Others : {non_gmail_count}
""")

# =========================
# Objective 8 — Suspicious orders (12 points)
# =========================
# Mark orders as suspicious if:
# - amount >= HIGH_VALUE_THRESHOLD and status is not completed
# - status is pending and amount is 0
# Store warning messages as strings.

HIGH_VALUE_THRESHOLD = 500

warnings = []

for i in range(len(order_ids)):

    # Regla 1: monto alto y no completed
    if amounts[i] >= HIGH_VALUE_THRESHOLD and status_amounts[i] != "completed":
        message = (
            "Order " + order_ids[i] +
            " is suspicious: high amount (" + str(amounts[i]) +
            ") and status is " + status_amounts[i]
        )
        warnings.append(message)

    # Regla 2: pending con monto 0
    if status_amounts[i] == "pending" and amounts[i] == 0:
        message = (
            "Order " + order_ids[i] +
            " is suspicious: pending status with zero amount"
        )
        warnings.append(message)

print(f"Suspicious orders found: {len(warnings)}")
print("Suspicious order details:")
for warning in warnings:
    print(warning)


# Objective 9 — Final report (10 points)

report = f"""
FINAL REPORT
-------------------------
1.Total raw records: {len(registers)}
2.Valid records: {len(order_ids)}
3.Invalid records: {len(invalid_registers)}

4.Completed orders total: {completed_total:.1f}
5.Completed orders average: {completed_average:.1f}

6.Highest completed order: {highest_text}

7.Gmail emails: {gmail_count}
8.Other emails: {non_gmail_count}

9.Suspicious orders: {len(warnings)}
"""

print(report)


# Objective 10 — User query by status (6 points)
# =========================


print(f"""
-------------------------------------------
Data entry program, what do you want to know?
""")

user_status = input("Write a status (completed, pending, shipped): ")
user_status = user_status.lower().strip()

if user_status in VALID_STATUSES:

    total_status_amount = 0

    for i in range(len(status_amounts)):
        if status_amounts[i] == user_status:
            total_status_amount = total_status_amount + amounts[i]

    print(f"Total amount for status '{user_status.capitalize()}': {total_status_amount:.1f}")

else:
    print("Invalid status entered.")
