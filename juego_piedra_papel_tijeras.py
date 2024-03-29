# -*- coding: utf-8 -*-
"""Juego_Piedra_Papel_Tijeras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17wker2DjDM4JOxuhlztBVlYD1zdSO2Ne
"""

import random

def juego():
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}

    while True:
        print("Elige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")

        while True:
            try:
                user = int(input("Elige entre las tres opciones (1, 2 o 3): "))
                if user < 1 or user > 3:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, ingresa un número válido del 1 al 3.")

        computer = random.randint(1, 3)
        print("El otro jugador elige", opciones[computer])

        print("Tu elección:", opciones[user])

        if user == computer:
            print("Es un empate.")
        elif (user == 1 and computer == 3) or \
             (user == 2 and computer == 1) or \
             (user == 3 and computer == 2):
            print("¡Has ganado!")
        else:
            print("¡Has perdido!")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

juego()