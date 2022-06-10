def erase(cc):
    if cc == '' or cc == ' ':
        return ''
    
    stringList = []
    
    # premier caractère, on teste seulement si c'est un espace après
    if cc[0] != " " or cc[1] == " ":
        stringList.append(cc[0])
        
    # milieu, on teste avant et après
    for i in range(1, len(cc)-1):
        if cc[i] != " " or cc[i+1] == " " or cc[i-1] == " ":
            stringList.append(cc[i])
    
    # dernier caractère, on teste seulement avant
    if cc[-1] != " " or cc[-2] == " ":
        stringList.append(cc[-1])
    return "".join(stringList)