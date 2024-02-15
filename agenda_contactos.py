"""
/*
 * Es demana que desenvolupeu EN PARELLES una aplicació d’agenda de contactes en Python amb les
 * següents funcionalitats:
 * 1. Afegir contacte: Permet als usuaris afegir un nou contacte amb nom i número de telèfon.
 * 2. Veure contactes: Mostra tots els contactes guardats.
 * 3. Eliminar contacte: Permet als usuaris eliminar un contacte pel seu nom.
 * 4. Cerca de contactes: Permet als usuaris cercar un contacte pel seu nom.
 * 5. Guardar i carregar contactes en un fitxer: L’aplicació ha de permetre als usuaris desar els contactes en un
 * fitxer i carregar-los posteriorment.
 
 * afegir_contacte(nom, telèfon): Afegeix un contacte al diccionari.
 * veure_contactes(): Mostra tots els contactes guardats.
 * eliminar_contacte(nom): Elimina un contacte pel seu nom.
 * cercar_contacte(nom): Cerca un contacte pel seu nom.
 * desar_contactes(nom_fitxer): Guarda els contactes en un fitxer.
 * carregar_contactes(nom_fitxer): Carrega els contactes des d’un fitxer.
 */
 """



def afegir_contacte():
    print("a quin quieres añadir?")
    contacto = input()
    file = open("./agenda.txt", "w")
    file.write(contacto)

def eliminar_contacte():
    pass


def veure_contactes():
    pass


def desar_contactes():
    pass

def carregar_contactes():
    pass

def cercar_contacte():
    pass



while-True:
    print("Que qu8ieres hacer?")
    print("1. afegir_contacte")
    print("2. eliminar_contacte")
    print("3. veure_contactes")
    print("4. desar_contactes")
    print("5. carregar_contactes")
    print("6. carregar_contactes")
    print("7. salir")

    opcion = int(input())
    if opcion == "1":
        afegir_contacte()
    elif opcion == "2":
        eliminar_contacte()
    elif opcion == "3":
        veure_contactes()
    elif opcion == "4":
        desar_contactes()
    elif opcion == "5":
        carregar_contactes()
    elif opcion == "6":
        cercar_contacte()
    else:
        opcion == "7"
        break

