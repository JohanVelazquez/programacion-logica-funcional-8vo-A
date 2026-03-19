# Calcular el factorial de un número (Recursividad)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Transformar una lista sin usar bucles (funciones Map + Lambda)
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))

print(f"Factorial de 5: {factorial(5)}")
print(f"Lista original: {numeros}")
print(f"Lista al cuadrado: {cuadrados}")
