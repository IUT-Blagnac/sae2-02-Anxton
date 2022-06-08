# return cc without spaces
def erase(cc):
    stringList = []
    i = 1
    while 1:
        if cc[i-1] == " ":
            stringList.append(cc[i])
            i+=1
        elif cc[i] != " ":
            stringList.append(cc[i])
            i+=1
        else:
            if cc[i+1] == " ":
                stringList.append(" ")
                stringList.append(" ")
                i+=2
    
    return stringList
            
    
print(erase(" a a l l o  o "))


# CONTINUE ? SKIP UN ESPACE LORSQUE ON VIENT DE LE DETECTER