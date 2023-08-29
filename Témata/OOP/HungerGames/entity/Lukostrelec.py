from Témata.OOP.HungerGames.entity.Ucastnik import Ucastnik
from Témata.OOP.HungerGames.predmet.Luk import Luk


class Lukostrelec(Ucastnik):
    """
    Účastník, který ale umí používat luk.
    Jediné v čem se liší od obyčejného účastníka je mechanika útoku - pokud má v inventáři luk, použije ho k útoku,
    čímž způsobí tolik poškození, kolik má Luk damage.
    """


    def generuj_utok(self):

        utok = self.sila

        # projdeme inventář a najdeme Luk s největším útokem
        for predmet in self.inventar:
            if isinstance(predmet, Luk):
                utok = max(utok, predmet.utok)

        # vrátíme útok nejsilnějšího Luku, pokud žádný Luk nemáme, tak bude hodnota rovna "self.sila"
        return utok