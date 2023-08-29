from Témata.OOP.HungerGames.entity.Ucastnik import Ucastnik
from Témata.OOP.HungerGames.predmet.Luk import Luk


class Lukostrelec(Ucastnik):

    def generuj_utok(self):

        utok = self.sila

        # projdeme inventář a najdeme Luk s největším útokem
        for predmet in self.inventar:
            if isinstance(predmet, Luk):
                utok = max(utok, predmet.utok)

        # vrátíme útok nejsilnějšího Luku, pokud žádný Luk nemáme, tak bude hodnota rovna "self.sila"
        return utok