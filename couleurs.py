# ============================================
# CO-67 - AFFICHAGE COULEUR
# ============================================

RESET = "\033[0m"

ROUGE = "\033[91m"
VERT = "\033[92m"
JAUNE = "\033[93m"
BLEU = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GRAS = "\033[1m"


def titre(texte):
    return f"{GRAS}{CYAN}{texte}{RESET}"


def succes(texte):
    return f"{VERT}{texte}{RESET}"


def attention(texte):
    return f"{JAUNE}{texte}{RESET}"


def danger(texte):
    return f"{ROUGE}{texte}{RESET}"


def information(texte):
    return f"{BLEU}{texte}{RESET}"


def important(texte):
    return f"{MAGENTA}{texte}{RESET}"
