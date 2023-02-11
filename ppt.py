# Menú
# 1. Piedra
# 2. Papel
# 3. Tijera
# Opción: _

import random

def juego_ppt():
    # Opción del usuario
    nombre_usuario = input("Ingresa tu nombre: ")
    menu = """
    Menú
    1. Piedra
    2. Papel
    3. Tijera
    4. Rasengan
    """
    print(menu)
    opcion_usuario = input("Opción: ")

    if opcion_usuario == "1":
        opcion_usuario = "Piedra"
    elif opcion_usuario == "2":
        opcion_usuario = "Papel"
    elif opcion_usuario == "3":
        opcion_usuario = "Tijera"
    elif opcion_usuario == "4":
        opcion_usuario = "Rasengan"

    # Opción de la computadora
    opcion_pc = random.randint(1,4)

    if opcion_pc == 1:
        opcion_pc = "Piedra"
    elif opcion_pc == 2:
        opcion_pc = "Papel"
    elif opcion_pc == 3:
        opcion_pc = "Tijera"
    elif opcion_pc == 4:
        opcion_pc = "Rasengan"

    print("La PC eligió ", opcion_pc)

    # Verificar ganador

    # Empate
    if opcion_usuario == opcion_pc:
        print("¡ES UN EMPATE!")
    elif opcion_usuario == "Piedra" and opcion_pc == "Papel":
        print("PC GANÓ")
    elif opcion_usuario == "Piedra" and opcion_pc == "Tijera":
        print(nombre_usuario, " GANÓ")
    elif opcion_usuario == "Papel" and opcion_pc == "Piedra":
        print(nombre_usuario, " GANÓ")
    elif opcion_usuario == "Papel" and opcion_pc == "Tijera":
        print("PC GANÓ")
    elif opcion_usuario == "Tijera" and opcion_pc == "Papel":
        print(nombre_usuario, " GANÓ")
    elif opcion_usuario == "Tijera" and opcion_pc == "Piedra":
        print("PC GANÓ")
    elif opcion_usuario == "Rasengan":
        print(nombre_usuario, " GANÓ")
    elif opcion_pc == "Rasengan":
        print("PC GANÓ")