'''#ex nr 1.

note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
note_muzicale = ['do','si','la','sol','fa','mi','re','do']
print(note_muzicale)
note_muzicale[::-1]
note_muzicale = ['do','si','la','sol','fa','mi','re','do']
note_muzicale.reverse()
print(note_muzicale)'''

'''#ex nr 2.

note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale.count('do'))'''

'''#ex nr 3. avand doua liste [3,1,0,2] si [6,5,4] gaseste doua variante sa le unesti intr-o singura lista

lista1 = [3,1,0,2]
lista2 = [6,5,4]
print(lista1 + lista2)
lista1.extend(lista2)
print(lista1)'''

'''#ex nr 4.

lista = [3,1,0,2,6,5,4]
print(lista)
lista.sort()
print(lista)'''

'''#ex nr 5.

lista = [3,1,0,2,6,5,4]
if len(lista) > 0:
    print('lista nu este goala')
else:
    print('lista este goala')'''

'''#ex nr 6.

lista = [3,1,0,2,6,5,4]
lista.clear()
print(lista)'''

'''#ex nr 7.

lista = [3,1,0,2,6,5,4]
lista.clear()
if len(lista) > 0:
    print('lista nu este goala')
else:
    print('lista este goala')'''

'''#ex nr 8. dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5},foloseste o functie ca sa afisezi elevii (cheile).
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())'''

'''#ex nr 9. Printeaza cei trei elevi de mai de sus si notele lor
#ex. Ana a luat nota {x}.Doar nota o vei lua folosindu-te de cheie.
dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
print(dict1.keys())
print(dict1.values())
x = dict1.get('Ana')
y = dict1.get('Gigel')
z = dict1.get('Dorel')
print(f'Ana a luat nota {x}')
print(f'Gigel a luat nota {y}')
print(f'Dorel a luat nota {z}')'''

'''#ex nr 10. Imagineaza-ti ca Dorel a facut constestatie si a primit nota 6.
#Modifica nota lui Dorel in 6
#Printeaza nota lui dupa modificare

dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
dict1['Dorel'] = 6
print(dict1)'''

'''#ex nr 11. Imagineaza-ti ca Gigel se transfera din clasa.Cauta o functie sa il stearga.
#Vine un coleg nou.Adaugati pe Ionica in lista cu nota 9 apoi printati dictionarul cu noii elevi.

dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)'''

'''#ex nr 12. Ai urmatoarele seturi:

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

# Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)'''

'''#ex nr 13. Foloseste un if si verifica daca:
#Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
#regasesc intre elementele din setul zile_sapt)
#Weekend nu este un subset al zilelor din sapt
#Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
#punct de mai sus va fi un boolean

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

 if (weekend == zile_sapt):
     print(f'zilele de {weekend} sunt in {zile_sapt}')
 else:
     print(f'zilele de {weekend} nu sunt in {zile_sapt}')'''

'''# ex nr 14.Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# sunt in weekend si invers)

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt- weekend)'''

'''#en nr 15.Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
#ambele seturi). Hint: Va puteti folosi de o functie

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.intersection(weekend))
print(zile_sapt & weekend)'''











