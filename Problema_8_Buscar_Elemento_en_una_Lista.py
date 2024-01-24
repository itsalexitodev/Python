"""
Desarrolla una funcion que busque un elemento especifico en una lista. 
La funcion debe devolver la posicion del elemento si se encuentra y un 
mensaje indicando que el elemento no esta presente en caso contrario.
"""

import os
import time

print("Ingrese una marca de coche:")
car_ls = ["Toyota Camry", "Honda Accord", "Ford Mustang", "Chevrolet Silverado", "Volkswagen Golf", "Tesla Model S", "Nissan Altima", 
          "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4", "Hyundai Sonata","Kia Optima", "Subaru Outback", "Mazda3", "Lexus RX",
          "Jeep Wrangler", "Ram 1500", "Ford F-150", "Chevrolet Equinox", "Toyota RAV4"]
for elemento in car_ls:
    print(elemento)
    time.sleep(0)

search_car = input()
os.system("cls")

def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El elemento {elemento} se encuentra en la posición {lista.index(elemento)}."
    else: 
        return f"El elemento {elemento} no está presente en la lista."

resultado_busqueda = buscar_elemento(car_ls, search_car)
print(resultado_busqueda)
