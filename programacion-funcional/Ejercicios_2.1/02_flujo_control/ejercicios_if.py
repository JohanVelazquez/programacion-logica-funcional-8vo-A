from os import system
if system("clear") != 0: system("cls")
###
# EJERCICIOS
###

print("\nEjercicio 1: Determinar el mayor de dos números")
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    print(f"El numero mayor es {num1}")
elif num2 > num1:
    print(f"El numero mayor es {num2}")
else:
    print("Los dos numeros son iguales")

print("\nEjercicio 2: Calculadora simple")
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
a = float(input("\nIngresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación a realizar (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", a + b)
elif operacion == "-":
    print("Resultado:", a - b)
elif operacion == "*":
    print("Resultado:", a * b)
elif operacion == "/":
    if b != 0:
        print("El Resultado es:", a / b)
    else:
        print("Error: Hay una división entre cero")
else:
    print("La operación no es válida")

print("\nEjercicio 3: Año bisiesto")
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
anio = int(input("\nIngresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")

print("\nEjercicio 4: Categorizar edades")
# Pide al usuario que introduzca una edad y la clasifique en:
# – Bebé (0–2 años)
# – Niño (3–12 años)
# – Adolescente (13–17 años)
# – Adulto (18–64 años)
# – Adulto mayor (65 años o más)

edad = int(input("Ingresa una edad: "))

if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad >= 3 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("La edad no es válida")