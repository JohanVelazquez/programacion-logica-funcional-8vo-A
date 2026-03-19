from os import system
if system ("clear") !=0: system("cls")

print("Conversión de tipos")

#convertir una cadena que contiene un numero a un entero y sumarlo con otro entero
print(2 + int("100")) #convierte "100" a entero y suma 2. Resultado: 102

#Convertir u entero a cadena para concatenarlo con otra cadena
print("100" + str(2)) #Convierte el numero 2 a cadena y lo concatena. resultado: "1002"

#Convertir una cadena con un numero decimal a tipo float
print(type (float("3.1416"))) #Convierte "3.1416" a float y muestra su tipo. Resultado <class

#Convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416)) #Convierte 3.1416 a 3 eliminando la parte decimal, resultado: 3

#Evaluar valores numericos como booleanos
print(bool(3)) #cualquier numero distinto a 0 es true
print(bool(0)) #0 es false
print(bool(-1)) #numero negativos tambien son true

#Evaluar cadenas como booleanos
print(bool("")) #Una cadena vacia es false
print(bool(" ")) #una cadena con espacios es true
print(bool("False")) #una cadena con texto, aunque sea "false", es true

#Redondear un numero decimal
print(round(2.51)) #Redondea 2.51 al entero mas cercano. Resultado 3