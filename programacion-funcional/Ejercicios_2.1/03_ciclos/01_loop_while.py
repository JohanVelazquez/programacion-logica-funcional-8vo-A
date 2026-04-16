from os import system
if system("clear") != 0: system ("cls")

print ("\ Bucle While: ")

#bucle con una simple condición
contador=0

while contador <= 5:
    print(contador)
    contadorn += 1 #es super importante para evitar un bucle infinito

# Utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break #sale del grupo

    #continue que lo hace es saltar esa itereacion en concreto y continuar con el bicle
    print("\n #bucle con continue")
    contador = 0
    while contador < 10:
        contador += 1

        if contador % 2 == 0:
            continue

        print(contador)
    
# else, esta condicion cuando se ejecuta?
print ("\n Bucle while con else: ")
contador=0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")


# pedirle al usuario un numero que tiene que ser positivo si no, no lo dejamos en paz
numero = -1
while numero < 0:
    numero = int(input("Escribe un numero positivo: "))
    if numero < 0:
        print("El numero debe ser positivo. Intenta otra vez")

print(f"El numero que has introducido es {numero}")


numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
            print("El numero debe ser positivo. Intenta otra vez")
    except:
        print("Lo que introduces debe ser un numero!")

print(f"El numero que has introducido es {numero}")

###
# EJERCICIOS (while)