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

code = input("Entrez un code défaut OBD-II : ").upper()

if code in codes:
    print()
    print("Code :", code)
    print("Description :", codes[code])
else:
    print()
    print("Code inconnu dans la base CO-67.")
