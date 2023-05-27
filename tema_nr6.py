# ex nr 1.Clasa Cerc
#Atribute: raza, culoare
#Constructor pentru ambele atribute
#Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print("Culoarea cercului este:", self.culoare)
        print("Raza cercului este:", self.raza)

    def aria(self):
        return 3.14 * (self.raza ** 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * 3.14 * self.raza

#ex nr 2 Clasa Dreptunghi
#Atribute: lungime, latime, culoare
#Constructor pentru toate atributele
#Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
#Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

#self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
#descrie().
class Dreptunghi :
    lungime = 0
    latime = 0
    culoare = None
    def __init__ (self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descriere_dreptunghi (self):
        print (f'lungime : {self.lungime}')
        print (f'latime : {self.latime}')
        print (f'culoare : {self.culoare}')
    def calculeaza_aria(self):
        return self.lungime * self.latime
    def calculeaza_perimetru(self):
        return 2 * (self.lungime + self.latime)
    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare

#ex nr 3 Clasa Angajat
#Atribute: nume, prenume, salariu
#Constructor pt toate atributele
#Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
class angajat:
    nume = 'Alina'
    prenume = 'Todea'
    salariu = 2600

    def __int__(self,nume,prenume,salriu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = self.salariu
    def descriere_angajat(self):
        print(f'nume : {self.nume}')
        print(f'prenume : {self.prenume}')
        print(f'salariu : {self.salariu}')
    def nume_complet(self):
        return f' {self.nume} {self.prenume}'
    def salariu_luna(self):
        return self.salariu /12
    def salariu_anual(self):
        return self.salariu
    def marime_salariu(self,procent):
        self.salariu += self.salariu * (procent/100)

#ex nr 4 Clasa Cont
#Atribute: iban, titular_cont, sold
#Constructor pentru toate atributele
#Metode:
# afisare_sold() - Titularul x are în contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
class cont:
    titular_cont = None
    iban = None
    sold = 0
    
    def __init__(self,titular_cont,iban,sold):
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = sold
    def afisare_sold(self):
        print(f'titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self, suma=None):
        self.sold -= suma
    def creditare_cont(self, suma=None):
        self.sold += suma
    











# ex nr 3 Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
def dreptunghi():
    return None


def cerc():
    return None