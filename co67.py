print("================================")
print("            CO-67")
print("     DIAGNOSTIC AUTOMOBILE")
print("================================")
print()

codes = {
    "P0300": "Ratés d'allumage aléatoires détectés.",
    "P0301": "Raté d'allumage détecté sur le cylindre 1.",
    "P0420": "Efficacité du système catalyseur insuffisante."
}

while True:
    print()
    print("1. Lire un code défaut")
    print("2. Quitter")
    print()

    choix = input("Votre choix : ")

    if choix == "1":
        code = input("Entrez un code défaut OBD-II : ").upper()

        if code in codes:
            print()
            print("Code :", code)
            print("Description :", codes[code])
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
