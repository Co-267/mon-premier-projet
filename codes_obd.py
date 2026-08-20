codes = {
    "P0300": {
        "nom": "Ratés d'allumage aléatoires",
        "description": "Le calculateur détecte des ratés d'allumage sur un ou plusieurs cylindres.",

        "causes_possibles": [
            "Bougies d'allumage",
            "Bobines d'allumage",
            "Injecteurs",
            "Probleme d'alimentation en carburant",
            "Prise d'air",
            "Probleme mecanique du moteur",
            "Probleme de cablage ou d'alimentation electrique"
        ],

        "controles_recommandes": [
            "Verifier l'etat des bougies d'allumage",
            "Verifier le fonctionnement des bobines",
            "Verifier les injecteurs",
            "Verifier l'alimentation en carburant",
            "Rechercher une prise d'air",
            "Verifier la compression du moteur",
            "Verifier le cablage et les connexions electriques"
        ],

        "symptomes_possibles": [
            "Moteur qui tremble au ralenti",
            "Perte de puissance",
            "A-coups a l'acceleration",
            "Demarrage difficile",
            "Voyant moteur allume",
            "Consommation de carburant augmentee"
        ],

        "orientations": {
            1: {
                "priorite_1": [
                    "Controler l'etat des bougies d'allumage."
                ],
                "priorite_2": [
                    "Controler le fonctionnement des bobines d'allumage."
                ],
                "priorite_3": [
                    "Verifier les injecteurs si le probleme persiste."
                ]
            },

            2: {
                "priorite_1": [
                    "Controler le systeme d'allumage."
                ],
                "priorite_2": [
                    "Verifier les injecteurs.",
                    "Verifier l'alimentation en carburant."
                ],
                "priorite_3": [
                    "Verifier la compression du moteur."
                ]
            },

            3: {
                "priorite_1": [
                    "Controler les bougies et les bobines."
                ],
                "priorite_2": [
                    "Verifier les injecteurs.",
                    "Rechercher une prise d'air."
                ],
                "priorite_3": [
                    "Verifier l'alimentation en carburant."
                ]
            },

            4: {
                "priorite_1": [
                    "Controler les bougies et les bobines."
                ],
                "priorite_2": [
                    "Verifier les injecteurs.",
                    "Verifier la pression de carburant."
                ],
                "priorite_3": [
                    "Verifier la compression du moteur."
                ]
            },

            5: {
                "priorite_1": [
                    "Lire et noter tous les codes défaut presents."
                ],
                "priorite_2": [
                    "Verifier si d'autres codes sont associes au P0300."
                ],
                "priorite_3": [
                    "Effectuer les controles d'allumage et d'injection."
                ]
            },

            6: {
                "priorite_1": [
                    "Verifier les rates d'allumage."
                ],
                "priorite_2": [
                    "Controler le systeme d'allumage.",
                    "Verifier l'injection et l'alimentation en carburant."
                ],
                "priorite_3": [
                    "Rechercher un probleme de combustion."
                ]
            }
        }
    },

    "P0301": {
        "nom": "Raté d'allumage du cylindre 1",
        "description": "Le calculateur détecte un raté d'allumage sur le cylindre 1.",

        "causes_possibles": [
            "Bougie du cylindre 1",
            "Bobine d'allumage",
            "Injecteur du cylindre 1",
            "Probleme de cablage",
            "Probleme de compression"
        ],

        "controles_recommandes": [
            "Verifier la bougie du cylindre 1",
            "Verifier la bobine d'allumage",
            "Verifier l'injecteur du cylindre 1",
            "Verifier le cablage",
            "Verifier la compression du cylindre 1"
        ],

        "symptomes_possibles": [
            "Moteur qui tremble au ralenti",
            "Perte de puissance",
            "A-coups a l'acceleration",
            "Demarrage difficile",
            "Voyant moteur allume"
        ],

        "orientations": {
            1: {
                "priorite_1": [
                    "Controler la bougie du cylindre 1."
                ],
                "priorite_2": [
                    "Verifier la bobine d'allumage."
                ],
                "priorite_3": [
                    "Verifier l'injecteur du cylindre 1."
                ]
            },

            2: {
                "priorite_1": [
                    "Controler la bougie du cylindre 1.",
                    "Verifier la bobine d'allumage."
                ],
                "priorite_2": [
                    "Verifier l'injecteur du cylindre 1."
                ],
                "priorite_3": [
                    "Verifier la compression du cylindre 1."
                ]
            },

            3: {
                "priorite_1": [
                    "Controler la bougie et la bobine du cylindre 1."
                ],
                "priorite_2": [
                    "Verifier l'injecteur du cylindre 1."
                ],
                "priorite_3": [
                    "Verifier le cablage."
                ]
            },

            4: {
                "priorite_1": [
                    "Controler la bougie et la bobine."
                ],
                "priorite_2": [
                    "Verifier l'injecteur.",
                    "Verifier la pression de carburant."
                ],
                "priorite_3": [
                    "Verifier la compression du cylindre 1."
                ]
            },

            5: {
                "priorite_1": [
                    "Lire tous les codes défaut presents."
                ],
                "priorite_2": [
                    "Verifier si d'autres codes sont associes au P0301."
                ],
                "priorite_3": [
                    "Controler le systeme d'allumage et d'injection."
                ]
            }
        }
    },

    "P0420": {
        "nom": "Efficacité du catalyseur insuffisante",
        "description": "Le calculateur détecte une efficacité du catalyseur inférieure au seuil attendu.",

        "causes_possibles": [
            "Catalyseur degrade",
            "Sonde lambda",
            "Fuite dans l'echappement",
            "Probleme de combustion",
            "Probleme de melange air-carburant"
        ],

        "controles_recommandes": [
            "Verifier les sondes lambda",
            "Rechercher une fuite dans l'echappement",
            "Verifier les problemes de combustion",
            "Verifier le melange air-carburant",
            "Effectuer un controle du catalyseur"
        ],

        "symptomes_possibles": [
            "Voyant moteur allume",
            "Perte de puissance",
            "Consommation de carburant augmentee",
            "Odeur inhabituelle a l'echappement",
            "Moteur qui fonctionne de maniere irreguliere"
        ],

        "orientations": {
            1: {
                "priorite_1": [
                    "Lire tous les codes défaut presents."
                ],
                "priorite_2": [
                    "Verifier les sondes lambda.",
                    "Verifier les parametres lies au melange air-carburant."
                ],
                "priorite_3": [
                    "Controler le catalyseur si les autres controles sont corrects."
                ]
            },

            2: {
                "priorite_1": [
                    "Verifier les problemes de combustion."
                ],
                "priorite_2": [
                    "Verifier les sondes lambda.",
                    "Rechercher une restriction du systeme d'echappement."
                ],
                "priorite_3": [
                    "Controler le catalyseur."
                ]
            },

            3: {
                "priorite_1": [
                    "Verifier le melange air-carburant."
                ],
                "priorite_2": [
                    "Controler les sondes lambda.",
                    "Verifier les problemes de combustion."
                ],
                "priorite_3": [
                    "Controler le catalyseur."
                ]
            },

            4: {
                "priorite_1": [
                    "Rechercher une fuite dans l'echappement."
                ],
                "priorite_2": [
                    "Verifier les sondes lambda."
                ],
                "priorite_3": [
                    "Verifier le fonctionnement du catalyseur."
                ]
            },

            5: {
                "priorite_1": [
                    "Verifier les rates d'allumage."
                ],
                "priorite_2": [
                    "Controler l'injection et le melange air-carburant.",
                    "Verifier les sondes lambda."
                ],
                "priorite_3": [
                    "Controler le catalyseur."
                ]
            }
        }
    }
}
