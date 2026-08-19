from codes_obd import codes

print("================================")
print("            CO-67")
print("     DIAGNOSTIC AUTOMOBILE")
print("================================")

while True:
    print()
    print("1. Lire un code défaut")
    print("2. Quitter")
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

        else:
            print()
            print("Code inconnu dans la base CO-67.")

    elif choix == "2":
        print()
        print("Merci d'avoir utilisé CO-67.")
        break

    else:
        print()
        print("Choix invalide. Entrez 1 ou 2.")
