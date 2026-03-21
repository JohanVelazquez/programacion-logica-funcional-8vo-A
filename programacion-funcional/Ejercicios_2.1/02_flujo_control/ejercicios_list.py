
###
# EJERCICIOS
###

print("\nEjercicio 1: El mensaje secreto")
# Dada la siguiente lista:
mensaje = ["C", "O", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
secret = mensaje[7:]   
print("".join(secret)) 

print("\nEjercicio 2: Intercambio de posiciones")
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

print("\nEjercicio 3: El sándwich de listas")
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

print("\nEjercicio 4: Duplicando la lista") 
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
duplicado = lista + lista
print(duplicado)  

print("\nEjercicio 5: Extrayendo el centro")
# Dada una lista con un número impar de elementos
lista = [10, 20, 30, 40, 50]
NumCentro = lista[len(lista)//2]  
print("El numero del centro es:", NumCentro)  

print("\nEjercicio 6: Reversa parcial")
# Dada una lista, invierte solo la primera mitad
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista)//2
resultado = lista[:mitad][::-1] + lista[mitad:]
print(resultado)  