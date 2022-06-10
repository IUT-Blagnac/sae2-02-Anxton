import timeit

from solution_regex import erase as erase_regex
from solution_cpt import erase as erase_cpt
from solution_while import erase as erase_while
from solution_comprehension import erase as erase_comprehension
from solution_suppr import erase as erase_suppr
from solution_ajout import erase as erase_ajout
from solution_recursif import erase as erase_recursif

s = " le. Pre  lude a  ttdu je du    ient "
nb = 100000
print("solution_regex:",timeit.timeit(lambda: erase_regex(s), number=nb))
print("solution_cpt:",timeit.timeit(lambda: erase_cpt(s), number=nb))
print("solution_comprehension:",timeit.timeit(lambda: erase_comprehension(s), number=nb))
print("solution_ajout:",timeit.timeit(lambda: erase_ajout(s), number=nb))
print("solution_while:",timeit.timeit(lambda: erase_while(s), number=nb))
print("solution_suppr:",timeit.timeit(lambda: erase_suppr(s), number=nb))
print("solution_recursif:",timeit.timeit(lambda: erase_recursif(s), number=nb))