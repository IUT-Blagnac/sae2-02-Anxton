from algos.efficacite21 import erase as eff21
from algos.efficacite46 import erase2 as eff46
from algos.simplicite86 import enlever_blanc as simp86
from algos.simplicite118 import erase as simp118
from algos.simplicite154 import erase as simp154
from algos.simplicite160 import bonmot2 as simp160
from algos.simplicite169 import erase as simp169
from algos.sobriete102 import erase as sob102

def sample_tests(erase):
    try:
        ok = True
        if erase('') != '': ok = False
        if erase('   06   07 65 19 70 ') != '   06   07651970': ok = False
        if erase(' 666, the number of the beast  ') != '666,thenumberofthebeast  ': ok = False
        if erase('  Cou cou  J M  B') != '  Coucou  JM  B': ok = False
        if ok: print('✅') # Fonctionne !
        else: print('❌') # Ne fonctionne pas comme attendu
    except:
        print("💀") # Erreur levée

print("efficacite21:")
sample_tests(eff21)
print("efficacite46:")
sample_tests(eff46)
print("simplicite86:")
sample_tests(simp86)
print("simplicite118:")
sample_tests(simp118)
print("simplicite154:")
sample_tests(simp154)
print("simplicite160:")
sample_tests(simp160)
print("simplicite169:")
sample_tests(simp169)
print("sobriete102:")
sample_tests(sob102)