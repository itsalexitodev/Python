"""
/*
 * Es demana que desenvolupeu EN PARELLES una aplicaci� d�agenda de contactes en Python amb les
 * seg�ents funcionalitats:
 * 1. Afegir contacte: Permet als usuaris afegir un nou contacte amb nom i n�mero de tel�fon.
 * 2. Veure contactes: Mostra tots els contactes guardats.
 * 3. Eliminar contacte: Permet als usuaris eliminar un contacte pel seu nom.
 * 4. Cerca de contactes: Permet als usuaris cercar un contacte pel seu nom.
 * 5. Guardar i carregar contactes en un fitxer: L�aplicaci� ha de permetre als usuaris desar els contactes en un
 * fitxer i carregar-los posteriorment.
 
 * afegir_contacte(nom, tel�fon): Afegeix un contacte al diccionari.
 * veure_contactes(): Mostra tots els contactes guardats.
 * eliminar_contacte(nom): Elimina un contacte pel seu nom.
 * cercar_contacte(nom): Cerca un contacte pel seu nom.
 * desar_contactes(nom_fitxer): Guarda els contactes en un fitxer.
 * carregar_contactes(nom_fitxer): Carrega els contactes des d�un fitxer.
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
    print("\nQu� vols fer?")
    print("1. Afegir contacte")
    print("2. Veure contactes")
    print("3. Eliminar contacte")
    print("4. Cercar contacte")
    print("5. Desar contactes en un fitxer")
    print("6. Carregar contactes des d'un fitxer")
    print("7. Sortir")

    opcio = input("Selecciona una opci� (1-7): ")

    if opcio == "1":
        nom = input("Introdueix el nom del contacte: ")
        telefon = input("Introdueix el tel�fon del contacte: ")
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
        nom_fitxer = input("Introdueix el nom del fitxer en qu� vols desar els contactes: ")
        desar_contactes(agenda, nom_fitxer)
    elif opcio == "6":
        nom_fitxer = input("Introdueix el nom del fitxer del qual vols carregar els contactes: ")
        agenda = carregar_contactes(nom_fitxer)
    elif opcio == "7":
        print("Gr�cies per utilitzar l'aplicaci� d'agenda de contactes. Adeu!")
        break
    else:
        print("Opci� no v�lida. Si us plau, selecciona una opci� v�lida (1-7).")