# gestion_empleados/dao/trabajador_dao.py
import pyodbc
from dto.trabajador_dto import TrabajadorDTO
from utils.db_connection import get_connection
from TrabajadorconDatoslaboralesDTO import TrabajadorConDatosLaboralesDTO
class TrabajadorDAO:
    def __init__(self):
        self.connection = get_connection()

    def insert(self, trabajador_dto):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO Trabajadores (Nombre, RUT, Genero, Direccion, Telefono)
            VALUES (?, ?, ?, ?, ?)
        """, (trabajador_dto.nombre, trabajador_dto.rut, trabajador_dto.genero, 
              trabajador_dto.direccion, trabajador_dto.telefono))
        self.connection.commit()
        
        # Obtener el ID del trabajador recién insertado
        cursor.execute("SELECT @@IDENTITY")
        id_trabajador = cursor.fetchone()[0]
        
        return id_trabajador

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT t.ID_Trabajador, t.Nombre, t.RUT, t.Genero, t.Direccion, t.Telefono, dl.Cargo, dl.Departamento
            FROM Trabajadores t
            LEFT JOIN DatosLaborales dl ON t.ID_Trabajador = dl.ID_Trabajador
        """)
        return [TrabajadorConDatosLaboralesDTO(*row) for row in cursor.fetchall()]

    def get_by_filters(self, genero=None, cargo=None, departamento=None):
        cursor = self.connection.cursor()
        query = """
            SELECT t.ID_Trabajador, t.Nombre, t.RUT, t.Genero, t.Direccion, t.Telefono, dl.Cargo, dl.Departamento
            FROM Trabajadores t
            LEFT JOIN DatosLaborales dl ON t.ID_Trabajador = dl.ID_Trabajador
            WHERE 1=1
        """
        params = []
        if genero:
            query += " AND t.Genero = ?"
            params.append(genero)
        if cargo:
            query += " AND dl.Cargo = ?"
            params.append(cargo)
        if departamento:
            query += " AND dl.Departamento = ?"
            params.append(departamento)
        
        cursor.execute(query, params)
        return [TrabajadorConDatosLaboralesDTO(*row) for row in cursor.fetchall()]

    def update(self, trabajador_dto):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Trabajadores
            SET Nombre = ?, RUT = ?, Genero = ?, Direccion = ?, Telefono = ?
            WHERE ID_Trabajador = ?
        """, (trabajador_dto.nombre, trabajador_dto.rut, trabajador_dto.genero,
              trabajador_dto.direccion, trabajador_dto.telefono, trabajador_dto.id_trabajador))
        self.connection.commit()
        return cursor.rowcount

    def delete(self, id_trabajador):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Trabajadores WHERE ID_Trabajador = ?", (id_trabajador,))
        self.connection.commit()
        return cursor.rowcount
