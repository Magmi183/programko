import random


class Ucastnik():

    def __init__(self, jmeno, hp, sila, obratnost):
        self.jmeno = jmeno
        self.hp = hp
        self.max_hp = hp
        self.sila = sila
        self.obratnost = min(10, obratnost) # obratnost může být maximálně 10
        self.inventar = []

    def odpocivej(self):
        # pokud to jde, účastník si doplní 1 HP
        if self.hp < self.max_hp:
            self.hp += 1


    def generuj_utok(self):
        # útok klasického účastníka = jeho síla
        return self.sila

    def prijmi_poskozeni(self, poskozeni):

        # pokus o úhyb útoku, podle obratnosti se šance zvětšuje
        sance = random.randint(0, 20)
        uhyb = sance < self.obratnost
        if uhyb:
            return 0
        else:
            self.hp -= poskozeni
            return poskozeni

    def prijmi_predmet(self, predmet):
        self.inventar.append(predmet)