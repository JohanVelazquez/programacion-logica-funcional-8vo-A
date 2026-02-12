#calcular el area de un circulo (math.pi y math.pow)
import math

def area_circulo(radio):
    return math.pi * math.pow(radio, 2)

r = float(input("Ingresa el radio del círculo: "))
resultado = area_circulo(r)
print("El área del círculo es:", resultado)

