import random
from collections import Counter
import os
from typing import Optional


def write_result(result_dict: dict[str, str]):
    # Crear la carpeta 'resultado' si no existe
    output_dir = os.path.join(os.getcwd(), 'resultado')
    os.makedirs(output_dir, exist_ok=True)  # `exist_ok=True` evita error si la carpeta ya existe

    # Recorremos el diccionario de resultados
    for giver, receiver in result_dict.items():
        # Construimos la ruta completa para el archivo
        filename = os.path.join(output_dir, f"{giver}.txt")

        # Abrimos el archivo para escribir (si no existe, se crea)
        with open(filename, 'w') as file:
            # Escribimos el mensaje en el archivo
            file.write(f"Has de regalar a {receiver}")


def check_result(participants: list[str], result_dict: dict[str, str]) -> bool:
    # Comprobamos que nadie se regale a sí mismo
    for name in participants:
        if result_dict[name] == name:
            return False

    # Verificamos que no haya receptores duplicados
    receivers = list(result_dict.values())
    if len(receivers) != len(set(receivers)):
        return False

    # Verificamos que todos los participantes estén correctamente asignados
    if sorted(result_dict.keys()) != sorted(participants):
        return False

    return True


def get_random_pair(participants: list[str]) -> dict[str, str]:
    while True:
        receivers = participants.copy()
        random.shuffle(receivers)
        # evitamos self-assignments
        if all(g != r for g, r in zip(participants, receivers)):
            return dict(zip(participants, receivers))


def get_participants() -> Optional[list[str]]:
    namefile = input("Ruta archivo con los participantes: ")
    try:
        names = []
        with open(namefile, "r") as f:
            for line in f:
                names += line.split()

        return names

    except FileNotFoundError:
        print(f"Archivo {namefile} no encontrado.")
    except OSError:
        print(f"No se pudo abrir el archivo {namefile}.")

    return None


def start_process():
    participants = get_participants()
    if participants is None:
        print("No se pudieron obtener los participantes.")
        return

    result_dict = get_random_pair(participants)
    if check_result(participants, result_dict):
        write_result(result_dict)
        print("Los archivos han sido generados correctamente.")
    else:
        print("Error en el emparejamiento:", result_dict)


if __name__ == '__main__':
    start_process()
