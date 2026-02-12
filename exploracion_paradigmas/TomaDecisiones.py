#Realizar operaciones aritmeticas
def calcular_operacion(num1, num2, opcion):
    if opcion == 1:
        return num1 + num2
    elif opcion == 2:
        return num1 - num2
    elif opcion == 3:
        return num1 * num2
    elif opcion == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: división entre cero"
    else:
        return "Opción no válida"


print("Menú de operaciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Elige una opción: "))
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultado = calcular_operacion(num1, num2, opcion)
print("Resultado:", resultado)

