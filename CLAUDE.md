### CLAUDE.md ###

Este archivo brinda orientación a Claude Code (claude.ai/code) para trabajar con el código de este repositorio.

### Descripción general del proyecto

Este es un sistema en Python para la gestión forestal (Forestación), que incluye plantaciones, cultivos, sistemas de riego y trabajadores.
El proyecto implementa un patrón de arquitectura Entidad–Servicio, junto con el uso de patrones de diseño como Factory Method y Registry Pattern, además de control concurrente simulado para el riego automatizado.

### Cómo ejecutar el proyecto

Ejecución
Desde la raíz del proyecto:
python3 main.py

El punto de entrada principal es el archivo main.py.


### Arquitectura y patrones utilizados
Patrón Entidad–Servicio

El código separa de manera estricta las entidades (datos y estado) de los servicios (lógica de negocio).

Entidades (entidades/) → solo contienen atributos y métodos simples (__init__, __str__, getters/setters).
No incluyen lógica de negocio.
Servicios (servicios/) → implementan las operaciones, validaciones y reglas sobre las entidades.

Ejemplo:

Pino es una entidad que representa un cultivo.
PinoService maneja la lógica de absorción de agua o crecimiento del pino.



### Principales patrones y conceptos
Factory Method

El patrón Factory crea cultivos según su tipo sin exponer la lógica interna

### Registry Pattern

CultivoServiceRegistry actúa como un registro central que asocia clases de cultivos con sus servicios correspondientes.
De esta forma se evita usar if o instanceof

### Inyección de dependencias

Los servicios reciben sus dependencias mediante el constructor, en lugar de crearlas dentro

### Manejo de excepciones personalizado

El sistema usa una jerarquía de excepciones específicas:
ForestacionException → excepción base
SuperficieInsuficienteException → se lanza cuando la superficie es insuficiente
AguaAgotadaException → cuando el agua baja del nivel mínimo
PersistenciaException → errores de lectura/escritura de archivos

Cada excepción incluye un código de error, mensaje técnico y mensaje para el usuario.

### Flujo general de negocio

Se crea una tierra y plantación.
Se registra la finca y los cultivos.
Se plantan los cultivos
Se riega automáticamente (control de sensores de humedad/temperatura)
Se pueden cosechar cultivos 
Se guardan los registros 

### Persistencia

Los datos del registro forestal se guardan en archivos .dat dentro del directorio /data.
Cada propietario tiene su propio archivo.
Se utiliza serialización de objetos (pickle) con manejo de errores controlado.


### ZOE CAMUS ###