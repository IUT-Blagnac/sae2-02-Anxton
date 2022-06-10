def erase(cc):
    stringList = []
    spaces = 0
    for char in cc:
        # espace : on le compte
        if char == " ":
            spaces+=1
        else:
            # lettre : si on a compté plus d'un espace de suite, on les met
            if spaces > 1:
                stringList.append(" "*spaces)
            stringList.append(char)
            # on remet à 0 les espaces consécutifs
            spaces = 0
    if spaces > 1:
        stringList.append(" "*spaces)
    return "".join(stringList)
