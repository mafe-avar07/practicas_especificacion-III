# PROBLEMA
# calcular el importe mensual de electricidad a partir del consumo en kWh.
#
# ENTRADAS
# - consumo : float, kWh, mayor o igual que 0.
#
# SALIDAS
# - pago : float, pesos mexicanos, mostrado con dos decimales.
#
# REGLAS Y SUPUESTOS
# - Se usa tarifa progresiva por tramos: primeros 150 kWh a $1.00/kWh;
#   de 150 a 280 kWh, los siguientes kWh a $1.50/kWh; por encima de 280 kWh,
#   los kWh excedentes a $3.00/kWh.
# - Esta interpretación debe confirmarse con el docente, porque el enunciado
#   también podría interpretarse como una tarifa única según el consumo total.
# - El pago se muestra con dos decimales; no se redondean los tramos antes de sumar.
#
# ALGORITMO
# 1. Leer el consumo.
# 2. Si consumo <= 150, pago = consumo * 1.00.
# 3. Si 150 < consumo <= 280, pago = 150 * 1.00 + (consumo - 150) * 1.50.
# 4. Si consumo > 280, pago = 150 * 1.00 + 130 * 1.50 + (consumo - 280) * 3.00.
# 5. Mostrar el consumo y el pago con dos decimales.
#
# CASOS DE PRUEBA
# 100 -> $100.00
# 150 -> $150.00
# 200 -> $225.00
# 280 -> $345.00
# 300 -> $405.00
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerConsumo() -> float : solicita y devuelve el consumo mensual en kWh.
# calcularPago(consumo: float) -> float : calcula el pago por tramos.
# mostrarRecibo(consumo: float, pago: float) -> None : muestra consumo y pago.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerConsumo():
    return float(input("Ingrese el consumo mensual en kWh: "))


def calcularPago(consumo):
    if consumo <= 150:
        pago = consumo * 1.00
    elif consumo <= 280:
        pago = 150 * 1.00 + (consumo - 150) * 1.50
    else:
        pago = 150 * 1.00 + 130 * 1.50 + (consumo - 280) * 3.00
    return pago


def mostrarRecibo(consumo, pago):
    print(f"Consumo: {consumo:.2f} kWh")
    print(f"Importe del recibo: ${pago:.2f}")
