# duplication entière puis on supprime les espaces seuls, inverse de solution_ajout.py
def erase(cc):
    if cc == " " or cc == "":
        return ""
    
    stringList = list(cc)
    
    # premier caractère, on teste seulement si c'est un espace après
    if stringList[0] == " " and stringList[1] != " ":
            stringList.pop(0)
            
    # milieu, on teste avant et après
    i = 0
    while i < len(stringList)-1:
        if stringList[i] == " " and stringList[i+1] != " " and stringList[i-1] != " ":
            stringList.pop(i)
            continue
        i+=1
    
    # dernier caractère, on teste seulement avant
    if stringList[i] == " " and stringList[i-1] != " ":
            stringList.pop(i)
    return "".join(stringList)