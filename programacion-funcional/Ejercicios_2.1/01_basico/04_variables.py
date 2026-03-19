from os import system
if system ("clear") !=0: system("cls")

#Para asignar una variable solo hace falta poner el nombre de la variable y asignarlo
my_name = "Johan"
print(my_name) #imprime el valor de la variable my_name

age=22
print(age) #imprime el valor de la variable age

#Reasignar un nuevo valor a una variable existente
age=26
print(age) #ahora la variable age tiene el valor 26

name = "Johan"
print(type(nombre)) #Muestra el tipo de datos de la variable name (str)

name = 32
print(type(name)) #Ahora la variable tiene un numero entero (int)

#Tipado fuerte

#f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age + 5} años")

#No recomendad forma de asignar variables
name, age, city = "Johan", 22, "FCP"

#Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

miNombreDeVariable = "no-recomendado" #camelCase
MiNombreDeVariable = "no-recomendado" #Pascalcase
minombredevariable = "no-recomendado" #todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 #UPPER_CASE --> Constantes

is_user_logged_in: bool = True #indica que la variable es un booleano
print(is_user_logged_in)

name: str = Johan
print(name)