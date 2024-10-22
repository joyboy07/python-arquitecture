import pymssql
from decouple import config

def initialize_sql():
    try:
        server = config('HOST')
        database = config('DB')
        username = config('USERDB')
        password = config('PASSWORD')

        conn = pymssql.connect(server=server, user=username, password=password, database=database)
        print("Conexión exitosa.")
        return conn
    except pymssql.DatabaseError as e:
        print(f"Error de conexión: {e}")
        return None

    except Exception as e:
        print(f"Otro error: {e}")
        return None