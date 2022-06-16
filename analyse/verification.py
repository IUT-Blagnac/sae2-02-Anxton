from algos.efficacite21 import erase as eff21
from algos.efficacite46 import erase2 as eff46
from algos.simplicite86 import enlever_blanc as simp86
from algos.simplicite118 import erase as simp118
from algos.simplicite154 import erase as simp154
from algos.simplicite160 import bonmot2 as simp160
from algos.simplicite169 import erase as simp169
from algos.sobriete102 import erase as sob102

def test(erase):
    try:
        ok = True
        if erase('') != '': ok = False
        if erase('   06   07 65 19 70 ') != '   06   07651970': ok = False
        if erase(' 666, the number of the beast  ') != '666,thenumberofthebeast  ': ok = False
        if erase('  Cou cou  J M  B') != '  Coucou  JM  B': ok = False
        if erase(' a a a a ') != 'aaaa': ok = False
        if ok: print('✅') # Fonctionne !
        else: print('❌') # Ne fonctionne pas comme attendu
    except:
        print("💀") # Erreur levée

print("efficacite21:")
test(eff21)
print("efficacite46:")
test(eff46)
print("simplicite86:")
test(simp86)
print("simplicite118:")
test(simp118)
print("simplicite154:")
test(simp154)
print("simplicite160:")
test(simp160)
print("simplicite169:")
test(simp169)
print("sobriete102:")
test(sob102)