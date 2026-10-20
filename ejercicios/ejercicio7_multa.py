# PROBLEMA
# determinar la multa correspondiente a partir de la velocidad del vehículo en km/h.
#
# ENTRADAS
# - velocidad : float, km/h, mayor o igual que 0.
#
# SALIDAS
# - multa : float, pesos mexicanos, mostrado con dos decimales.
#
# REGLAS Y SUPUESTOS
# - El límite de velocidad es 60 km/h.
# - Si velocidad <= 60, la multa es $0.
# - Si 60 < velocidad <= 80, la multa es $500.
# - Si velocidad > 80, la multa es $1,000.
# - La multa se muestra con dos decimales.
#
# ALGORITMO
# 1. Leer la velocidad.
# 2. Si velocidad <= 60, multa = 0.
# 3. En caso contrario, si velocidad <= 80, multa = 500.
# 4. En caso contrario, multa = 1000.
# 5. Mostrar la velocidad y la multa con dos decimales.
#
# CASOS DE PRUEBA
# 50 -> $0.00
# 60 -> $0.00
# 61 -> $500.00
# 80 -> $500.00
# 81 -> $1000.00
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerVelocidad() -> float : solicita y devuelve la velocidad.
# calcularMulta(velocidad: float) -> float : determina la multa.
# mostrarMulta(velocidad: float, multa: float) -> None : muestra velocidad y multa.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerVelocidad():
    return float(input("Ingrese la velocidad del vehículo en km/h: "))


def calcularMulta(velocidad):
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000
    return multa


def mostrarMulta(velocidad, multa):
    print(f"Velocidad: {velocidad:.2f} km/h")
    print(f"Multa: ${multa:.2f}")
