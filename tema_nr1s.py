# Ex1 o variabila = o cutiuta in care stocam valori
# Ex2 string,int,float,bool

produs = 'iphone'
print('produs')
model = 11  # int
print('model')
pret = 2200.50 #float
print('pret')
promo = True # bool
print('True')

# Ex3 utilizeaza functia type
print(type('produs'))
print(type('model'))
print(type('pret'))
print(type('promo'))

# Ex4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
print('pret')
pret = '2200'
print(f'Am cumparat un telefon iphone 11 la pretul :{pret}')

# Ex nr5
print(f'Telefonul {produs} model {model} avand pretul de {pret} este la promotie {promo} !')

# Ex nr6
nume = input('Introduceti numele')
prenume = input('Introduceti prenumele')
print(f'Numele complet are {len(nume + prenume)} caractere')

# Ex nr7
lungime = int(input('Introduceti lungimea dreptunghiului'))
latime = int(input('Introduceti latimea dreptunghiului'))
print(f'Aria dreptunghiului este {lungime * latime}.')

# Ex nr8
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.coun('the'))

# Ex nr9
print(propozitie.replace('the'))

# Ex nr10
assert propozitie.isnumeric(),'stringul nu contine doar numere'
