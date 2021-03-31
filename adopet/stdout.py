"""
Módulo encargado de realizar imprimir información a la salida estándar (STDOUT)
"""

import datetime

def print_registers(registers, title=None):
    """
    Imprime la lista de registros en la salida estándar en formato texto, cada
    registro es de tipo lista.

    username - Es de tipo str y si es proporcionado se imprime como username
    """
    # Se calcula el ancho máximo para cada columna
    width = [[len(str(field)) for field in reg] for reg in registers]
    width = [max(col) for col in zip(*width)]

    # Se imprime la lista
    print()
    if title: print(title)
    print("-" * len(title))
    for reg in registers:
        # Se cambia los valores None por cademas vacias para impresión
        reg = tuple(r if r != None else "" for r in reg)
        # Se combierten las fechas a str
        reg = tuple(str(r) if type(r) == datetime.date else r for r in reg)
        # Se formatea cada registro en una línea de texto
        reg = zip(reg, width)
        reg = ["{:{}}".format(*field) for field in reg]
        print(" | ".join(reg))
    print("-" * len(title))
    print()
