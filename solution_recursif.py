# même algorithme que solution_compteur.py sous forme récursive
def erase(cc, spaces=0):
    if cc == "":
        return ""
    # espace : on le note
    if cc[0] == " ":
        return erase(cc[1:], spaces+1)
    # lettre : si on a compté plus d'un espace, on les met
    if spaces > 1:
        return " "*spaces + cc[0] + erase(cc[1:])
    # lettre et pas plus d'un espace
    return cc[0] + erase(cc[1:])
            
    