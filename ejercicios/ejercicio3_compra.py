# PROBLEMA
# calcular el subtotal, descuento, IVA y total de una compra.
#
# ENTRADAS
# - subtotal : float, pesos mexicanos, mayor o igual que 0.
#
# SALIDAS
# - descuento, iva, total : float, pesos mexicanos, cada importe mostrado con dos decimales.
#
# REGLAS Y SUPUESTOS
# - Subtotal menor que $1,000: descuento de 0%.
# - Subtotal desde $1,000 y menor que $5,000: descuento de 10%.
# - Subtotal de $5,000 o más: descuento de 20%.
# - El descuento se calcula sobre el subtotal.
# - El IVA es 16% del subtotal después de restar el descuento.
# - total = subtotal - descuento + iva. Se muestran importes con dos decimales.
#
# ALGORITMO
# 1. Leer el subtotal.
# 2. Si subtotal >= 5000, descuento = subtotal * 0.20.
# 3. En caso contrario, si subtotal >= 1000, descuento = subtotal * 0.10.
# 4. En caso contrario, descuento = 0.
# 5. calcularIVA: iva = (subtotal - descuento) * 0.16.
# 6. calcularTotal: total = subtotal - descuento + iva.
# 7. Mostrar subtotal, descuento, IVA y total con dos decimales.
#
# CASOS DE PRUEBA
# 500 -> subtotal 500.00; descuento 0.00; IVA 80.00; total 580.00
# 900 -> subtotal 900.00; descuento 0.00; IVA 144.00; total 1044.00
# 1000 -> subtotal 1000.00; descuento 100.00; IVA 144.00; total 1044.00
# 5000 -> subtotal 5000.00; descuento 1000.00; IVA 640.00; total 4640.00
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerSubtotal() -> float : solicita y devuelve el subtotal.
# calcularDescuento(subtotal: float) -> float : calcula el descuento según el subtotal.
# calcularIVA(subtotal: float, descuento: float) -> float : calcula el IVA sobre el importe descontado.
# calcularTotal(subtotal: float, descuento: float, iva: float) -> float : calcula el total final.
# mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None : muestra el ticket.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerSubtotal():
    return float(input("Ingrese el subtotal de la compra: $"))


def calcularDescuento(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.20
    elif subtotal >= 1000:
        return subtotal * 0.10
    else:
        return 0.0


def calcularIVA(subtotal, descuento):
    return (subtotal - descuento) * 0.16


def calcularTotal(subtotal, descuento, iva):
    return subtotal - descuento + iva


def mostrarTicket(subtotal, descuento, iva, total):
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
