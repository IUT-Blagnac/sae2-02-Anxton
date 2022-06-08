# return cc without spaces
def erase(cc):
    stringList = []
    i = 0
    while i < len(cc)-1:
        if cc[i] != " ":
            stringList.append(cc[i])
            i+=1
        else:
            while cc[i+1] == " " or i < len(cc):
                stringList.append(" ")
                i+=1
    
    return stringList
            
    
print(erase(" a a l l o  o "))


# CONTINUE ? SKIP UN ESPACE LORSQUE ON VIENT DE LE DETECTER