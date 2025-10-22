"""
Archivo integrador generado automaticamente
Directorio: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones
Fecha: 2025-10-22 09:45:41
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class AguaAgotadaException(ForestacionException):
    """
    Lanzada cuando el agua disponible en la plantación se agota por debajo del mínimo permitido.
    """

    def __init__(self, disponible: int, minima: int):
        super().__init__(
            "ERROR_02",
            f"Agua agotada. Disponible: {disponible} L, mínima requerida: {minima} L."
        )
        self.disponible = disponible
        self.minima = minima


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del sistema de forestación.
    """

    def __init__(self, error_code: str, user_message: str):
        super().__init__(f"[{error_code}] {user_message}")
        self.error_code = error_code
        self.user_message = user_message

    def get_error_code(self):
        return self.error_code

    def get_user_message(self):
        return self.user_message

    def get_full_message(self):
        return f"Error {self.error_code}: {self.user_message}"


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

class MensajesException:
    """
    Centraliza los mensajes de error del sistema para mantener coherencia.
    """

    SUPERFICIE_INSUFICIENTE = "Superficie insuficiente para el cultivo solicitado."
    AGUA_AGOTADA = "El nivel de agua en la plantación es insuficiente."
    PERSISTENCIA_ERROR = "Error durante la persistencia de datos."
    REGISTRO_NO_ENCONTRADO = "No se encontró el registro solicitado."


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class PersistenciaException(ForestacionException):
    """
    Excepción para errores de lectura/escritura de archivos de persistencia.
    """

    def __init__(self, tipo_operacion: str, nombre_archivo: str):
        super().__init__(
            "ERROR_03",
            f"Error en operación de {tipo_operacion} sobre archivo '{nombre_archivo}'."
        )
        self.tipo_operacion = tipo_operacion
        self.nombre_archivo = nombre_archivo

    @staticmethod
    def from_ioerror(nombre_archivo: str):
        return PersistenciaException("ESCRITURA", nombre_archivo)

    @staticmethod
    def from_classnotfound(nombre_archivo: str):
        return PersistenciaException("LECTURA", nombre_archivo)


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/zoe/Diseño de sistemas /parcial/sistema-forestal-zoecamus/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """
    Lanzada cuando la superficie disponible de la plantación no alcanza
    para el cultivo solicitado.
    """

    def __init__(self, tipo_cultivo: str, requerida: float, disponible: float):
        super().__init__(
            "ERROR_01",
            f"Superficie insuficiente para {tipo_cultivo}. "
            f"Requerida: {requerida} m², disponible: {disponible} m²."
        )
        self.tipo_cultivo = tipo_cultivo
        self.requerida = requerida
        self.disponible = disponible


