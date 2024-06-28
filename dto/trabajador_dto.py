# gestion_empleados/dto/trabajador_dto.py

class TrabajadorDTO:
    def __init__(self, id_trabajador=None, nombre=None, rut=None, genero=None, direccion=None, telefono=None):
        self.id_trabajador = id_trabajador
        self.nombre = nombre
        self.rut = rut
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono

    def to_dict(self):
        return {
            'id_trabajador': self.id_trabajador,
            'nombre': self.nombre,
            'rut': self.rut,
            'genero': self.genero,
            'direccion': self.direccion,
            'telefono': self.telefono
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_trabajador=data.get('ID_Trabajador'),
            nombre=data.get('Nombre'),
            rut=data.get('RUT'),
            genero=data.get('Genero'),
            direccion=data.get('Direccion'),
            telefono=data.get('Telefono')
        )
