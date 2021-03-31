"""
Módulo encargado de realizar las operaciones a la base de datos MariaDB
"""

# Datos de conexión a la base de datos
BD = {
    #Se Cambiaron los datos de la Biblioteca DB por Banco
    "database":"adopet_django",
    "host":"localhost",
    "user":"pet",
    "password":"pet"
}

# zona de imports
from mysql.connector import connect, Error


def connect_db():
    """
    Se conecta a la base de datos BD, regresa un conecto o None en caso
    de error.
    """
    try:
        conn = connect(**BD)
    except Error as err:
        print(err)
        return None

    return conn

def get_registers(table):
    """
    Obtiene la lista de registros de tabla y los regresa en forma de lista
    """
    # Se realiza la conexión a la base de datos
    conn = connect_db()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {}".format(table)
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        registers = [[r[0].capitalize() for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        registers += cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registers
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def get_tables():
    """
    Obtiene la lista de tablas en la base de datos
    """
    # Se realiza la conexión a la base de datos
    conn = connect_db()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SHOW TABLES"
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de resultados de la consulta SQL
        registers = cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registers
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def add_register(table, values):
    """ Agrega un registro en tabla """
    # Se realiza la conexión a la BD
    conn = connect_db()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se arma una tupla con los valores de los campos
        # Se crea una cadena con tantos símbolos "%s" como valores
        # tengamos separados por comas
        signs = ", ".join(["%s"] * len(values))
        # Se crea la consulta en SQL
        sql = "insert into {} values (null, {})".format(table, signs)
        # Se ejecuta la consulta
        cur.execute(sql, values)
        # Se ejecuta un commit para indicar que la inserción se ejecute como una
        # operación atómica.
        conn.commit()
        # Se cierra la BD
        conn.close()
        # Se regresa True para indicar que el registro se ha insertado con
        # éxito
        return True

    return False  # En caso de error

def get_register(table, id):
    """
    Obtiene el registro id de tabla
    """
    # Se realiza la conexión a la base de datos
    conn = connect_db()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {} WHERE id=%s".format(table)
        # Se ejecuta la consulta
        cur.execute(sql, (id,))
        # Se obtiene el resultados de la consulta SQL
        register = cur.fetchone()
        # Se cierra la BD
        conn.close()

        return register
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return None

def update_register(table, id, values):
    """ Modifica un registro de la tabla """
    # Se realiza la conexión a la BD
    conn = connect_db()
    if conn:
        values = (id,) + values
        register = get_register(table, id)
        register = [t[0] if t[1] == None else t[1]
            for t in zip(register, values)]
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se arma una tupla con los valores de los campos
        # Se crea una cadena con tantos símbolos "%s" como valores
        # tengamos separados por comas
        signs = ", ".join(["%s"] * len(values))
        # Se crea la consulta en SQL
        sql = "REPLACE INTO {} VALUES ({})".format(table, signs)
        # Se ejecuta la consulta
        cur.execute(sql, register)
        # Se ejecuta un commit para indicar que la inserción se ejecute como una
        # operación atómica.
        conn.commit()
        # Se cierra la BD
        conn.close()
        # Se regresa True para indicar que el registro se ha insertado con
        # éxito
        return True

    return False  # En caso de error

def execute_sql(sql):
    """
    Ejecuta las instrucciones proporcionadas por sql y regresa True en
    caso de éxtio, False en caso contrario.
    """
    # Se realiza la conexión a la base de datos
    conn = connect_db()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se ejecuta la consulta
        #mysql.connector.errors.InterfaceError: Use multi=True when executing multiple statements
        cur.execute(sql, multi=True)

        # Se cierra la BD
        conn.close()

        return True
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return False