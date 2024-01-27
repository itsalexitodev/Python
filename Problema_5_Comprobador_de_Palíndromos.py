"""
/*
 * Crea una funcion que determine si una palabra dada es un palindromo 
 * (se lee igual de izquierda a derecha que de derecha a izquierda), 
 * ignorando mayusculas y minusculas.
 */
"""

print("Cual es la palabara que quieres comprobar")
palabra = input()

def palindromo(palabra):
    if palabra == palabra[::-1]:
        print(f"la {palabra}, es palindromo")
    else:
        print(f"la {palabra}, no es palindromo")
palindromo(palabra)

