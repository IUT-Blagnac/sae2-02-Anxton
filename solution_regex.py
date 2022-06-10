import re

def erase(cc):
    # supprime : espace seul en début de ligne | espace entre deux lettres | espace seul en fin de ligne
    # utilisation de lookbehinds/lookaheads pour éviter les problèmes de chevauchement
    return re.sub(r'(?<! ) (?! )', '', cc)
