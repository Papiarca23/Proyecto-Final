# gestion_empleados/services/trabajador_service.py

from dao.trabajador_dao import TrabajadorDAO
from dao.datos_laborales_dao import DatosLaboralesDAO
from dto.trabajador_dto import TrabajadorDTO
from dto.datos_laborales_dto import DatosLaboralesDTO

class TrabajadorService:
    def __init__(self):
        self.trabajador_dao = TrabajadorDAO()
        self.datos_laborales_dao = DatosLaboralesDAO()

    def crear_trabajador(self, trabajador_dto, datos_laborales_dto):
        # Validaciones
        if not trabajador_dto.nombre or not trabajador_dto.rut:
            raise ValueError("Nombre y RUT son campos obligatorios")

        # Insertar trabajador y obtener el ID
        trabajador_id = self.trabajador_dao.insert(trabajador_dto)
        
        # Asignar el ID del trabajador a los datos laborales
        datos_laborales_dto.id_trabajador = trabajador_id
        self.datos_laborales_dao.insert(datos_laborales_dto)

        return trabajador_id

    def obtener_trabajadores_filtrados(self, genero=None, cargo=None, departamento=None):
        return self.trabajador_dao.get_by_filters(genero, cargo, departamento)

    def actualizar_trabajador(self, trabajador_dto):
        # Validaciones
        if not trabajador_dto.id_trabajador:
            raise ValueError("ID de trabajador es necesario para actualizar")

        return self.trabajador_dao.update(trabajador_dto)

    def eliminar_trabajador(self, id_trabajador):
        return self.trabajador_dao.delete(id_trabajador)