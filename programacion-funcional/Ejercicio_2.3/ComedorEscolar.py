# =============================================================================
#  ACTIVIDAD PRÁCTICA INTEGRADORA
#  Sistema de pedidos: Comedor Escolar
# =============================================================================
#  Programación Funcional en Python — Nivel Básico
#  Temas integrados:
#    ✅ Funciones simples y de primera clase  
#    ✅ Comprensión de listas                 
#    ✅ Funciones de orden superior           
#    ✅ Callbacks                             
#    ✅ Funciones lambda + map()              
#    ✅ Lógica condicional dentro de funcs.   
#    ✅ Entrada del usuario                   
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
#  Sección 1 — INVESTIGA
# ─────────────────────────────────────────────────────────────────────────────
# Antes de comenzar a codificar, investiga y responde en comentarios:
#
# 1. ¿Qué es una función de primera clase en Python?
# R: Es una función que puede tratarse como cualquier otro valor,
#    se puede guardar en variables, pasar como argumento
#    a otras funciones y devolver como resultado.

# 2. ¿Cuál es la diferencia entre una función de orden superior y un callback?
# R: Una función de orden superior recibe otra función
#    como argumento o devuelve una función. Un callback es la función
#    que se pasa como argumento para ser ejecutada dentro de otra función.

# 3. ¿Cuándo conviene usar comprensión de listas en lugar de un ciclo for?
# R: Conviene usar comprensión de listas cuando se quiere crear una lista
#    de forma más corta, clara y eficiente a partir de otra secuencia.

# 4. ¿Qué hace map() y cómo se relaciona con lambda?
# R: map lo que hace es aplicar una función a cada elemento de una lista.
#    Se relaciona con lambda porque permite usar funciones pequeñas
#    y anónimas sin necesidad de definirlas.

# 5. ¿Qué ventaja ofrece pasar una función como argumento a otra función?
# R: Permite reutilizar código, hacer programas más dinámicos,
#    y aplicar diferentes comportamientos sin modificar la función principal.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────
# Lee el siguiente escenario y diseña tu solución ANTES de codificar.
#
# ESCENARIO
# La cooperativa escolar ofrece tres productos en su menú:
#   🍕 Pizza  |  🥤 Agua fresca  |  🫔 Tamal
#
# El sistema debe:
#   A) Preparar cualquier producto usando una función dedicada por producto.
#   B) Tomar la orden de un grupo: recibir la FUNCIÓN del producto y la
#      CANTIDAD solicitada, y devolver una lista con todas las porciones.
#   C) Calcular el precio total aplicando el precio unitario a cada porción  
#      usando map() y una función lambda.
#   D) Aplicar una PROMOCIÓN: si el pedido es de 3 o más porciones,
#      agregar "🎁 postre gratis" a la orden.
#   E) Solicitar al usuario cuántas porciones desea de cada producto y
#      mostrar el resumen completo del pedido.
#
# Antes de codificar respone o describe:

# ¿Qué funciones necesitas definir?
# R:
# - preparar_pizza()
# - preparar_agua()
# - preparar_tamal()
# - calcular_promocion(cantidad)
# - tomar_orden(preparar_alimento, cantidad, precio_unitario)

# ¿Cuál de ellas es de orden superior? ¿Por qué?
# R:
# La función tomar_orden es de orden superior porque recibe otra función
# como argumento (preparar_alimento) y la ejecuta dentro de ella.

# ¿Dónde usarás comprensión de listas?
# R:
# Dentro de la función tomar_orden para generar la lista de porciones,
# repitiendo el resultado de preparar_alimento() según sea la cantidad.

# ¿Dónde usarás lambda + map()?
# R:
# Dentro de la función tomar_orden para crear una lista de precios,
# aplicando una función lambda que asigna el precio_unitario a cada porción.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Sección 3 — CODIFICA
# ─────────────────────────────────────────────────────────────────────────────
# Completa cada paso en el orden indicado.
# Puedes apoyarte en los archivos del carpeta para recordar la sintaxis.


# ── PASO 1 ──────────────────────────────────────────────────────────────────

def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"


# ── PASO 2 ──────────────────────────────────────────────────────────────────

def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    else:
        return ""


# ── PASO 3 ──────────────────────────────────────────────────────────────────

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    porciones = [preparar_alimento() for _ in range(cantidad)]
    precios = list(map(lambda x: precio_unitario, porciones))
    promocion = calcular_promocion(cantidad)
    # EXTRA: calcular total
    total = sum(map(lambda x: x, precios))
    return porciones, precios, promocion, total

def elegir_producto(nombre):
    if nombre == "pizza":
        return preparar_pizza
    elif nombre == "agua":
        return preparar_agua
    elif nombre == "tamal":
        return preparar_tamal
    else:
        return None


# ── PASO 4 ──────────────────────────────────────────────────────────────────

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

funcion_pizza = elegir_producto("pizza")
funcion_agua = elegir_producto("agua")
funcion_tamal = elegir_producto("tamal")

orden_pizza = tomar_orden(funcion_pizza, cantidad_pizzas, 25)
orden_agua = tomar_orden(funcion_agua, cantidad_aguas, 10)
orden_tamal = tomar_orden(funcion_tamal, cantidad_tamales, 15)


# ── PASO 5 ──────────────────────────────────────────────────────────────────

print("\n========== RESUMEN DEL PEDIDO ==========")
# Desempaqueta cada tupla en sus tres partes y muéstralas
porciones_pizza,  precios_pizza,  promo_pizza, total_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua,  total_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal, total_tamal  = orden_tamal

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")
print(f"💰 Total    → {total_pizza}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")
print(f"💰 Total    → {total_agua}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")
print(f"💰 Total    → {total_tamal}")

print("\n========================================")

# ─────────────────────────────────────────────────────────────────────────────
# Sección 4 — PRUEBA
# ─────────────────────────────────────────────────────────────────────────────
# Ejecuta el programa con los siguientes casos y verifica los resultados.
#
# CASO 1
# Pizzas: 2 | Aguas: 1 | Tamales: 2
# Resultado: ✅
# Ninguna orden muestra "🎁 postre gratis"
# El programa funciona correctamente en este caso.

# CASO 2
# Pizzas: 3 | Aguas: 5 | Tamales: 4
# Resultado: ✅
# Todas las órdenes muestran "🎁 postre gratis"
# La condición de promoción funciona correctamente.

# CASO 3
# Pizzas: 1 | Aguas: 3 | Tamales: 2
# Resultado: ✅
# Solo la orden de aguas muestra "🎁 postre gratis"
# La lógica condicional se aplica correctamente por producto.

# CASO 4
# Verificación de precios:
# 3 pizzas → [25, 25, 25]
# 4 tamales → [15, 15, 15, 15]
# Resultado: ✅
# map() + lambda funcionan correctamente.
#
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Desafío extra (opcional)
# ─────────────────────────────────────────────────────────────────────────────
# Si terminaste antes y quieres ir más allá:
#
# 1. Usa sum() y map() + lambda para calcular el TOTAL a pagar de cada orden.

# 2. Crea una función elegir_producto(nombre) que sea de ORDEN SUPERIOR:
#    recibe un string ("pizza", "agua" o "tamal") y DEVUELVE la función
#    de preparación correspondiente (sin ejecutarla).
#    Referencia: funciones.py → elegir_operacion()
    
# 3. Usa la función del punto 2 para reemplazar los argumentos directos en
#    las llamadas a tomar_orden().
