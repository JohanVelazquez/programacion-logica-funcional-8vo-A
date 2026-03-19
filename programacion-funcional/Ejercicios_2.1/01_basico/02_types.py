from os import system

if system ("clear") !=0: system("cls")

"""
El comando `type()` devuelve el tipo de un objeto en python
"""

print("int:")   #Enteros
print(type(10)) #Número entero positivo
print(type(0))  #El numero cero tambien es entero
print(type(-5)) #Número entero negativo
print(type(7238424723784278934789239874)) #python permite enteros de gran tamaño

print("float:")  #numero decimales
print(type(3.14)) #numero con punto decimal
print(type(1.0))  #tambien es considerado un float aunque sea un numero entero con punto
print(type(1e3))  #notacion cientifica equivalente a 100.0

print("complex:")
print(type(1+2j))

print("str:") #Cadenas de texto
print(type("Hola")) #un string con texto
print(type("")) #un string vacio
print(type("123")) #aunque parezca un numero, esta entre comillas, por lo que es un string
print(type("""
multilinea
""")) #un string que abarca varias lineas usando triple comillas

print("Bool:") #valores booleanos
print(type(True)) #valor booleano verdadero
print(type(False)) #valor booleano falso
print(type(1 < 2)) #

print("NoneType:")
print(type(None))