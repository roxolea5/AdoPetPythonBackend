import click
from mysqlmodel import add_register


@click.command()
@click.argument("username")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
@click.argument("password")
@click.argument("date_of_birth")
@click.argument("photo")
@click.argument("status", type=int)
@click.argument("role_id", type=int)
def add_user(username, first_name, last_name, email, password, date_of_birth,
    photo, status, role_id):
    """
    Agrega un nuevo registro a la tabla Libro con los campos TITULO,
    EDITORIAL, NUMPAG y AUTORES. Imprime un mensaje si el registro se agrega
    exitosamente a la tabla.
    """
    table = "user"
    register = (username, first_name, last_name, email, password, date_of_birth,
    photo, status, role_id)
    if add_register(table, register):
        print("Se ha agregado el registro {} a la tabla {}".format(
            register, table))

if __name__ == '__main__':
    add_user()