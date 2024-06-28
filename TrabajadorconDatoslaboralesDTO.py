class TrabajadorConDatosLaboralesDTO:
    def __init__(self, id_trabajador, nombre, rut, genero, direccion, telefono, cargo, departamento):
        self.id_trabajador = id_trabajador
        self.nombre = nombre
        self.rut = rut
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.departamento = departamento