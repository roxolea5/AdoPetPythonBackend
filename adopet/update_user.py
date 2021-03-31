import click
from mysqlmodel import update_register


@click.command()
@click.argument("id", type=int)
@click.argument("username")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
@click.argument("password")
@click.argument("date_of_birth")
@click.argument("photo")
@click.argument("status", type=int)
@click.argument("role_id", type=int)
def update_user(id, username, first_name, last_name, email, password, 
    date_of_birth, photo, status, role_id):
    """
    Modifica un egistro de la tabla user. Si se proporciona un valor a un campo, ese
    valor será actualizado en la base de datos. Si no se desea actualizar
    un campo, entonces colocar el valor None.  Imprime un mensaje si el
    registro se atualiza exitosamente.
    """
    value = lambda cad, value: value if cad == "None" else cad
    table = "user"
    status = value(status, None)
    role_id = value(role_id, None)
    try:
        register = (
            value(username, None),
            value(first_name, None),
            value(last_name, None),
            value(email, None),
            value(password, None),
            value(date_of_birth, None),
            value(photo, None))
    except ValueError:
        print("\nError: Uno de los valores fue introducido incorrectamente\n")
        return
    if update_register(table, id, register):
        register = (id,) + register
        print("Se ha actualizado el registro {} a la tabla {}".format(
            register, table))

if __name__ == '__main__':
    update_user()