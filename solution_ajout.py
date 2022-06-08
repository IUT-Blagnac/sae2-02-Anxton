# return cc without spaces
def erase(cc):
    stringList = []
    if cc[0] != " " or cc[1] == " ":
        stringList.append(cc[0])
    for i in range(1, len(cc)-1):
        if cc[i] != " " or cc[i+1] == " " or cc[i-1] == " ":
            stringList.append(cc[i])
    if cc[-1] != " " or cc[-2] == " ":
        stringList.append(cc[-1])
    return "".join(stringList)
def erase_variante(cc):
    stringList = [cc[0]] if cc[0] != " " or cc[1] == " " else []
    stringList += [cc[i] for i in range(1, len(list(cc))-1) if cc[i] != " " or cc[i+1] == " " or cc[i-1] == " "]
    stringList += [cc[-1]] if cc[-1] != " " or cc[-2] == " " else []
    return "".join(stringList)
def erase_mdr(cc):
    return "".join(([cc[0]] if cc[0] != " " or cc[1] == " " else []) + ([cc[i] for i in range(1, len(list(cc))-1) if cc[i] != " " or cc[i+1] == " " or cc[i-1] == " "]) + ([cc[-1]] if cc[-1] != " " or cc[-2] == " " else []))
    
print(erase(" a l l o  m d r a s d  g g "))
print(erase_variante(" a l l o  m d r a s d  g g "))
print(erase_mdr(" a l l o  m d r a s d  g g "))
print("|"+erase("  a  ")+"|")
print("|"+erase_variante("  a  ")+"|")
print("|"+erase_mdr("  a a a   ")+"|")


# CONTINUE ? SKIP UN ESPACE LORSQUE ON VIENT DE LE DETECTER