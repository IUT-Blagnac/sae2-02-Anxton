import timeit

from solution_regex import erase as erase_regex
from solution_compteur import erase as erase_compteur
from solution_while import erase as erase_while
from solution_comprehension import erase as erase_comprehension
from solution_suppr import erase as erase_suppr
from solution_ajout import erase as erase_ajout
from solution_recursif import erase as erase_recursif


import string
import random
s = ""
for i in range(100000):
    s+=random.choice(string.ascii_letters+"     ")
nb = 100
print("solution_regex:",timeit.timeit(lambda: erase_regex(s), number=nb))
print("solution_compteur:",timeit.timeit(lambda: erase_compteur(s), number=nb))
print("solution_comprehension:",timeit.timeit(lambda: erase_comprehension(s), number=nb))
print("solution_ajout:",timeit.timeit(lambda: erase_ajout(s), number=nb))
print("solution_while:",timeit.timeit(lambda: erase_while(s), number=nb))
print("solution_suppr:",timeit.timeit(lambda: erase_suppr(s), number=nb))
# print("solution_recursif:",timeit.timeit(lambda: erase_recursif(s), number=nb)) 