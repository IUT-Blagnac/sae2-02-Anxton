from test import sample_tests

# return cc without spaces
def erase(cc):
    stringList = []
    cpt = 0
    for char in cc:
        if char != " ":
            if cpt > 1:
                stringList += [" "]*cpt
            stringList.append(char)
            cpt = 0
        else:
            cpt+=1
    if cpt > 1:
        stringList += [" "]*cpt
    return "".join(stringList)
            
sample_tests()
print("|"+erase("   a a  ")+"|")
