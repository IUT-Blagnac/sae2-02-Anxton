
def erase(cc):
    stringList = []
    i = 0
    longueur = len(cc)
    while i < longueur:
        if cc[i] != " ":
            stringList.append(cc[i])
            i+=1
        else:
            if i < longueur-1 and cc[i+1] == " ":
                while i < longueur and cc[i] == " ":
                    stringList.append(" ")
                    i+=1
            else :
                i+=1
    
    return "".join(stringList)
            
    