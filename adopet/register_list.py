import click
from mysqlmodel import get_registers, get_tables
from stdout import print_registers

@click.command()
@click.argument("table", required=False)
def register_list(table):
    """
    Imprime la lista de registros de TABLA  en la salida estándar, si no se
    proporciona una tabla, se imprime la Lista de tablas disponibles.
    """
    if table:
        # Se obtiene la lista de registros de tabla
        registers = get_registers(table)
        # Se imprimen los registros en formato texto en la salida estándar
        print_registers(registers, "Tabla: {}".format(table))
    else:
        tables = get_tables()
        print_registers(tables, "Tablas disponibles")

if __name__ == '__main__':
    register_list()
