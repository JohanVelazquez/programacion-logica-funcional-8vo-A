from os import system
if system ("clear") !=0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("\nJohan Velázquez\n")
print("Felipe Carrillo Puerto\n")


print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
### Completa aquí
cadena = "12345"
entero = int(cadena)
flotante = float(entero)
print("Entero:", entero)
print("Float:", flotante)

print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

valor = 3.99
enterof = int(valor)
print(f"{enterof} se redondea el numero al convertirlo en entero")



print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# ¡Hola! Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros

## Completa aquí
# Definir variables
nombre = "Johan"
edad = 21
altura = 1.60

# Usar f-string para imprimir la presentación
print(f"¡Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")



print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# Desarrollo del ejercicio
pi = 3.14159        
pi_redondeado = round(pi)  
resultado = pi_redondeado // 2   

print("PI:", pi)
print("Redondeado:", pi_redondeado)
print("Resultado de la división entera:", resultado)
