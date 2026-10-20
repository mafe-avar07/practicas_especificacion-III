# PROBLEMA
# calcular el precio de un boleto de cine según la edad del cliente.
#
# ENTRADAS
# - edad : int, años cumplidos, entero mayor o igual que 0.
#
# SALIDAS
# - precio : float, pesos mexicanos, mostrado con dos decimales.
#
# REGLAS Y SUPUESTOS
# - El precio general es $80.
# - Edad <= 12 o edad >= 60: precio = $40.
# - En cualquier otra edad, precio = $80.
# - El precio se muestra con dos decimales.
#
# ALGORITMO
# 1. Leer la edad.
# 2. Si edad <= 12 o edad >= 60, precio = 40.
# 3. En caso contrario, precio = 80.
# 4. Mostrar edad y precio con dos decimales.
#
# CASOS DE PRUEBA
# 8 -> $40.00
# 12 -> $40.00
# 13 -> $80.00
# 59 -> $80.00
# 60 -> $40.00
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerEdad() -> int : solicita y devuelve la edad.
# calcularPrecio(edad: int) -> float : determina el precio del boleto.
# mostrarPrecio(edad: int, precio: float) -> None : muestra edad y precio.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerEdad():
    return int(input("Ingrese la edad del cliente: "))


def calcularPrecio(edad):
    if edad <= 12 or edad >= 60:
        precio = 40
    else:
        precio = 80
    return precio


def mostrarPrecio(edad, precio):
    print(f"Edad: {edad} años")
    print(f"Precio del boleto: ${precio:.2f}")
