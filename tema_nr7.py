from abc import abstractmethod, ABC

class Apartament:
    suprafata_mp = None
    utilitati = []

    def __init__ (self,suprafata_mp):
        self.suprafata_mp = suprafata_mp
    def listeaza_utilitati(self):
        for utilitate in self.utilitati:
            utilitate.get_consum ()

class Utilitate(ABC):
    consum = 0

    @abstractmethod
    def get_consum(self):
        pass
    def set_consum(self,consum):
        self.consum = consum

class Apa(Utilitate):
    def get_consum(self):
        print(f'Apa:Ati consumat {self.consum} litri')
    def __str__(self):
        return 'apa'

class Gaz(Utilitate):
    def get_consum(self):
        print(f'Gaz:Ati consumat {self.consum} mc')

class Electricitate(Utilitate):
    def get_consum(self):
        print(f'Electricitate:Ati consumat {self.consum} kw/h')
    def __str__(self):
        return 'electricitate'


apartament1 = Apartament(90)
electricitate = Electricitate()
apartament1.utilitati.append(electricitate)
electricitate.set_consum(50)

apa = Apa()
apartament1.utilitati.append(apa)
apa.set_consum(100)


gaz = Gaz()
apartament1.utilitati.append(gaz)
gaz.set_consum(4)

apartament1.listeaza_utilitati()

print(45 * '-')

camera1 = Camera_living
print(camera1.afiseaza_suprafata())
camera1.este_mobilata(True)
print(45 * '-')


