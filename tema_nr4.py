# ex nr1. Avand lista : masini = ['Audi','Volvo','BMW','Mercedes','Aston Martin',Lastun',
# 'Fiat','Trabant','Opel']
#Folosește un for că să iterezi prin toată lista și să afișezi;
#Mașina mea preferată este x’.
# Fă același lucru cu un for each.
# Fă același lucru cu un while.

'''masini = ['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
for masina in masini:
    print(f'Masina mea preferata este {masina}')'''

'''masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i ,masina in enumerate(masini):
    print(f'Masina mea preferata este {masina} de la pozitia{i}')'''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

'''i = 0
while i < len(mașini):
    print("Mașina mea preferată este " + mașini[i])
    i += 1'''

#ex nr 2

'''mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for i in range(1, len(mașini)-1):
    mașini[i] = mașini[i].upper()
else:
    print(mașini)'''

#ex nr 3

'''mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in mașini:
    if masina == "Mercedes":
        print("Am găsit mașina dorită de dvs.")
        break
    else:
        print("Am găsit mașina ", masina, ". Mai căutam.")'''

#ex nr 4

'''mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in mașini:
    if masina in ["Trabant", "Lăstun"]:
        continue
    print("S-ar putea să vă placă mașina", masina)'''

#ex nr 5

mașini = ['Lăstun', 'Trabant', 'Opel', 'Ford', 'Lăstun', 'Tesla']
masini_vechi = []

'''for index, masina in enumerate(mașini):
    if masina in ['Lăstun', 'Trabant']:
        masini_vechi.append(masina)
        mașini[index] = 'Tesla'

print("Modele vechi:", masini_vechi)
print("Modele noi:", mașini)'''

'''#ex nr 6Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
#Vine un client cu un buget de 15000 euro.
#Prezintă doar mașinile care se încadrează în acest buget.
#Itereaza prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină
#xLastun
#Iterează prin listă.

budget = 15000
print(f"Pentru un buget de sub {budget} euro puteți alege următoarele mașini:")
for masina, pret in pret_masini.items():
    if pret <= budget:
        print(masina)
budget = 15000
print(f"Pentru un buget de sub {budget} euro puteți alege următoarele mașini:")
masini_sub_buget = [masina for masina, pret in pret_masini.items() if pret <= budget]
print(*masini_sub_buget, sep = '\n')'''

'''#ex nr 7 Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor = 0
for numar in numere:
    if numar == 3:
        contor += 1
print(contor)'''

'''#ex nr 8 Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

suma = 0
for numar in numere:
    suma += numar

print("Suma numerelor este:", suma)'''

'''#ex nr 9 Aceeași listă:
#Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
largest = numere[0]
for n in numere:
    if n > largest:
        largest = n
print(largest)'''

'''#ex nr 10 Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
#Ex: dacă e 3, să devină -3
# Afișază noua listă.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)'''







