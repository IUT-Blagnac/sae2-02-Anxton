from solution_regex import erase as erase_regex
from solution_compteur import erase as erase_compteur
from solution_while import erase as erase_while
from solution_comprehension import erase as erase_comprehension
from solution_suppr import erase as erase_suppr
from solution_ajout import erase as erase_ajout
from solution_recursif import erase as erase_recursif

def sample_tests(erase):
    ok = True
    if erase('') != '': ok = False
    if erase(' 06   07 65 19 70 ') != '06   07651970': ok = False
    if erase(' 666, the number of the beast  ') != '666,thenumberofthebeast  ': ok = False
    if erase('  Cou cou  J M  B') != '  Coucou  JM  B': ok = False
    if ok: print('ok')
    else: print('erreur')
    
print("solution_regex:")
sample_tests(erase_regex)
print("solution_compteur:")
sample_tests(erase_compteur)
print("solution_comprehension:")
sample_tests(erase_comprehension)
print("solution_ajout:")
sample_tests(erase_ajout)
print("solution_while:")
sample_tests(erase_while)
print("solution_suppr:")
sample_tests(erase_suppr)
print("solution_recursif:") 
sample_tests(erase_recursif)