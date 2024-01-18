"""
Escribe un programa que genere una contrasenya aleatoria. 
La contrasenya debe tener una longitud predeterminada y contener letras mayusculas, letras minusculas y numeros.
"""

import random

characters = ["A","B", "C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",
              "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for cahracter in range(1):
    longitud = 8
    contrasena = ''.join(random.choices(characters, k=longitud))
    print(contrasena)