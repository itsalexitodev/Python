# -*- coding: iso-8859-1 -*-

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


def afegir_contacte(agenda, nom, telefon):
    agenda[nom] = telefon

def veure_contactes(agenda):
    if not agenda:
        print("\nNo hi ha cap contacte a l'agenda.\n")
    else:
        for nom, telefon in agenda.items():
            print(f'\nnombre: {nom}\ntelefono: {telefon}\n')

def eliminar_contacte(agenda, nom):
    if nom in agenda:
        del agenda[nom]
        print(f"\nEl contacte {nom} s'ha eliminat. \n")
    else:
        print("\nAquest contacte no existeix a l'agenda. \n")

def cercar_contacte(agenda, nom):
    if nom in agenda:
        print(f'\nnombre: {nom}\ntelefono: {agenda[nom]}\n')
    else:
        print("Aquest contacte no existeix a l'agenda.")

def desar_contactes(agenda, agenda_txt):
    with open(agenda_txt, 'w') as file:
        for nom, telefon in agenda.items():
            file.write(f"{nom},{telefon}\n")
    print("\nEls contactes s'han desat correctament. \n")

def carregar_contactes(agenda, agenda_txt):
    try:
        with open(agenda_txt, 'r') as file:
            for line in file:
                nom, telefon = line.strip().split(',')
                agenda[nom] = telefon
        print("\nEls contactes s'han carregat correctament. \n")
        return agenda
    except FileNotFoundError:
        print("\nNo s'ha pogut trobar el fitxer d'agenda. \n")

agenda = {}

while True:
    print("\nQuè vols fer?\n")
    print("1. Afegir contacte")
    print("2. Veure contactes")
    print("3. Eliminar contacte")
    print("4. Cercar contacte")
    print("5. Desar contactes en un fitxer")
    print("6. Carregar contactes des d'un fitxer")
    print("7. Sortir")

    opcio = input("\nSelecciona una opció (1-7): \n")

    if opcio == "1":
        nom = input("\nIntrodueix el nom del contacte: \n")
        telefon = input("\nIntrodueix el telèfon del contacte: \n")
        afegir_contacte(agenda, nom, telefon)
    elif opcio == "2":
        veure_contactes(agenda)
    elif opcio == "3":
        nom = input("\nIntrodueix el nom del contacte que vols eliminar: \n")
        eliminar_contacte(agenda, nom)
    elif opcio == "4":
        nom = input("\nIntrodueix el nom del contacte que vols cercar: \n")
        cercar_contacte(agenda, nom)
    elif opcio == "5":
        agenda_txt = input("\nIntrodueix el nom del fitxer en què vols desar els contactes: \n")
        desar_contactes(agenda, agenda_txt)
    elif opcio == "6":
        agenda_txt = input("\nIntrodueix el nom del fitxer del qual vols carregar els contactes: \n")
        agenda = carregar_contactes(agenda, agenda_txt)
    elif opcio == "7":
        print("\nGràcies per utilitzar l'aplicació d'agenda de contactes. Adeu!\n")
        break
    else:
        print("\nOpció no vàlida. Si us plau, selecciona una opció vàlida (1-7).\n")
