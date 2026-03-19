#concatenar datos
def concatenar_datos(nombre, carrera, prom):
    resultado = (nombre + " es alumno de la carrera de " + carrera +
                 " y su promedio es de " + str(prom))
    return resultado

nombre = input("Ingresa tu nombre: ")
carrera = input("Ingresa tu carrera: ")
prom = float(input("Ingresa tu promedio: "))

mensaje = concatenar_datos(nombre, carrera, prom)
print(mensaje)

