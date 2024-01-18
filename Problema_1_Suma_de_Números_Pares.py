# Escribe un programa que solicite al usuario un número entero positivo 'n' y 
# luego calcule la suma de los primeros 'n' números pares.
# -*- coding: utf-8 -*-

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def suma_numeros_pares():
    while True:
        try:
            print("Ingresa un numero entero positivo:")
            n = int(input())
            if n > 0:
                break
            else:
                print("Por favor, ingresa un numero entero positivo")
        except ValueError:
            print("Error: Ingresa un numero entero valido")

    suma = 0
    for i in range(1, n + 1):
        if es_primo(i): 
            suma += 2 * i
    return n, suma

n, resultado = suma_numeros_pares()
print(f"La suma de los primeros pares de {n} es {resultado}")
