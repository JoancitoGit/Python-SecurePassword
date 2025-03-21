import string
import random

longitud = int(input(f'Ingrese el tamaño de la contraseña: '))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: " + contrasena)

# Adecuar para modificar las contrasaeñas a lo que requiera el usuario Ej. "Quieres que contenga puras mayusculas, minusculas, numeros?"