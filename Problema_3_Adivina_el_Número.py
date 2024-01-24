"""""
Desarrolla un juego en el que el programa elige un número aleatorio entre 1 y 100, 
y el jugador debe adivinar ese número.
El programa debe proporcionar pistas (mayor, menor o correcto) hasta que el jugador adivine.
"""

import os
import random
import time

print("Hola, introduce tu nombre")
username = input()
os.system("cls")

print(f"Hola {username}, vamos a jugar a un juego")
os.system("cls")

vidas = 10
print(f"{username}, quiero que adivines un número entre 1 y 100")

while True:
    print("Introduce un número:")
    adivinar = int(input())
    os.system("cls")

    numero = random.randint(1, 100)

    if adivinar < numero:
        print(f"El número {adivinar} es mayor al número que he pensado.")
        time.sleep(2)
    elif adivinar > numero:
        print(f"El número {adivinar} es menor al número que he pensado.")
        time.sleep(2)
    else:
        print(f"¡Felicidades, {username}! Has adivinado el número correctamente.")
        break

    vidas -= 1
    if vidas == 0:
        print(f"El número a adivinar era {numero}. Has agotado tus vidas. ¡Intenta de nuevo!")
        break
