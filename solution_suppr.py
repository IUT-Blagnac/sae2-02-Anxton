# return string without spaces
def erase(cc):
    if cc == " " or cc == "":
        return ""
    string = list(cc)
    if string[0] == " " and string[1] != " ":
            string.pop(0)
    i = 0
    while i < len(string)-1:
        if string[i] == " " and string[i+1] != " " and string[i-1] != " ":
            string.pop(i)
            continue
        i+=1
    if string[i] == " " and string[i-1] != " ":
            string.pop(i)
    return "".join(string)
    
    
print(erase(" allo  mdr asd  gg "))
print("|"+erase(" a ")+"|")


# CONTINUE ? SKIP UN ESPACE LORSQUE ON VIENT DE LE DETECTER