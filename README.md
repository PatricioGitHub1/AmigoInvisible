SORTEO DE AMIGO INVISIBLE (SECRET SANTA) – PYTHON
================================================

Script en Python que lee una lista de participantes desde un archivo de texto,
genera un emparejamiento aleatorio sin que nadie se regale a sí mismo y crea
un archivo .txt por participante con el nombre de la persona a la que debe regalar.


REQUISITOS
----------
- Python 3.10 o superior
- No se utilizan librerías externas


ARCHIVO DE PARTICIPANTES
-----------------------
Crea un archivo de texto (por ejemplo: participantes.txt) con los nombres
separados por espacios o saltos de línea.

Ejemplo:
Patricio
Juan
Alberto
Maria

Los nombres deben ser únicos.


EJECUCIÓN
---------
1. Guarda el script con el nombre:
   amigo_invisible.py

2. Ejecuta el programa:
   python amigo_invisible.py

3. Introduce la ruta del archivo de participantes cuando el programa lo solicite.


SALIDA
------
El programa crea una carpeta llamada "resultado" en el directorio actual.
Dentro se genera un archivo por cada participante, por ejemplo:

resultado/Patricio.txt
resultado/Maria.txt
...

Cada archivo contiene un mensaje del tipo:
Has de regalar a Patricio


DETALLES DE FUNCIONAMIENTO
-------------------------
- El emparejamiento se obtiene barajando la lista de participantes hasta que
  no existan auto-asignaciones.
- El algoritmo garantiza:
  * Nadie se regala a sí mismo
  * No hay receptores duplicados
  * Todos los participantes quedan asignados exactamente una vez
