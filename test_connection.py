# test_connection.py

from utils.db_connection import get_connection

def test_sql_connection():
    connection = get_connection()
    if connection:
        print("Conexión exitosa a la base de datos SQL Server.")
        cursor = connection.cursor()
        cursor.execute("SELECT @@VERSION")
        row = cursor.fetchone()
        print(f"Versión del servidor SQL: {row[0]}")
        connection.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

if __name__ == "__main__":
    test_sql_connection()