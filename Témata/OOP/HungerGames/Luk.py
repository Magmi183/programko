from Predmet import Predmet


class Luk(Predmet):

    def __init__(self, nazev, utok):
        self.utok = utok
        super().__init__(nazev)