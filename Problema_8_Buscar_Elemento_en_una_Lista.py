"""
Desarrolla una funcion que busque un elemento especifico en una lista. 
La funcion debe devolver la posicion del elemento si se encuentra y un 
mensaje indicando que el elemento no esta presente en caso contrario.
"""

print("que marca de coche quieres buscar")
marca = input()

marcas_de_coches = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "BMW", "Mercedes-Benz", "Audi", "Nissan", "Tesla"]

if marca == marcas_de_coches:
    print(f"la marca es {marca} ")    