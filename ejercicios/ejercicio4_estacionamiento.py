# PROBLEMA
# calcular el importe de estacionamiento a partir del tiempo de estancia en minutos.
#
# ENTRADAS
# - minutos : int, minutos de estancia, entero mayor o igual que 0.
#
# SALIDAS
# - cobro : float, pesos mexicanos, mostrado con dos decimales.
#
# REGLAS Y SUPUESTOS
# - Si la estancia es de 0 minutos, el cobro es $0.
# - De 1 a 60 minutos, se cobran $20 por la primera hora o fracción.
# - Después de los primeros 60 minutos, cada hora adicional o fracción cuesta $15.
# - El cobro máximo es $150.
# - Para calcular fracciones se utiliza aritmética entera; no se importa ninguna biblioteca.
#
# ALGORITMO
# 1. Leer los minutos de estancia.
# 2. Si minutos == 0, cobro = 0.
# 3. Si 0 < minutos <= 60, cobro = 20.
# 4. Si minutos > 60, calcular horas_adicionales = (minutos - 1) // 60.
# 5. En ese caso, cobro = 20 + horas_adicionales * 15.
# 6. Si cobro > 150, establecer cobro = 150.
# 7. Mostrar el cobro con dos decimales.
#
# CASOS DE PRUEBA
# 45 -> $20.00
# 60 -> $20.00
# 61 -> $35.00
# 150 -> $50.00
# 600 -> $150.00
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerMinutos() -> int : solicita y devuelve los minutos de estancia.
# calcularCobro(minutos: int) -> float : calcula el cobro aplicando fracciones y tope.
# mostrarCobro(minutos: int, cobro: float) -> None : muestra minutos y cobro.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerMinutos():
    return int(input("Ingrese el tiempo de estancia en minutos: "))


def calcularCobro(minutos):
    if minutos == 0:
        cobro = 0
    elif minutos <= 60:
        cobro = 20
    else:
        horas_adicionales = (minutos - 1) // 60
        cobro = 20 + horas_adicionales * 15
    if cobro > 150:
        cobro = 150
    return cobro


def mostrarCobro(minutos, cobro):
    print(f"Tiempo de estancia: {minutos} minutos")
    print(f"Importe a cobrar: ${cobro:.2f}")
