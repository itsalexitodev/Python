# Implementa una función que calcule el factorial de un número dado. 
# El factorial de un número 'n' se calcula multiplicando todos los números enteros desde 1 hasta 'n'.

import math

print("ingrese un numero para calcular su factorial")
numero = input()

def factorial(numero):
    numero = math.factorial(int(numero))
    return numero
resultado = factorial(numero)

print(f"el factorial del {numero} es {resultado}")