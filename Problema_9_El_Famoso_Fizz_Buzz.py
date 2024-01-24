"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * numeros de 1 a 100 (ambos incluidos y con un salto de linea entre
 * cada impresion), sustituyendo los siguientes:
 * - Multiplos de 3 por la palabra "fizz".
 * - Multiplos de 5 por la palabra "buzz".
 * - Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""

numbers = range(1, 101)


for number in numbers:
    if number % 3 == 0:
        print("fizz")
    elif  number % 5 == 0:
        print("Buzz")
    elif number % 3 & number % 5 == 0:
           print("fizzbuzz")
    else:
        print(number)