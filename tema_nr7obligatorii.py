#ABSTRACTION
#Clasa abstractă FormaGeometrica
#Conține un field PI=3.14
#Conține o metodă abstractă aria (opțional)
#Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
#probabil am colturi’
from abc import ABC, abstractmethod

import self as self


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass
    def descriere(self):
        print('Cel mai probabil am colturi')

#INHERITANCE
#Clasa Pătrat - moștenește FormaGeometrica
#constructor pentru latură
class Patrat(FormaGeometrica):
    def __init__(FormaGeometrica, self=None, latura=5):
        self.latura = latura 
    def aria(self):
        return self.latura ** 2

#3ENCAPSULATION
#latura este proprietate privată
#Implementează getter, setter, deleter pentru latură
#Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
#implementezi metoda abstractă aria)
class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura = latura

# @property transforma metoda latura intr un getter

    @property
    def latura(self):
        return self.latura

    @latura.setter
    def latura(self,valoare):
        self.latura = valoare

    @latura.deleter
    def latura(self):
        del self.latura

    def aria(self):
        return self.latura ** 2

#Clasa Cerc - moștenește FormaGeometrica
#constructor pentru rază
#raza este proprietate privată
#Implementează getter, setter, deleter pentru rază
#Implementează metoda cerută de interfață - în calcul folosește field PI
#mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
#abstractă aria)
class Cerc(FormaGeometrica):
    def __init__ (self,raza):
        self.raza = raza

    @property
    def raza(self):
        return self.raza
    @raza.setter
    def raza(self,valoare):
        self.raza = valoare
    @raza.deleter
    def raza(self):
        del self.raza
    def aria(self):
        return self.PI * self.raza ** 2

#POLYMORPHISM
#Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
#Creează un obiect de tip Patrat și joacă-te cu metodele lui
#Creează un obiect de tip Cerc și joacă-te cu metodele lui
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self._latura = latura

    @property
    def latura(self):
        return self._latura

    @latura.setter
    def latura(self, valoare):
        self._latura = valoare

    @latura.deleter
    def latura(self):
        del self._latura

    def aria(self):
        return self.latura ** 2

    def descrie(self):
        print("Eu nu  am colturi")


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self._raza = raza

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, valoare):
        self._raza = valoare

    @raza.deleter
    def raza(self):
        del self._raza

    def aria(self):
        return self.PI * self.raza ** 2

    def descrie(self):
        print("Eu nu am colturi")

