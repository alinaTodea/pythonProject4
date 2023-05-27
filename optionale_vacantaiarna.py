'''#1. Având doua numere întregi, printează produsul dacă e mai mic sau
# egal decât 2000, altfel printează suma. Testează cu diferite valori.

def test(a, b):
  result = a * b if a * b <= 2000 else a + b
  print(result)

test(10, 200)  # 2000
test(10, 201)  # 211
test(10, 20)  # 200'''

'''#2. Amandoua liste cu numere întregi, crează o lista care conține
#numerele pare din prima lista și numerele impare din a doua lista.
#Testează cu diferite valori.

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [11,12,13,14,15,16,17,18,19,20]

numere_pare = []
numere_impare = []

for numar in lista1:
  if numar % 2 == 0:
    numere_pare.append(numar)

for numar in lista2:
  if numar % 2 == 1:
    numere_impare.append(numar)

  print('Numere pare')
  print('Numere impare')'''

'''#ex3. Calculează suma numerelor din lista l = [ 10, 20, 34, 55, 67, 80,9].

sum = 0
l = [10,20,34,55,67,80,9]
for numar in l:
  sum += numar
l = [10, 20, 34, 55, 67, 80, 9]
sum = 0
for numar in l:
  sum += numar
print(sum)'''

'''#ex4. Printează cel mai mic număr din lista l = [ 10, 20, 34, 55, 67, 80, 9].

l = [ 10, 20, 34, 55, 67, 80, 9]
print(min(l))'''

'''#ex5. Printează poziția numarului 34 din lista l = [ 10, 20, 34, 55, 7, 80, 9].
l = [ 10, 20, 34, 55, 7, 80, 9]
print(l.index(34))'''

'''#ex6. Printează anul nașterii lui Tom dict={“nume”: “Tom”, “țară”:“USA”, “Anul nașterii”: 1991, “înălțime”: 163}.

dict={'nume': 'Tom', 'țară':'USA', 'Anul nașterii': 1991, 'înălțime': 163}
year_of_birt = dict['Anul nașterii']
print(year_of_birt)'''

'''#ex7. Adauga doi centimetrii înalții lui Tom.
dict={'nume': 'Tom', 'țară':'USA', 'Anul nașterii': 1991, 'înălțime': 163}
dict["înălțime"] += 2
print(dict["înălțime"]) '''

'''#ex8. Printează țara dacă începe cu litera “A”, altfel printează 'Irelevant'.
dict={'nume': 'Tom', 'țară':'USA', 'Anul nașterii': 1991, 'înălțime': 163}
if dict["țară"].startswith("A"):
  print(dict["țară"])
else:
  print("Irelevant")'''

'''#ex9. Verifica dacă un string introdus de la tastatura începe cu “A”.
string = input("Introdu un string: ")
if string.startswith("A"):
  print("String-ul introdus începe cu 'A'.")
else:
  print("String-ul introdus NU începe cu 'A'.")'''

'''#ex10. Printează 5 din lista nested_list=[[1,2,3], [4,5,6], [7,8,9]].
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][1])'''


'''#ex11. Printează caracterul “Z” din nested_list = [['Elefant','Șoarece', 'Girafa'], ['Bizon', 'Zebra', 'Hipopotam']]
nested_list = [['Elefant','Șoarece', 'Girafa'], ['Bizon', 'Zebra', 'Hipopotam']]
print(nested_list[1][1])'''

'''#ex12. Printeaza primul elemente din vremea României nested_dict ={'Romania': {'verse':['ploaie', 'vant'], 'drum':'uscat'}, 'Germania':{'vreme':['ceata', 'nori'], 'drum': 'pietros'}}
nested_dict ={'Romania': {'verse':['ploaie', 'vant'], 'drum':'uscat'}, 'Germania':{'vreme':['ceata', 'nori'], 'drum': 'pietros'}}
print(nested_dict["Romania"]["verse"][0])'''

'''#ex13. Declara o lista și printeaz-o în ordine descrescătoare/inversa alfabetic. Testează cu diferite valori.
lista = [5, 6, 7]
lista_sortata = sorted(lista, reverse=True)
print(lista_sortata)'''

'''#ex14. Printează partea zecimala a unui număr introdus de la tastatura.Dacă partea zecimala nu exista, printează “Numărul este întreg”
import math
numar = float(input("Introdu un numar: "))
parte_zecimala, parte_intreaga = math.modf('numar')

if parte_zecimala == 0:
  print("Numarul este întreg")
else:
  print("Partea zecimala a numarului este:", parte_zecimala)'''

'''#ex15. Introdu o cifra n de la tastatura. Calculează n + nn + nnn.Exemplu: Dacă cifra data e 4, se calculează 4 + 44 +444.
n = 4
result = 0
result = n + (n * 10 + n) + (n * 100 + n * 10 + n)
print(result)'''

'''#ex16. Introdu un număr de la tastatura. Verifica dacă acel număr e la distanta de cel mult 100 de 500 sau 700.
def check_distance(num):
  if abs(num - 500) <= 100 or abs(num - 700) <= 100:
    return True
  else:
    return False
num = int(input('Introdu un număr: '))
if check_distance (num):
  print('Numărul este la distanță de cel mult 100 de 500 sau 700.')
else:
  print('Numărul nu este la distanță de cel mult 100 de 500 sau 700.')'''

'''#ex17. Introdu un string de la tastatura. Verifica dacă acel string e un număr par sau impar. Atenție: string-ul poate sa fie orice.Testează cu diferite valori.
numar = 2
if numar % 2 == 0:
    print(f'Numarul este par')
else:
    numar (f'Numarul este impar')'''

'''#ex18. Introdu 3 numere de la tastatura. Afișează suma lor dacă numerele sunt diferite, sau 0 dacă cel putin doua din numere sunt egale.

numar1 = int(input("Introdu primul numar: "))
numar2 = int(input("Introdu al doilea numar: "))
numar3 = int(input("Introdu al treilea numar: "))

if numar1 == numar2 or numar1 == numar3 or numar2 == numar3:
    print(0)
else:
    print(numar1 + numar2 + numar3)'''

'''#ex19. Calculează suma finala a unui credit, știind suma împrumutată,dobânda anuală și perioada împrumutului (în ani).
suma_finala = ('suma împrumutata + (suma împrumutata * dobanda anuala * perioada împrumutului')
suma_finala = 10.000 + (10.000 * 10 * 3) / 100
suma_finala = 10.000 + 3.000
suma_finala = 13.000'''

'''#ex20. Verifica dacă o variabila este lista, tuple sau set.
x = ([1,2,3])
x = ((1,2,3))
x = ({123})
if type(x) is list:
    print("The input is a list.")
elif type(x) is tuple:
    print("The input is a tuple.")
elif type(x) is set:
    print("The input is a set.")
else:
    print("The input is neither a list, a tuple, nor a set.")'''

























