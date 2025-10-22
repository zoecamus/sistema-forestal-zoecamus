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
