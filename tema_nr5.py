'''# ex nr1 Funcție care să calculeze și să returneze suma a două numere.

def suma_numere(a, b):
    return a + b

numar1 = 5
numar2 = 7

rezultat = suma_numere(numar1, numar2)
print(rezultat)'''

'''# ex nr2 Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def numar_par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(numar_par_impar(numar)) # False
print(numar_par_impar(numar)) # True'''

'''# ex nr3 Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def nume_caractere(nume,prenume,nume_mijlociu):
    litere_nume = len(nume) + len(prenume) + len(nume_mijlociu)
        return nume_caractere
print(f'Numarul total de caractere {nume_caractere}(''Todea'',''Alina'',''Ramona'')}')'''


'''#ex nr4 Funcție care returnează aria dreptunghiului
def aria_dreptunghiului(lungime,latime):
    return lungime * latime
aria_dreptunghiului('lungime * latime')'''

'''#ex nr5 Funcție care returnează aria cercului
def piValue():
    return piValue()
piValue(3.14)'''

'''#ex nr6 Funcție care returnează True dacă un caracter x se găsește într-un string dat
#și False dacă nu găsește.
def is_char_in_string(x, string):
    return x in string
is_char_in_string('a', 'hello') #True
is_char_in_string('z', 'hello')#False'''

'''# ex nr7  Funcție fără return, primește un string și printează pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
def print_case_count(string):
    lower_count = 0
    upper_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    print("Nr de caractere lower case este", lower_count)
    print("Nr de caractere upper case este", upper_count)'''

'''#ex nr8 Funcție care primește o LISTA de numere și returnează o LISTA doar cu
#numerele pozitive
def numere_pozitive(numere):
    return [x for x in numere if x > 0]

numere_pozitive([1, -2, 3, -4, 5])'''

'''#ex nr9 Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# Primul număr x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
def compara_numbere(x, y):
    if x > y:
        print("Primul număr", x, "este mai mare decat al doilea nr", y)
    elif x < y:
        print("Al doilea număr", y, "este mai mare decat primul nr", x)
    else:
        print("Numerele sunt egale.")

compara_numbere(5, 7)'''

'''#ex nr10 Funcție care primește un număr și un set de numere.
# Printeaza ‘am adaugat numărul nou în set’ + returnează True
# Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
#returnează False
def set_numbers(num, my_set):
  my_set = {1, 2, 3}
    if num in my_set:
        set_numbers(3, my_set)
        print("nu am adaugat numărul în set. Acesta există deja.")
        return False
    else:
        my_set.add(num)
        set_numbers(4,)
        print("am adaugat numărul nou în set.")
        return True
print(set_numbers(3,{1,2,3}))'''









