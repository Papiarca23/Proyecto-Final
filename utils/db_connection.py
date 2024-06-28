import pyodbc

def get_connection():
    server = 'Matias'
    database = 'Proyectofinal2'
    username = 'Matias'
    password = 'Chancho1.'
    
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        print(f"Error de conexión: {e}")
        return None
