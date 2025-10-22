import os
import pickle
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


class RegistroForestalService:
    """Servicio encargado de la persistencia del registro forestal."""

    def __init__(self, registry: CultivoServiceRegistry):
        self.registry = registry

    def persistir(self, registro: RegistroForestal) -> None:
        """Guarda un registro en disco usando pickle."""
        os.makedirs("data", exist_ok=True)
        archivo = f"data/{registro.propietario}.dat"
        try:
            with open(archivo, "wb") as f:
                pickle.dump(registro, f)
            print(f"[PERSISTENCIA] Registro '{registro.propietario}' guardado en {archivo}")
        except Exception as e:
            raise PersistenciaException("ESCRITURA", archivo, str(e))

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """Lee un registro desde disco."""
        archivo = f"data/{propietario}.dat"
        try:
            with open(archivo, "rb") as f:
                registro = pickle.load(f)
            print(f"[LECTURA] Registro '{propietario}' leído correctamente.")
            return registro
        except FileNotFoundError:
            raise PersistenciaException("LECTURA", archivo, "Archivo no encontrado.")
        except Exception as e:
            raise PersistenciaException("LECTURA", archivo, str(e))



    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """Muestra información completa del registro forestal."""
        print("\n" + "=" * 70)
        print("REGISTRO FORESTAL")
        print("=" * 70)
        print(f"Propietario: {registro.propietario}")
        print(f"Avalúo fiscal: ${registro.avaluo:,.2f}")
        print(f"ID Padrón: {registro.id_padron}\n")
    
        print("--- TERRENO ---")
        print(f"Ubicación: {registro.tierra.domicilio}")
        print(f"Superficie: {registro.tierra.superficie} m²\n")
    
        print("--- PLANTACIÓN ---")
        print(f"Nombre: {registro.plantacion.nombre}")
        print(f"Agua disponible: {registro.plantacion.agua_disponible} L")
        print(f"Cultivos: {len(registro.plantacion.cultivos)}")
        print(f"Trabajadores: {len(registro.plantacion.trabajadores)}")
        print("=" * 70 + "\n")

