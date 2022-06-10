# même algorithme que solution_ajout.py avec des listes en compréhension
def erase(cc):
    if cc == '': return ''
    return "".join(([cc[0]] if cc[0] != " " or cc[1] == " " else []) + ([cc[i] for i in range(1, len(list(cc))-1) if cc[i] != " " or cc[i+1] == " " or cc[i-1] == " "]) + ([cc[-1]] if cc[-1] != " " or cc[-2] == " " else []))
    