class DatosLaboralesDTO:
    def __init__(self, id_trabajador=None, cargo=None, fecha_ingreso=None, area=None, departamento=None):
        self.id_trabajador = id_trabajador
        self.cargo = cargo
        self.fecha_ingreso = fecha_ingreso
        self.area = area
        self.departamento = departamento

    def to_dict(self):
        return {
            'id_trabajador': self.id_trabajador,
            'cargo': self.cargo,
            'fecha_ingreso': self.fecha_ingreso,
            'area': self.area,
            'departamento': self.departamento
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)