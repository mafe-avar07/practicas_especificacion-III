# PROBLEMA
# calcular el importe de renta de una bicicleta según el número de horas.
#
# ENTRADAS
# - horas : int, horas completas de renta, entero mayor o igual que 1.
#
# SALIDAS
# - importe : float, pesos mexicanos, mostrado con dos decimales.
#
# REGLAS Y SUPUESTOS
# - La tarifa es de $30 por hora.
# - Si horas >= 3, se aplica 15% de descuento sobre el importe base.
# - Se consideran horas completas; no se cobra una fracción porque el enunciado de prueba usa horas enteras.
# - El importe se muestra con dos decimales.
#
# ALGORITMO
# 1. Leer las horas completas de renta.
# 2. importe_base = horas * 30.
# 3. Si horas >= 3, importe = importe_base - importe_base * 0.15.
# 4. En caso contrario, importe = importe_base.
# 5. Mostrar horas e importe con dos decimales.
#
# CASOS DE PRUEBA
# 1 -> $30.00
# 2 -> $60.00
# 3 -> $76.50
# 4 -> $102.00
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerHoras() -> int : solicita y devuelve las horas de renta.
# calcularRenta(horas: int) -> float : calcula la renta y aplica el descuento.
# mostrarRenta(horas: int, importe: float) -> None : muestra horas e importe.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerHoras():
    return int(input("Ingrese las horas completas de renta: "))


def calcularRenta(horas):
    importe_base = horas * 30
    if horas >= 3:
        importe = importe_base - importe_base * 0.15
    else:
        importe = importe_base
    return importe


def mostrarRenta(horas, importe):
    print(f"Horas de renta: {horas}")
    print(f"Importe a pagar: ${importe:.2f}")
