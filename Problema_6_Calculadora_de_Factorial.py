# Implementa una funci�n que calcule el factorial de un n�mero dado. 
# El factorial de un n�mero 'n' se calcula multiplicando todos los n�meros enteros desde 1 hasta 'n'.

import math

print("ingrese un numero para calcular su factorial")
numero = input()

def factorial(numero):
    numero = math.factorial(int(numero))
    return numero
resultado = factorial(numero)

print(f"el factorial del {numero} es {resultado}")