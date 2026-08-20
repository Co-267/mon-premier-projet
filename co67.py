from codes_obd import codes
from couleurs import titre, succes, attention, danger, information, important

def afficher_separateur():
    print("================================")


def afficher_titre():
    afficher_separateur()
    print(titre("            CO-67"))
    print(titre("     DIAGNOSTIC AUTOMOBILE"))
    afficher_separateur()


def afficher_menu():
    print()
    print("1. Lire un code défaut")
    print("2. Afficher les codes disponibles")
    print("3. Quitter")
    print()


def afficher_conclusion(information, numero):
    if "conclusion" not in information:
        return

    conclusions = information["conclusion"]

    if numero not in conclusions:
        return

    conclusion = conclusions[numero]

    print()
    afficher_separateur()
    print("       CONCLUSION CO-67")
    afficher_separateur()

    print()
    print("Orientation principale :")
    print("- " + conclusion["orientation_principale"])

    print()
    print("Niveau d'attention :")
    print(conclusion["niveau_attention"])

    print()
    print("A controler :")

    for element in conclusion["a_controler"]:
        print("- " + element)

    print()
    print("IMPORTANT :")
    print("Cette orientation est une aide au diagnostic.")
    print("Elle ne remplace pas les mesures et controles")
    print("effectues sur le vehicule.")


def afficher_code(information, code):
    print()
    afficher_separateur()
    print("         RESULTAT CO-67")
    afficher_separateur()

    print()
    print("Code :", code)
    print("Nom :", information["nom"])

    print()
    print("Description :")
    print(information["description"])

    print()
    print("Causes possibles :")

    for cause in information["causes_possibles"]:
        print("- " + cause)

    print()
    print("Controles recommandes :")

    for controle in information["controles_recommandes"]:
        print("- " + controle)

    if "symptomes_possibles" not in information:
        return

    print()
    print("Symptomes possibles :")

    for numero, symptome in enumerate(
        information["symptomes_possibles"],
        start=1
    ):
        print(str(numero) + " - " + symptome)

    print()

    choix_symptome = input(
        "Entrez le numero du symptome constate (0 pour continuer) : "
    )

    if not choix_symptome.isdigit():
        print()
        print("Entree invalide.")
        return

    numero = int(choix_symptome)

    if numero == 0:
        return

    if numero < 1 or numero > len(
        information["symptomes_possibles"]
    ):
        print()
        print("Numero de symptome invalide.")
        return

    symptome_choisi = information[
        "symptomes_possibles"
    ][numero - 1]

    print()
    afficher_separateur()
    print("       ORIENTATION CO-67")
    afficher_separateur()

    print()
    print("Symptome selectionne :")
    print("- " + symptome_choisi)

    if "orientations" not in information:
        print()
        print("Aucune orientation disponible.")
        return

    orientations = information["orientations"]

    if numero not in orientations:
        print()
        print("Aucune orientation disponible.")
        return

    orientation = orientations[numero]

    print()

    if isinstance(orientation, dict):

        if "priorite_1" in orientation:
            print("PRIORITE 1 - A VERIFIER EN PREMIER")

            for element in orientation["priorite_1"]:
                print("- " + element)

            print()

        if "priorite_2" in orientation:
            print("PRIORITE 2 - A VERIFIER ENSUITE")

            for element in orientation["priorite_2"]:
                print("- " + element)

            print()

        if "priorite_3" in orientation:
            print("PRIORITE 3 - SI LE DEFAUT PERSISTE")

            for element in orientation["priorite_3"]:
                print("- " + element)

    else:
        print("Orientation CO-67 :")

        for element in orientation:
            print("- " + element)

    afficher_conclusion(information, numero)

    print()
    print("Fin de l'orientation CO-67.")


def afficher_codes():
    print()
    afficher_separateur()
    print("        CODES DISPONIBLES")
    afficher_separateur()

    for code, information in codes.items():
        print(code + " - " + information["nom"])


afficher_titre()

while True:
    afficher_menu()

    choix = input("Votre choix : ")

    if choix == "1":

        code = input(
            "Entrez un code défaut OBD-II : "
        ).upper()

        if code in codes:
            afficher_code(codes[code], code)

        else:
            print()
            print("Code inconnu dans la base CO-67.")

    elif choix == "2":

        afficher_codes()

    elif choix == "3":

        print()
        print("Merci d'avoir utilisé CO-67.")
        break

    else:

        print()
        print("Choix invalide. Entrez 1, 2 ou 3.")
