# return cc without spaces
def erase(cc):
    stringList = []
    i = 0
    while i < len(cc):
        if cc[i] != " ":
            stringList.append(cc[i])
            i+=1
        else:
            if i < len(cc) and cc[i+1] == " ":
                while i < len(cc) and cc[i] == " ":
                    stringList.append(" ")
                    i+=1
            else :
                i+=1
    
    return "".join(stringList)
            
    
print(erase("|"+"Cou cou  J M  B  ")+"|")
