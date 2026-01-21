#Collections Phyton Course, puede guardar datos de diferentes tipos
#listas, tuplas, diccionarios y conjuntos (sets)
mi_lista = [10, 20, "hola", 3.14, True]
print(mi_lista)
#Acceder a elementos de la lista CON .append() agrega elementos al final de la lista
mi_lista.append("818")
print(mi_lista)
#Eliminar elementos de la lista CON .remove()   elimina el primer elemento que coincida con el valor dado
mi_lista.remove(20)
print(mi_lista)

#Tuplas: similares a las listas pero inmutables (no se pueden modificar)
mi_tupla = (1, 2, 3, "adios", 4.5)
print(mi_tupla)
#Acceder a elementos de la tupla
print(mi_tupla[3])

#Sets : colecciones no ordenadas de elementos únicos, elimina duplicados automaticamente
mi_set = {1, 2, 2, 3, 4, 4, 5}
print(mi_set)
#Agregar elementos al set CON .add()
mi_set.add(6)
print(mi_set)

#Diccionarios: colecciones de pares clave-valor
mi_diccionario = {
    "nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario)
#Acceder a valores mediante claves      
print(mi_diccionario["ciudad"])
#Agregar un nuevo par clave-valor           
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)

#Colecciones: es un modulo que tiene estructuras listas para usar
from collections import Counter
#Counter: cuenta la frecuencia de elementos en una lista o iterable
frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
conteo = Counter(frutas)

print(conteo)              # Counter({'manzana': 3, 'pera': 2, 'uva': 1})
print(conteo["manzana"])   # 3
print(conteo.most_common(1))  # [('manzana', 3)]

#---------------------------------------------------------
# Metodos de strings
mi_cadena = " Hola Mundo "    
print(mi_cadena.lower())      # hola mundo
print(mi_cadena.upper())      # HOLA MUNDO  
print(mi_cadena.strip())      # Hola Mundo quita espacio al inicio y al final
print(mi_cadena.replace("Mundo", "Python"))  # Hola Python
texto = "2026-01-21."
print(texto.replace("-", "/"))  # 2026/01/21.
texto2 = "h o l a   m u n d o"
sin_espacios = texto2.replace(" ", "")
print(sin_espacios)

#Cuenta cuántas veces aparece un carácter o palabra dentro de un texto."
texto3 = "Hola mundo, hola Python"
print(texto3.count("hola"))

#verifica si una palabra empieza con algo o termina con algo, devuelve True o False
print(texto3.startswith("Hola"))  # True
print(texto3.endswith("Python"))  # True

# Metodo de division o separacion de strings
frase = "Aprendiendo Python es divertido"
palabras = frase.split(" ")  # Divide la frase en palabras usando el espacio como separador, el resultados es  una lista
print(palabras)  # ['Aprendiendo', 'Python', 'es', -...

texto4 = "   manzana, pera, uva,  banano   "
frutas = texto4.strip().split(",")
frutas_limpias = []
for fruta in frutas:
    frutas_limpias.append(fruta.strip())

print(frutas_limpias)


# Condiciones con strings
user = "admin"
if user.lower() == "admin":
    print("Welcome, administrator!")
    
print ("Validar una entrada")
entrada = input("Escribe si o no: ")
entrada_limpia = entrada.strip().lower()
if entrada_limpia == "si":
    print("Elegiste SI")
elif entrada_limpia == "no":
    print("Elegiste NO")
else:
    print("Opción no válida")
