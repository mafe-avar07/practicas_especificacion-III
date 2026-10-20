# PROBLEMA
# calcular la calificación final ponderada de tres parciales e indicar si la materia se aprueba.
#
# ENTRADAS
# - parcial1, parcial2, parcial3 : float, puntos de calificación, de 0 a 100.
#
# SALIDAS
# - final : float, puntos, mostrado con dos decimales.
# - estado : str, texto “Aprobado” o “Reprobado”.
#
# REGLAS Y SUPUESTOS
# - Los parciales pesan 30%, 30% y 40%, respectivamente.
# - La calificación final = parcial1*0.30 + parcial2*0.30 + parcial3*0.40.
# - Se reprueba si cualquier parcial es menor que 50, incluso si la final es 70 o más.
# - Si ningún parcial es menor que 50, se aprueba con final mayor o igual a 70.
# - La final se muestra con dos decimales; la decisión se toma con el valor sin redondear.
#
# ALGORITMO
# 1. Leer los tres parciales.
# 2. Calcular final = parcial1*0.30 + parcial2*0.30 + parcial3*0.40.
# 3. Si algún parcial < 50, estado = "Reprobado".
# 4. En caso contrario, si final >= 70, estado = "Aprobado".
# 5. En caso contrario, estado = "Reprobado".
# 6. Mostrar la final con dos decimales y el estado.
#
# CASOS DE PRUEBA
# (80, 70, 90) -> final 81.00; Aprobado
# (70, 70, 70) -> final 70.00; Aprobado
# (100, 100, 40) -> final 76.00; Reprobado
# (69, 70, 70) -> final 69.70; Reprobado
#
# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#
# CONTRATO DE FUNCIONES
# leerParciales() -> tuple : solicita y devuelve los tres parciales en orden.
# calcularFinal(parcial1: float, parcial2: float, parcial3: float) -> float : calcula la ponderación.
# determinarEstado(parcial1: float, parcial2: float, parcial3: float, final: float) -> str : determina aprobación.
# mostrarResultado(final: float, estado: str) -> None : muestra final y estado.
#
# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerParciales():
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
    return parcial1, parcial2, parcial3


def calcularFinal(parcial1, parcial2, parcial3):
    return parcial1 * 0.30 + parcial2 * 0.30 + parcial3 * 0.40


def determinarEstado(parcial1, parcial2, parcial3, final):
    if parcial1 < 50 or parcial2 < 50 or parcial3 < 50:
        return "Reprobado"
    elif final >= 70:
        return "Aprobado"
    else:
        return "Reprobado"


def mostrarResultado(final, estado):
    print(f"Calificación final: {final:.2f}")
    print(f"Estado: {estado}")
