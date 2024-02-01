"""
/*
 * Haz un Progama que te reparta una canitdad dada X de dinero
 * te imprima la cantidad de billetes necesarios
 */
 """

def repartir_dinero(cantidad):
    billetes = [50, 20, 10, 5, 2, 1]  
    cantidades_billetes = {}  

    for billete in billetes:
        if cantidad >= billete:
            cant_billetes = cantidad // billete
            cantidad -= cant_billetes * billete
            cantidades_billetes[billete] = cant_billetes

    for billete, cantidad in cantidades_billetes.items():
        print(f"Billetes de {billete}:", cantidad)

cantidad_dinero = int(input("Ingrese la cantidad de dinero a repartir: "))
repartir_dinero(cantidad_dinero)

