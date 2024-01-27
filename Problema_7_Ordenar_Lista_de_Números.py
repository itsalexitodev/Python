"""
/*
 * Escribe un programa que tome una lista de números como entrada 
 * y devuelva la lista ordenada de forma ascendente.
 */
"""

print("Ingrese una lista de números separados por espacio:")
num_list =  [int(x) for x in input().split()]

def ordenar_lista(lista):
    lista_ordenada  = sorted(lista)
    return lista_ordenada


lista_ordenada = ordenar_lista(num_list)
print(f"Lista ordenada: {lista_ordenada}")