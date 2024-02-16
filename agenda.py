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
    pass

def veure_contactes():
    pass

def eliminar_contacte():
    pass

def cercar_contacte():
    pass
 
def desar_contactes():
    pass

def carregar_contactes():
    pass



while True:
    print("\nQuè vols fer?")
    print("1. Afegir contacte")
    print("2. Veure contactes")
    print("3. Eliminar contacte")
    print("4. Cercar contacte")
    print("5. Desar contactes en un fitxer")
    print("6. Carregar contactes des d'un fitxer")
    print("7. Sortir")

    opcio = input("Selecciona una opció (1-7): ")

    if opcio == "1":
        nom = input("Introdueix el nom del contacte: ")
        telefon = input("Introdueix el telèfon del contacte: ")
        afegir_contacte(agenda, nom, telefon)
    elif opcio == "2":
        veure_contactes(agenda)
    elif opcio == "3":
        nom = input("Introdueix el nom del contacte que vols eliminar: ")
        eliminar_contacte(agenda, nom)
    elif opcio == "4":
        nom = input("Introdueix el nom del contacte que vols cercar: ")
        cercar_contacte(agenda, nom)
    elif opcio == "5":
        nom_fitxer = input("Introdueix el nom del fitxer en què vols desar els contactes: ")
        desar_contactes(agenda, nom_fitxer)
    elif opcio == "6":
        nom_fitxer = input("Introdueix el nom del fitxer del qual vols carregar els contactes: ")
        agenda = carregar_contactes(nom_fitxer)
    elif opcio == "7":
        print("Gràcies per utilitzar l'aplicació d'agenda de contactes. Adeu!")
        break
    else:
        print("Opció no vàlida. Si us plau, selecciona una opció vàlida (1-7).")