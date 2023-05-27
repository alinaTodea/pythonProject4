# ex nr1 cum functioneaza un if else ?
# un if else ruleaza codul de sus in jos , lasa sa curga codul frumos
# if else este o conditionare
# ex nr2 x este un numar natural sau nu . verifica
x=4
if type(x) == int and x >= 1:
    print("numarul este natural")
else:
    print("numarul nu este natural")

# ex nr3 x este numar pozitiv,negatic sau nu
x = 4
if x >= 1:
    print(f"numarul {x} este pozitiv")
elif x == 0:
    print(f'numarul {x} este negativ')
else:
    print(f'numarul {x} este neutru')

# ex4 daca x este -2 si 13
x = 4
if x >= -2 and x <= 13:
    print(f'numarul {x} este cuprins intre -2 si 13')
else:
    print(f'numarul {x} nu este cuprins intre -2 si 13')

# ex nr5 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
#cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs

x = 4
y = 8
if (abs (x - y)) < 6:
    print(f'diferenta dintre {x} si {y} este mai mica de 5')
elif (abs(x - y)) < 5:
    print (f'diferenta dintre {x} si {y} este mai mica decat 5')
elif (abs(x - y)) == 5:
    print(f'diferenta dintre {x} si {y} este egala cu 5')
else:
    print(f'diferenta dintre {x} si {y} este mai mare decat 5')

#ex nr6 Verifica daca x NU este intre 5 si 27, incluzand capetele de interval . (a se folosi 'not' )

x = 4
if not (5 <= x <= 27):
    print(f'numarul {x} nu neste cuprins intre numerele 5 si 27')
else:
    print(f'numarul {x} este cuprins intre numerele 5 si 27')

#ex nr7 Declara o noua variabila y de tip int apoi verifica si afiseaza daca x si y sunt egale,
#daca nu , afiseaza care din ele este mai mare

x = 4
y = 8

if x == y:
    print(f'numerele {x} si {y} sunt egale ')
elif x > y:
    print(f'numerele {x} si {y} nu sunt egale iar numarl {x} este mai mare decat numarul {y}')
else:
    print(f'numerele {x} si {y} nu sunt egale iar numarul {x} este mai mic decat numarul {y}')

# ex nr8 Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

x = 4
y = 8
z = 8
if x == y == z:
    print('triunghiul este echilateral')
elif x == y:
    print('triunghiul este isoscel')
elif x == z:
    print('triunghiul este isoscel')
elif y == z:
    print('triunghiul este isoscel')
else :
    print('nici o latura nu este egala')

# ex nr9 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = str(input('introdu o litera'))
vocale = 'AaEeIiOoUu'
if litera in vocale:
    print(f'litera {litera} este o vocala')
else:
    print(f'litera {litera} nu este o vocala')

# ex nr10 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = float(input('Introdu o nota in sistem romanesc'))
if 9 < nota <= 10:
    print('ai luat nota A in sistem american')
elif 8 < nota <= 9:
    print('ai luat nota B in sistem american')
elif 7 < nota <= 8:
    print('ai luat nota C in sistem american')
elif 6 < nota <= 7:
    print('ai luat nota D in sistem american')
elif 4 < nota <= 7:
    print('ai luat nota E in sistem american')
elif 1 <= nota <=4:
    print('si luat nota F in sistem american')
else:
    print('nu ai introdus un  umar intre 1 si 10')








