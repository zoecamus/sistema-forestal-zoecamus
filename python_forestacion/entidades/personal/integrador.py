"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

from dataclasses import dataclass
from datetime import date

@dataclass
class AptoMedico:
    """Certifica si un trabajador está apto para trabajar."""
    apto: bool
    fecha_emision: date
    observaciones: str

    def esta_apto(self) -> bool:
        return self.apto

    def get_resumen(self) -> str:
        estado = "APTO" if self.apto else "NO APTO"
        return f"AptoMedico({estado}, emitido={self.fecha_emision}, obs='{self.observaciones}')"

    def __str__(self):
        return self.get_resumen()


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

from dataclasses import dataclass

@dataclass
class Herramienta:
    """Representa una herramienta utilizada por los trabajadores."""

    id: int
    nombre: str
    estado: str = "Operativa" 
    certificacion_seguridad: str = "IRAM-ISO 45001" #norma argentina e internacional sobre seguridad laboral

    def get_nombre(self):
        return self.nombre
    
    def __str__(self):
        return (f"Herramienta(id={self.id}, nombre='{self.nombre}', estado={self.estado}, "
                f"certificación={self.certificacion_seguridad})")





# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/tarea.py
# ================================================================================

from datetime import date

class Tarea:
    """Representa una tarea asignada a un trabajador."""

    def __init__(self, id: int, descripcion: str, fecha_programada: date):
        self.id = id
        self.descripcion = descripcion
        self.fecha_programada = fecha_programada
        self.completada = False  # estado inicial

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __repr__(self):
        estado = "COMPLETADA" if self.completada else "PENDIENTE"
        return f"Tarea(id={self.id}, desc='{self.descripcion}', fecha={self.fecha_programada}, estado={estado})"
    
    @property
    def estado(self):
        return self.completada

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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



