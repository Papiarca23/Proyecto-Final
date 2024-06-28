from utils.db_connection import get_connection
from dto.datos_laborales_dto import DatosLaboralesDTO

class DatosLaboralesDAO:
    def __init__(self):
        self.connection = get_connection()

    def insert(self, datos_laborales_dto):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO DatosLaborales (ID_Trabajador, Cargo, FechaIngreso, Area, Departamento)
            VALUES (?, ?, ?, ?, ?)
        """, (datos_laborales_dto.id_trabajador, datos_laborales_dto.cargo, 
              datos_laborales_dto.fecha_ingreso, datos_laborales_dto.area, 
              datos_laborales_dto.departamento))
        self.connection.commit()
        return cursor.rowcount

    def get_by_trabajador_id(self, id_trabajador):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM DatosLaborales WHERE ID_Trabajador = ?", (id_trabajador,))
        row = cursor.fetchone()
        if row:
            return DatosLaboralesDTO.from_dict(dict(zip([column[0] for column in cursor.description], row)))
        return None

    def update(self, datos_laborales_dto):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE DatosLaborales
            SET Cargo = ?, FechaIngreso = ?, Area = ?, Departamento = ?
            WHERE ID_Trabajador = ?
        """, (datos_laborales_dto.cargo, datos_laborales_dto.fecha_ingreso,
              datos_laborales_dto.area, datos_laborales_dto.departamento,
              datos_laborales_dto.id_trabajador))
        self.connection.commit()
        return cursor.rowcount

    def delete(self, id_trabajador):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM DatosLaborales WHERE ID_Trabajador = ?", (id_trabajador,))
        self.connection.commit()
        return cursor.rowcount