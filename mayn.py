from tema_nr6 import cerc,dreptunghi,angajat,cont

cerc = cerc(12,'rosu')
cerc.descriere_cerc()
print(cerc.calculeaza_aria())
print(cerc.calculeaza_diametru())
print(cerc.calculeaza_circumferinta())

dreptunghi = dreptunghi(10,9,'galben')
dreptunghi.descriere_dreptunghi()
print(dreptunghi.calculeaza_aria())
print(dreptunghi.calculeaza_perimetru())
dreptunghi.schimba_culoarea('rosu')
dreptunghi.descriere_dreptunghi()

angajat = angajat()
angajat.descriere_angajat()
print(angajat.nume_complet())
print(angajat.salariu_luna())
print(angajat.salariu_anual())
angajat.marire_salariu(6)
angajat.descriere_angajat()

cont = cont('Todea Alina','Ro1409',39966)
cont.afisare_sold()
cont.debitare_cont(696)
cont.afisare_sold()
cont.creditare_cont(325)
cont.afisare_sold()

