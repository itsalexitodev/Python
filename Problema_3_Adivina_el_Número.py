# Desarrolla un juego en el que el programa elige un número aleatorio entre 1 y 100, 
# y el jugador debe adivinar ese número.
# El programa debe proporcionar pistas (mayor, menor o correcto) hasta que el jugador adivine.

import os
import random

print("Hola introduce tu nombre")
username = input()
os.system("cls")

print(f"hola {username}, vamos a jugar a un juego")
os.system("cls")

vidas = 3

while-True:
    print(f"{username}, quiero que adivines un numero entre el 1 y el 100")
    
    adivinar = int(input())

    numero = random.randint(1, 10)
    
    if adivinar < numero:
        print(f"el numero a {adivinar}, es menor al numero que he pensado")
  
    if adivinar > numero:
        print(f"el numero a {adivinar}, es mayor al numero que he pensado")
    vidas -= 1
    
    if adivinar == numero:
        print(f"el numero a {adivinar}, es correcto")
    
    else:
        if vidas == 0:
            print(f"el numero a adivinar era {numero}")
    