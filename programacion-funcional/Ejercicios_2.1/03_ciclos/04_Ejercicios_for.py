###
#EJERCICIOS FOR
###

print("\nEjercicio 1: Imprimir números pares ")
for numero in range(2, 21, 2):
    print(numero)

print("\nEjercicio 2: Calcular la media de una lista")
numeros = [10, 20, 30, 40, 50]
suma = 0
for n in numeros:
    suma += n
media = suma / len(numeros)
print("La media de la lista es:", media)

print("\n Ejercicio 3: Buscar el máximo de una lista")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for n in numeros:
    if n > maximo:
        maximo = n
print("El número máximo en la lista es:", maximo)

print("\n Ejercicio 4: Filtrar cadenas por longitud ")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
filtradas = [p for p in palabras if len(p) > 5]
print("Palabras con más de 5 letras:", filtradas)

print("\nEjercicio 5: Contar palabras que empiezan con una letra")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra = "c"  
contador = 0
for p in palabras:
    if p.lower().startswith(letra.lower()):
        contador += 1
print(f"Número de palabras que empiezan con '{letra}':", contador)
