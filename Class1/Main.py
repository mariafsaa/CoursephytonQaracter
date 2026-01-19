# Variables and Data Types

sales = 150          # int
price = 9.99         # float
customer_name = "Alice"  # string

# Integer examples
units_sold = 120
customers = 46


# Floating point (float)
price = 9.99
price = 19.95          # this overwrites the previous price
tax_rate = 0.21
average_score = 7.8

# String (str)
customer_name = "Alice"
product_name = "Laptop"
category = "Electronics"
order_id = "ORD_1023"

# Boolean (bool)
is_active = True
has_discount = False
is_preliminar_customer = "ORD_1023"

# Type of a variable -> type(), conocer el tipo de variable
print(type(price))          # <class 'float'>
print(type(product_name))   # <class 'str'>
print(type(is_active))      # <class 'bool'>

# PEP 8 Style Guide, guía oficial de estilo de Python
#Letras: a-z, A-Z ; Números (no al inicio) ; Guion bajo _ (underscore)
# No permitido ; Espacios ; Caracteres especiales (@, #, %, etc.) ; Empezar con números

# Constantes Se escriben en MAYÚSCULAS
# Good variable names (snake_case)
units_sold = 120
unit_price = 9.99

# Constants (should not change)
TAX_RATE = 0.21
MAX_USER = 1000
PI = 3.14159

# Print values
print(units_sold)
print(unit_price)
print(TAX_RATE)
print(MAX_USER)
print(PI)
# Constant example
TAX_RATE = 0.21

price = 100
final_price = price + (price * TAX_RATE)
print(final_price)

# Reassigning variables
sales = 100
sales = sales + 50 
print(sales)  #salida 150


# Print values
print(sales)
print(price)
print(customer_name)
print(units_sold)
print(customers)
print(tax_rate)
print(average_score)
print(product_name)
print(category)
print(order_id)
print(is_active)
print(has_discount)


# -------------------------
# ARITHMETIC OPS
# +   Addition ;  -   Subtraction ; # *   Multiplication ; # /   Division ; #
# //  Integer division ; # %   Modulus (remainder) ; # **  Power

# Division vs Integer Division
# / → mantiene los decimales
# // → quita los decimales (redondea hacia abajo)
a, b = 5, 2
normal_division = a / b      # division
integer_division = a // b    # integer division
print(normal_division)   # 2.5
print(integer_division)  # 2

 # ---------- Comparison
a, b = 10, 3
# Verifica si a es igual a b
print(a == b)   # False
# Verifica si a es diferente de b
print(a != b)   # True
# Verifica si a es mayor que b
print(a > b)    # True
# Verifica si a es menor que b
print(a < b)    # False
# Verifica si a es mayor o igual que b
print(a >= b)   # True
# Verifica si a es menor o igual que b
print(a <= b)   # False


# LOGICAL OPS
# ============
# and  -> True if both are True ; or   -> True if one is True ;  not  -> Negates the value
c = 10
f = 5
print(c > 5 and f < 10)   # True
print(c < 5 or f < 10)    # True
print(not c > 5)          # False


# ASSIGNMENT OPERATORS
# = assign | += add | -= subtract | *= multiply
# /= divide | //= int divide | %= modulo | **= power
x = 10
x += 5    # x = x + 5
x -= 2    # x = x - 2
x *= 3    # x = x * 3
x /= 2    # x = x / 2

# TYPE CONVERSION
# int()   -> to integer ; float() -> to decimal ; str()   -> to string ; bool()  -> to boolean
# Ejemplo : Context: sales data
units_sold = "10"          # string
price = 9.5               # float
units_sold = int(units_sold)   # str -> int
total = units_sold * price
print(total)               # 95.0
print(str(total))          # float -> str
print(bool(units_sold))    # int -> bool (True)

## CONVERSIÓN A BOOLEAN (bool)
# False solo para: 0, "", None
# Todo lo demás es True
# Ejemplos: bool(0)->False | bool(4)->True | bool(-10)->True
#           bool("")->False | bool("data")->True
# Se usa en: validaciones, if, input del usuario

#MODULE INPUT
# INPUT EN PYTHON input() se usa para pedir información al usuario ; El mensaje dentro de input() explica qué debe escribir
# input() SIEMPRE devuelve un string (texto) ; Para hacer cálculos, el valor debe convertirse (int, float, etc.)
age = input("How old are u?: ")  # "27" -> string
print(type(age))
age = int(age)
print(type(age))
customer_amount = int(input("How many customers do u have?: "))
print(type(customer_amount))

#Concatenacion con , and f
name = "Ana"
age = 25
print("Hola", name, "tienes", age, "años", "Y tienes ", customer_amount, " costumers" )

product = "Laptop"
price = 1200.5
tax = 0.21

final_price = price + (price * tax)
print(f"Producto: {product}")
print(f"Precio base: {price:.2f}")
print(f"Precio final: {final_price:.2f}")

#f-string multilínea
customer = "Alice"
sales = 960.2

print(f"""
Hello, I'm {customer}.
Total sales: {sales}
""")

#CONDITIONAL OF CONTROL
# Ask the user for their age

age2 = int(input("How old are u?: "))
# Check if the user is an adult or a minor
if age2 >= 18:
    print("Adult")
else:
    print("Minor")
    
    
# LOOPS IN PYTHON
# FOR LOOP
#Para cada número i desde 0 hasta 4, imprime ese número
for i in range(5):
    print(i)
