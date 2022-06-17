# même algorithme que solution_compteur.py sous forme récursive
def erase(cc, spaces=0):
    # cas d'arrêt
    if cc == "":
        # on regarde s'il reste des espaces lorsqu'on arrête
        if spaces > 1:
            return " "*spaces
        return ""
    # espace : on le compte
    if cc[0] == " ":
        return erase(cc[1:], spaces+1)
    # lettre : si on a compté plus d'un espace, on les met, puis la lettre
    if spaces > 1:
        return " "*spaces + cc[0] + erase(cc[1:])
    # lettre et pas plus d'un espace, on met la lettre simplement
    return cc[0] + erase(cc[1:])
            
