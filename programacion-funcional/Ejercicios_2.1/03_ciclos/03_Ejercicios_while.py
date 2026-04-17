###
#EJERCICIOS WHILE
##

# Ejercicio 1: Cuenta atrás
print("\n Ejercicio 1: Cuenta atras")
contador = 10
while contador > 0:
    print(contador)
    contador -= 1

# Ejercicio 2: Suma de números pares (1–20)
print("\nEjercicio 2: Suma de números pares")
numero = 2
suma = 0
while numero <= 20:
    suma += numero
    numero += 2
print("La suma de los pares entre 1 y 20 es:", suma)

# Ejercicio 3: Factorial de un número
print("\nEjercicio 3: Factorial de un número")
n = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1
while contador <= n:
    factorial *= contador
    contador += 1
print(f"El factorial de {n} es {factorial}")

# Ejercicio 4: Validación de contraseña
print("\nEjercicio 4: Validación de contraseña")
contraseña = input("Introduce una contraseña: ")
while len(contraseña) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    contraseña = input("Introduce una contraseña: ")
print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
print("\nEjercicio 5: Tabla de multiplicar")
n = int(input("Introduce un número: "))
contador = 1
while contador <= 10:
    print(f"{n} x {contador} = {n * contador}")
    contador += 1

# Ejercicio 6: Números primos hasta N
print("\nEjercicio 6: Números primos hasta N")
N = int(input("Introduce un número entero positivo: "))
num = 2
while num <= N:
    es_primo = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(num)
    num += 1
