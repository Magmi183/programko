import random

from Luk import Luk
from Predmet import Predmet


class Arena:

    def __init__(self, ucastnici):
        self.ucastnici = ucastnici
        self.kolo = 1
        self.sance_na_utok = 40
        self.sance_na_odpocinek = 40
        self.sance_na_predmet = 20

    def vygeneruj_akci(self):
        """
        Funkce náhodně vygeneruje nějakou akci, šance na jednotlivé akce jsou dány vlastnosmi arény.
        Funkce vráti jedno z: utok, odpocinek, predmet
        """

        cislo = random.randint(1, 100)

        if cislo <= self.sance_na_utok:
            return "utok"
        elif cislo <= self.sance_na_utok + self.sance_na_odpocinek:
            return "odpocinek"
        else:
            return "predmet"

    def vygeneruj_predmet(self):
        cislo = random.randint(1, 2)

        if cislo == 1:
            return Predmet("klacek")
        elif cislo == 2:
            return Luk("Obyčejný luk", 15)

    def odstran_mrtve(self):
        """
        Tato metoda projde seznam účastníku, vybere všechny kteří žijí (mají HP větší než 0)
        a dá je do nového seznamu. Následně nahradí starý seznam nový seznamem, takže zůstanou jen živí účastníci.
        Funkce tedy slouží k ODSTRANĚNÍ MRTVÝCH ÚČASTNÍKŮ Z ARENY.
        """
        zivy_ucastnici = []
        for ucastnik in self.ucastnici:
            if ucastnik.hp > 0:
                zivy_ucastnici.append(ucastnik)
            else:
                print(f"{ucastnik.jmeno} umřel")
        self.ucastnici = zivy_ucastnici

    def zobraz_stav_areny(self):
        print(f"Zbývající počet účastníků: {len(self.ucastnici)}")
        for u in self.ucastnici:
            print(f"  - {u.jmeno}, {u.hp} HP")

    def vyhodnot_akci(self, akce, ucastnik):
        """
        Vyhodnotí akci pro danného účastníka.
        """
        if akce == "utok":
            poskozeni = ucastnik.generuj_utok()

            obet = random.choice(self.ucastnici)
            while obet == ucastnik:
                # vybíráme znova, ucastnik nemůže útočit sám na sebe
                obet = random.choice(self.ucastnici)

            utrpene_poskozeni = obet.prijmi_poskozeni(poskozeni)
            print(f"{ucastnik.jmeno} způsobil {utrpene_poskozeni} poškození hráči {obet.jmeno}")

        elif akce == "odpocinek":
            ucastnik.odpocivej()
            print(f"{ucastnik.jmeno} odpočívá")

        elif akce == "predmet":
            predmet = self.vygeneruj_predmet()
            ucastnik.prijmi_predmet(predmet)
            print(f"{ucastnik.jmeno} našel {predmet}.")

    def start(self):
        """
        Funkce odstartuje HERNÍ CYKLUS. Opakují se následující akce:
            - Zamíchá se pořadí účastníku.
            - Postupně se prochází účastníci a pro každého z nich se vygeneruje nějaká akce, kterou ihned vykoná.
            - Mrtvý účastníci se odstraní z arény.
            - Zobrazí se stav areny.
            - Pokud zbývají alespoň 2 hráči, jede se další kolo, pokud ne, vyhlásí se vítěz.

        """

        while len(self.ucastnici) > 1:
            input("Stiskni ENTER pro další kolo\n")
            print("------------------------------------------------------------")
            print(f"Kolo {self.kolo}")

            # zamícháme pořadí účastníků
            random.shuffle(self.ucastnici)

            for ucastnik in self.ucastnici:

                if ucastnik.hp <= 0:
                    # tento účastník je mrtvý, zřejmě zemřel dříve v tomto kole a proto je ještě v listu
                    continue

                # každý účastník udělá náhodnou akci
                akce = self.vygeneruj_akci()
                self.vyhodnot_akci(akce, ucastnik)

            self.odstran_mrtve()
            self.zobraz_stav_areny()
            self.kolo += 1

        print(f"Vyhrál {self.ucastnici[0].jmeno}")
