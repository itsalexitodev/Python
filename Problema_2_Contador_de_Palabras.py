# Crea una funci�n que tome una cadena como entrada y 
# devuelva el n�mero de palabras en esa cadena. 
# Considera que las palabras est�n separadas por espacios.

print("Ingrese una cadena de texto: ")
texto = input()

def contar_palabras(texto):
    return len(texto)

cantidad_palabras = contar_palabras(texto)
print(f"La cantidad de palabras en la cadena es: {cantidad_palabras}")
