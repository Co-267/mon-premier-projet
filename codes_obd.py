codes = {

    "P0300": {
        "nom": "Rates d'allumage aleatoires",
        "description": "Le calculateur detecte des rates d'allumage sur un ou plusieurs cylindres.",

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
                "priorite_1": ["Controler les bougies d'allumage."],
                "priorite_2": ["Verifier les bobines d'allumage."],
                "priorite_3": ["Verifier les injecteurs si le probleme persiste."]
            },
            2: {
                "priorite_1": ["Controler le systeme d'allumage."],
                "priorite_2": [
                    "Verifier les injecteurs.",
                    "Verifier l'alimentation en carburant."
                ],
                "priorite_3": ["Verifier la compression du moteur."]
            },
            3: {
                "priorite_1": ["Controler les bougies et les bobines."],
                "priorite_2": [
                    "Verifier les injecteurs.",
                    "Rechercher une prise d'air."
                ],
                "priorite_3": ["Verifier l'alimentation en carburant."]
            },
            4: {
                "priorite_1": ["Controler les bougies et les bobines."],
                "priorite_2": [
                    "Verifier les injecteurs.",
                    "Verifier la pression de carburant."
                ],
                "priorite_3": ["Verifier la compression du moteur."]
            },
            5: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Verifier les codes associes au P0300."],
                "priorite_3": ["Effectuer les controles d'allumage et d'injection."]
            },
            6: {
                "priorite_1": ["Verifier les rates d'allumage."],
                "priorite_2": [
                    "Controler l'allumage.",
                    "Verifier l'injection et l'alimentation en carburant."
                ],
                "priorite_3": ["Rechercher un probleme de combustion."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Systeme d'allumage et combustion",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougies d'allumage",
                    "Bobines d'allumage",
                    "Injecteurs"
                ]
            },
            2: {
                "orientation_principale": "Systeme d'allumage et alimentation en carburant",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougies",
                    "Bobines",
                    "Injecteurs",
                    "Alimentation en carburant"
                ]
            },
            3: {
                "orientation_principale": "Systeme d'allumage et injection",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougies",
                    "Bobines",
                    "Injecteurs",
                    "Prise d'air"
                ]
            },
            4: {
                "orientation_principale": "Allumage, injection et compression",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougies",
                    "Bobines",
                    "Injecteurs",
                    "Compression moteur"
                ]
            },
            5: {
                "orientation_principale": "Systeme moteur a diagnostiquer",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Tous les codes défaut",
                    "Systeme d'allumage",
                    "Systeme d'injection"
                ]
            },
            6: {
                "orientation_principale": "Combustion et alimentation moteur",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Allumage",
                    "Injection",
                    "Alimentation en carburant"
                ]
            }
        }
    },


    "P0301": {
        "nom": "Rate d'allumage du cylindre 1",
        "description": "Le calculateur detecte un rate d'allumage sur le cylindre 1.",

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
                "priorite_1": ["Controler la bougie du cylindre 1."],
                "priorite_2": ["Verifier la bobine d'allumage."],
                "priorite_3": ["Verifier l'injecteur du cylindre 1."]
            },
            2: {
                "priorite_1": [
                    "Controler la bougie du cylindre 1.",
                    "Verifier la bobine d'allumage."
                ],
                "priorite_2": ["Verifier l'injecteur du cylindre 1."],
                "priorite_3": ["Verifier la compression du cylindre 1."]
            },
            3: {
                "priorite_1": ["Controler la bougie et la bobine du cylindre 1."],
                "priorite_2": ["Verifier l'injecteur du cylindre 1."],
                "priorite_3": ["Verifier le cablage."]
            },
            4: {
                "priorite_1": ["Controler la bougie et la bobine."],
                "priorite_2": [
                    "Verifier l'injecteur.",
                    "Verifier la pression de carburant."
                ],
                "priorite_3": ["Verifier la compression du cylindre 1."]
            },
            5: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Verifier les codes associes au P0301."],
                "priorite_3": ["Controler le systeme d'allumage et d'injection."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Circuit d'allumage du cylindre 1",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 1",
                    "Bobine d'allumage",
                    "Injecteur du cylindre 1"
                ]
            },
            2: {
                "orientation_principale": "Allumage et injection du cylindre 1",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 1",
                    "Bobine d'allumage",
                    "Injecteur du cylindre 1",
                    "Compression du cylindre 1"
                ]
            },
            3: {
                "orientation_principale": "Allumage et injection du cylindre 1",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 1",
                    "Bobine",
                    "Injecteur",
                    "Cablage"
                ]
            },
            4: {
                "orientation_principale": "Allumage, injection et compression",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie",
                    "Bobine",
                    "Injecteur",
                    "Compression"
                ]
            },
            5: {
                "orientation_principale": "Rate d'allumage du cylindre 1",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Tous les codes défaut",
                    "Allumage",
                    "Injection"
                ]
            }
        }
    },


    "P0420": {
        "nom": "Efficacite du catalyseur insuffisante",
        "description": "Le calculateur detecte une efficacite du catalyseur inferieure au seuil attendu.",

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
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": [
                    "Verifier les sondes lambda.",
                    "Verifier les parametres lies au melange air-carburant."
                ],
                "priorite_3": ["Controler le catalyseur si les autres controles sont corrects."]
            },
            2: {
                "priorite_1": ["Verifier les problemes de combustion."],
                "priorite_2": [
                    "Verifier les sondes lambda.",
                    "Rechercher une restriction du systeme d'echappement."
                ],
                "priorite_3": ["Controler le catalyseur."]
            },
            3: {
                "priorite_1": ["Verifier le melange air-carburant."],
                "priorite_2": [
                    "Controler les sondes lambda.",
                    "Verifier les problemes de combustion."
                ],
                "priorite_3": ["Controler le catalyseur."]
            },
            4: {
                "priorite_1": ["Rechercher une fuite dans l'echappement."],
                "priorite_2": ["Verifier les sondes lambda."],
                "priorite_3": ["Verifier le fonctionnement du catalyseur."]
            },
            5: {
                "priorite_1": ["Verifier les rates d'allumage."],
                "priorite_2": [
                    "Controler l'injection et le melange air-carburant.",
                    "Verifier les sondes lambda."
                ],
                "priorite_3": ["Controler le catalyseur."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Systeme antipollution et controle du catalyseur",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Codes défaut associes",
                    "Sondes lambda",
                    "Melange air-carburant",
                    "Catalyseur"
                ]
            },
            2: {
                "orientation_principale": "Combustion et systeme d'echappement",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Combustion",
                    "Sondes lambda",
                    "Echappement",
                    "Catalyseur"
                ]
            },
            3: {
                "orientation_principale": "Melange air-carburant",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Melange air-carburant",
                    "Sondes lambda",
                    "Combustion",
                    "Catalyseur"
                ]
            },
            4: {
                "orientation_principale": "Systeme d'echappement",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Fuites d'echappement",
                    "Sondes lambda",
                    "Catalyseur"
                ]
            },
            5: {
                "orientation_principale": "Combustion et systeme antipollution",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Allumage",
                    "Injection",
                    "Sondes lambda",
                    "Catalyseur"
                ]
            }
        }
    },


    "P0171": {
        "nom": "Melange trop pauvre",
        "description": "Le calculateur detecte un melange air-carburant trop pauvre.",

        "causes_possibles": [
            "Prise d'air",
            "Fuite de durite d'admission",
            "Pression de carburant insuffisante",
            "Injecteur encrasse",
            "Debitmetre ou capteur de pression defectueux",
            "Sonde lambda"
        ],

        "controles_recommandes": [
            "Rechercher une prise d'air",
            "Verifier les durites d'admission",
            "Verifier la pression de carburant",
            "Verifier les injecteurs",
            "Verifier les valeurs du debitmetre",
            "Verifier la sonde lambda"
        ],

        "symptomes_possibles": [
            "Ralenti instable",
            "Perte de puissance",
            "A-coups a l'acceleration",
            "Demarrage difficile",
            "Voyant moteur allume",
            "Consommation anormale"
        ],

        "orientations": {
            1: {
                "priorite_1": ["Rechercher une prise d'air."],
                "priorite_2": ["Verifier les durites d'admission.", "Verifier le debitmetre."],
                "priorite_3": ["Verifier les injecteurs et la pression de carburant."]
            },
            2: {
                "priorite_1": ["Verifier la pression de carburant."],
                "priorite_2": ["Verifier les injecteurs."],
                "priorite_3": ["Verifier la sonde lambda."]
            },
            3: {
                "priorite_1": ["Rechercher une prise d'air."],
                "priorite_2": ["Verifier l'alimentation en carburant."],
                "priorite_3": ["Verifier les injecteurs."]
            },
            4: {
                "priorite_1": ["Verifier l'alimentation en carburant."],
                "priorite_2": ["Verifier les injecteurs."],
                "priorite_3": ["Verifier la pression de carburant."]
            },
            5: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Rechercher la cause du melange pauvre."],
                "priorite_3": ["Verifier admission, injection et capteurs."]
            },
            6: {
                "priorite_1": ["Verifier les valeurs de correction de carburant."],
                "priorite_2": ["Verifier admission et injection."],
                "priorite_3": ["Verifier les sondes et capteurs."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Admission d'air et melange air-carburant",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Prise d'air",
                    "Durites d'admission",
                    "Debitmetre",
                    "Injecteurs"
                ]
            },
            2: {
                "orientation_principale": "Alimentation en carburant",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Pression de carburant",
                    "Injecteurs",
                    "Sonde lambda"
                ]
            },
            3: {
                "orientation_principale": "Admission et alimentation moteur",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Prise d'air",
                    "Alimentation carburant",
                    "Injecteurs"
                ]
            },
            4: {
                "orientation_principale": "Alimentation et injection",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Pompe et pression carburant",
                    "Injecteurs",
                    "Filtration carburant"
                ]
            },
            5: {
                "orientation_principale": "Melange air-carburant",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Codes associes",
                    "Admission",
                    "Injection",
                    "Capteurs"
                ]
            },
            6: {
                "orientation_principale": "Correction du melange",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Corrections carburant",
                    "Admission",
                    "Injection",
                    "Sondes"
                ]
            }
        }
    },


    "P0172": {
        "nom": "Melange trop riche",
        "description": "Le calculateur detecte un melange air-carburant trop riche.",

        "causes_possibles": [
            "Injecteur qui fuit",
            "Pression de carburant trop elevee",
            "Filtre a air encrasse",
            "Sonde lambda defectueuse",
            "Capteur de temperature defectueux",
            "Debitmetre defectueux"
        ],

        "controles_recommandes": [
            "Verifier les injecteurs",
            "Verifier la pression de carburant",
            "Verifier le filtre a air",
            "Verifier la sonde lambda",
            "Verifier le capteur de temperature",
            "Verifier le debitmetre"
        ],

        "symptomes_possibles": [
            "Consommation de carburant augmentee",
            "Fumee noire",
            "Ralenti instable",
            "Odeur de carburant",
            "Perte de puissance",
            "Voyant moteur allume"
        ],

        "orientations": {
            1: {
                "priorite_1": ["Verifier les injecteurs."],
                "priorite_2": ["Verifier la pression de carburant."],
                "priorite_3": ["Verifier les sondes et capteurs."]
            },
            2: {
                "priorite_1": ["Verifier le systeme d'admission d'air."],
                "priorite_2": ["Verifier les injecteurs."],
                "priorite_3": ["Verifier les capteurs."]
            },
            3: {
                "priorite_1": ["Verifier le ralenti et l'injection."],
                "priorite_2": ["Verifier les injecteurs."],
                "priorite_3": ["Verifier la sonde lambda."]
            },
            4: {
                "priorite_1": ["Verifier les injecteurs."],
                "priorite_2": ["Rechercher une fuite de carburant."],
                "priorite_3": ["Verifier la pression de carburant."]
            },
            5: {
                "priorite_1": ["Verifier l'injection."],
                "priorite_2": ["Verifier le filtre a air."],
                "priorite_3": ["Verifier les capteurs moteur."]
            },
            6: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Verifier l'injection et les capteurs."],
                "priorite_3": ["Verifier le systeme de gestion moteur."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Injection et alimentation en carburant",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Injecteurs",
                    "Pression de carburant",
                    "Sondes"
                ]
            },
            2: {
                "orientation_principale": "Admission d'air et injection",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Filtre a air",
                    "Injecteurs",
                    "Capteurs"
                ]
            },
            3: {
                "orientation_principale": "Injection et gestion du ralenti",
                "niveau_attention": "MOYEN A ELEVE",
                "a_controler": [
                    "Injecteurs",
                    "Sonde lambda",
                    "Gestion moteur"
                ]
            },
            4: {
                "orientation_principale": "Injection et circuit carburant",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Injecteurs",
                    "Fuites carburant",
                    "Pression carburant"
                ]
            },
            5: {
                "orientation_principale": "Injection et admission d'air",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Injection",
                    "Filtre a air",
                    "Capteurs"
                ]
            },
            6: {
                "orientation_principale": "Gestion moteur",
                "niveau_attention": "MOYEN",
                "a_controler": [
                    "Codes associes",
                    "Injection",
                    "Capteurs"
                ]
            }
        }
    },


    "P0201": {
        "nom": "Circuit injecteur cylindre 1",
        "description": "Le calculateur detecte un probleme sur le circuit de l'injecteur du cylindre 1.",

        "causes_possibles": [
            "Injecteur du cylindre 1 defectueux",
            "Cablage de l'injecteur",
            "Connecteur endommage",
            "Probleme d'alimentation electrique",
            "Probleme de calculateur"
        ],

        "controles_recommandes": [
            "Verifier l'injecteur du cylindre 1",
            "Verifier le connecteur",
            "Verifier le cablage",
            "Verifier l'alimentation electrique",
            "Verifier la commande de l'injecteur"
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
                "priorite_1": ["Verifier l'injecteur du cylindre 1."],
                "priorite_2": ["Verifier le connecteur et le cablage."],
                "priorite_3": ["Verifier la commande electrique."]
            },
            2: {
                "priorite_1": ["Verifier l'injecteur du cylindre 1."],
                "priorite_2": ["Verifier la pression de carburant."],
                "priorite_3": ["Verifier le cablage."]
            },
            3: {
                "priorite_1": ["Verifier l'injecteur du cylindre 1."],
                "priorite_2": ["Verifier le cablage."],
                "priorite_3": ["Verifier la commande electrique."]
            },
            4: {
                "priorite_1": ["Verifier l'injecteur."],
                "priorite_2": ["Verifier l'alimentation electrique."],
                "priorite_3": ["Verifier le cablage."]
            },
            5: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Verifier le circuit de l'injecteur."],
                "priorite_3": ["Verifier les autres systemes moteur."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Injecteur du cylindre 1",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Injecteur cylindre 1",
                    "Connecteur",
                    "Cablage"
                ]
            },
            2: {
                "orientation_principale": "Injection et alimentation carburant",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Injecteur",
                    "Pression carburant",
                    "Cablage"
                ]
            },
            3: {
                "orientation_principale": "Circuit injecteur cylindre 1",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Injecteur",
                    "Cablage",
                    "Commande electrique"
                ]
            },
            4: {
                "orientation_principale": "Injection et alimentation electrique",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Injecteur",
                    "Alimentation",
                    "Cablage"
                ]
            },
            5: {
                "orientation_principale": "Circuit d'injection",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Codes associes",
                    "Injecteur",
                    "Cablage"
                ]
            }
        }
    },


    "P0302": {
        "nom": "Rate d'allumage du cylindre 2",
        "description": "Le calculateur detecte un rate d'allumage sur le cylindre 2.",

        "causes_possibles": [
            "Bougie du cylindre 2",
            "Bobine d'allumage",
            "Injecteur du cylindre 2",
            "Probleme de cablage",
            "Probleme de compression"
        ],

        "controles_recommandes": [
            "Verifier la bougie du cylindre 2",
            "Verifier la bobine d'allumage",
            "Verifier l'injecteur du cylindre 2",
            "Verifier le cablage",
            "Verifier la compression du cylindre 2"
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
                "priorite_1": ["Controler la bougie du cylindre 2."],
                "priorite_2": ["Verifier la bobine d'allumage."],
                "priorite_3": ["Verifier l'injecteur du cylindre 2."]
            },
            2: {
                "priorite_1": ["Controler la bougie et la bobine du cylindre 2."],
                "priorite_2": ["Verifier l'injecteur du cylindre 2."],
                "priorite_3": ["Verifier la compression du cylindre 2."]
            },
            3: {
                "priorite_1": ["Controler la bougie et la bobine du cylindre 2."],
                "priorite_2": ["Verifier l'injecteur du cylindre 2."],
                "priorite_3": ["Verifier le cablage."]
            },
            4: {
                "priorite_1": ["Controler l'allumage du cylindre 2."],
                "priorite_2": ["Verifier l'injection."],
                "priorite_3": ["Verifier la compression."]
            },
            5: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Verifier les codes associes au P0302."],
                "priorite_3": ["Controler l'allumage et l'injection."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Circuit d'allumage du cylindre 2",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 2",
                    "Bobine d'allumage",
                    "Injecteur du cylindre 2"
                ]
            },
            2: {
                "orientation_principale": "Allumage et injection du cylindre 2",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie",
                    "Bobine",
                    "Injecteur",
                    "Compression"
                ]
            },
            3: {
                "orientation_principale": "Allumage et injection",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie",
                    "Bobine",
                    "Injecteur",
                    "Cablage"
                ]
            },
            4: {
                "orientation_principale": "Allumage et injection du cylindre 2",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Allumage",
                    "Injection",
                    "Compression"
                ]
            },
            5: {
                "orientation_principale": "Rate d'allumage du cylindre 2",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Codes associes",
                    "Allumage",
                    "Injection"
                ]
            }
        }
    },


    "P0303": {
        "nom": "Rate d'allumage du cylindre 3",
        "description": "Le calculateur detecte un rate d'allumage sur le cylindre 3.",

        "causes_possibles": [
            "Bougie du cylindre 3",
            "Bobine d'allumage",
            "Injecteur du cylindre 3",
            "Probleme de cablage",
            "Probleme de compression"
        ],

        "controles_recommandes": [
            "Verifier la bougie du cylindre 3",
            "Verifier la bobine d'allumage",
            "Verifier l'injecteur du cylindre 3",
            "Verifier le cablage",
            "Verifier la compression du cylindre 3"
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
                "priorite_1": ["Controler la bougie du cylindre 3."],
                "priorite_2": ["Verifier la bobine d'allumage."],
                "priorite_3": ["Verifier l'injecteur du cylindre 3."]
            },
            2: {
                "priorite_1": ["Controler la bougie et la bobine du cylindre 3."],
                "priorite_2": ["Verifier l'injecteur du cylindre 3."],
                "priorite_3": ["Verifier la compression du cylindre 3."]
            },
            3: {
                "priorite_1": ["Controler la bougie et la bobine du cylindre 3."],
                "priorite_2": ["Verifier l'injecteur du cylindre 3."],
                "priorite_3": ["Verifier le cablage."]
            },
            4: {
                "priorite_1": ["Controler l'allumage du cylindre 3."],
                "priorite_2": ["Verifier l'injection."],
                "priorite_3": ["Verifier la compression."]
            },
            5: {
                "priorite_1": ["Lire tous les codes défaut presents."],
                "priorite_2": ["Verifier les codes associes au P0303."],
                "priorite_3": ["Controler l'allumage et l'injection."]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Circuit d'allumage du cylindre 3",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 3",
                    "Bobine d'allumage",
                    "Injecteur du cylindre 3"
                ]
            },
            2: {
                "orientation_principale": "Allumage et injection du cylindre 3",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie",
                    "Bobine",
                    "Injecteur",
                    "Compression"
                ]
            },
            3: {
                "orientation_principale": "Allumage et injection",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie",
                    "Bobine",
                    "Injecteur",
                    "Cablage"
                ]
            },
            4: {
                "orientation_principale": "Allumage et injection du cylindre 3",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Allumage",
                    "Injection",
                    "Compression"
                ]
            },
            5: {
                "orientation_principale": "Rate d'allumage du cylindre 3",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Codes associes",
                    "Allumage",
                    "Injection"
                ]
            }
        }
    }

,

    "P0304": {
        "nom": "Rate d'allumage du cylindre 4",
        "description": "Le calculateur detecte un rate d'allumage sur le cylindre 4.",

        "causes_possibles": [
            "Bougie du cylindre 4",
            "Bobine d'allumage",
            "Injecteur du cylindre 4",
            "Probleme de cablage",
            "Probleme de compression"
        ],

        "controles_recommandes": [
            "Verifier la bougie du cylindre 4",
            "Verifier la bobine d'allumage",
            "Verifier l'injecteur du cylindre 4",
            "Verifier le cablage",
            "Verifier la compression du cylindre 4"
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
                "priorite_1": ["Controler la bougie du cylindre 4."],
                "priorite_2": ["Verifier la bobine d'allumage."],
                "priorite_3": ["Verifier l'injecteur du cylindre 4."]
            },
            2: {
                "priorite_1": [
                    "Controler la bougie et la bobine du cylindre 4."
                ],
                "priorite_2": [
                    "Verifier l'injecteur du cylindre 4."
                ],
                "priorite_3": [
                    "Verifier la compression du cylindre 4."
                ]
            },
            3: {
                "priorite_1": [
                    "Controler la bougie et la bobine du cylindre 4."
                ],
                "priorite_2": [
                    "Verifier l'injecteur du cylindre 4."
                ],
                "priorite_3": [
                    "Verifier le cablage."
                ]
            },
            4: {
                "priorite_1": [
                    "Controler l'allumage du cylindre 4."
                ],
                "priorite_2": [
                    "Verifier l'injection."
                ],
                "priorite_3": [
                    "Verifier la compression du cylindre 4."
                ]
            },
            5: {
                "priorite_1": [
                    "Lire tous les codes défaut presents."
                ],
                "priorite_2": [
                    "Verifier les codes associes au P0304."
                ],
                "priorite_3": [
                    "Controler l'allumage et l'injection."
                ]
            }
        },

        "conclusion": {
            1: {
                "orientation_principale": "Circuit d'allumage du cylindre 4",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 4",
                    "Bobine d'allumage",
                    "Injecteur du cylindre 4"
                ]
            },
            2: {
                "orientation_principale": "Allumage et injection du cylindre 4",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 4",
                    "Bobine d'allumage",
                    "Injecteur du cylindre 4",
                    "Compression du cylindre 4"
                ]
            },
            3: {
                "orientation_principale": "Allumage et injection du cylindre 4",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Bougie du cylindre 4",
                    "Bobine",
                    "Injecteur",
                    "Cablage"
                ]
            },
            4: {
                "orientation_principale": "Allumage, injection et compression",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Allumage",
                    "Injection",
                    "Compression"
                ]
            },
            5: {
                "orientation_principale": "Rate d'allumage du cylindre 4",
                "niveau_attention": "ELEVE",
                "a_controler": [
                    "Codes associes",
                    "Allumage",
                    "Injection"
                ]
            }
        }
    }

}
