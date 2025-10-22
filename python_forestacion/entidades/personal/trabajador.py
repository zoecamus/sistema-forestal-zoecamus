from datetime import date
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    """
    Representa a un trabajador agrícola, con DNI, nombre, apto médico y tareas asignadas.
    """

    def __init__(self, dni: int, nombre: str, tareas=None):
        self.dni = dni
        self.nombre = nombre
        self.apto_medico = None
        self.tareas = tareas or []

    def get_nombre(self):
        return self.nombre

    def get_apto_medico(self):
        return self.apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico):
        #Asigna o actualiza el apto médico del trabajador
        self.apto_medico = apto_medico

    def get_tareas(self):
        return list(self.tareas)

    def asignar_apto_medico(self, apto: bool, fecha: date, obs: str):
        #Crea y asigna un nuevo AptoMedico
        self.apto_medico = AptoMedico(apto, fecha, obs)

    def __repr__(self):
        return f"Trabajador(dni={self.dni}, nombre='{self.nombre}')"

class PropietarioFinca:
    """Actor del sistema: gestiona el registro forestal y supervisa operaciones."""

    def __init__(self, nombre: str, dni: int):
        self.nombre = nombre
        self.dni = dni

    def supervisar_operaciones(self):
        print(f"[PROPIETARIO] {self.nombre} supervisa las operaciones de la finca.")

    def registrar_finca(self, nombre_finca: str):
        print(f"[PROPIETARIO] {self.nombre} registró la finca '{nombre_finca}' exitosamente.")


class AuditorInspector:
    """Actor del sistema: consulta registros persistidos para verificación."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    def verificar_registro(self, propietario: str):
        print(f"[AUDITOR] {self.nombre} está verificando el registro de '{propietario}' en el sistema.")

