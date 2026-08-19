from codes_obd import codes

print("================================")
print("            CO-67")
print("     DIAGNOSTIC AUTOMOBILE")
print("================================")

while True:
    print()
    print("1. Lire un code défaut")
    print("2. Afficher les codes disponibles")
    print("3. Quitter")
    print()

    choix = input("Votre choix : ")

    if choix == "1":
        code = input("Entrez un code défaut OBD-II : ").upper()

        if code in codes:
            information = codes[code]

            print()
            print("Code :", code)
            print("Nom :", information["nom"])
            print("Description :", information["description"])

            print()
            print("Causes possibles :")
            for cause in information["causes_possibles"]:
                print("-", cause)

            print()
            print("Contrôles recommandés :")
            for controle in information["controles_recommandes"]:
                print("-", controle)

            if "symptomes_possibles" in information:
                print()
                print("Symptomes possibles :")

                for numero, symptome in enumerate(
                    information["symptomes_possibles"], start=1
                ):
                    print(numero, "-", symptome)

                print()
                choix_symptome = input(
                    "Entrez le numero du symptome constate (0 pour continuer) : "
                )

                if choix_symptome.isdigit():
                    numero = int(choix_symptome)

                    if 1 <= numero <= len(information["symptomes_possibles"]):
                        symptome_choisi = information["symptomes_possibles"][numero - 1]

                        print()
                        print("Symptome selectionne :")
                        print("-", symptome_choisi)

                        if "orientations" in information:
                            orientations = information["orientations"]

                            if numero in orientations:
                                print()
                                print("Orientation CO-67 :")

                                for orientation in orientations[numero]:
                                    print("-", orientation)

                    elif numero != 0:
                        print()
                        print("Numero de symptome invalide.")
                else:
                    print()
                    print("Entree invalide.")

        else:
            print()
            print("Code inconnu dans la base CO-67.")

    elif choix == "2":
        print()
        print("Codes disponibles :")

        for code, information in codes.items():
            print(code, "-", information["nom"])

    elif choix == "3":
        print()
        print("Merci d'avoir utilisé CO-67.")
        break

    else:
        print()
        print("Choix invalide. Entrez 1, 2 ou 3.")
