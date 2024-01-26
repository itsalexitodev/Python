"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 """

print("Ingresa la primera palabra: ")
palabra_usuario1 = input()

print("Ingresa la segunda palabra: ")
palabra_usuario2 = input()

def verificar_anagrama(palabra1,palabra2 ):
   palabra1 = palabra1.replace("","").lower()
   palabra2 = palabra2.replace("","").lower()
   return sorted(palabra1) == sorted(palabra2)

resultado = verificar_anagrama(palabra_usuario1,palabra_usuario2)

if resultado:
    print(f"{palabra_usuario1} y {palabra_usuario2} son anagramas.")
else:
    print(f"{palabra_usuario1} y {palabra_usuario2} no son anagramas.")