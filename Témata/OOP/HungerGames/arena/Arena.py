import random

class Arena:

    def __init__(self, ucastnici):
        self.ucastnici = ucastnici
        self.kolo = 1
        self.sance_na_utok = 40
        self.sance_na_odpocinek = 40
        self.sance_na_predmet = 20
    def vygeneruj_akci(self):
        cislo = random.randint(1, 100)

        if cislo <= self.sance_na_utok:
            return "utok"
        elif cislo <= self.sance_na_utok + self.sance_na_odpocinek:
            return "odpocinek"
        else:
            return "predmet"

    def odstran_mrtve(self):
        zivy_ucastnici = []
        for ucastnik in self.ucastnici:
            if ucastnik.hp > 0:
                zivy_ucastnici.append(ucastnik)
            else:
                print(f"{ucastnik.jmeno} umřel")
        self.ucastnici = zivy_ucastnici

    def start(self):

        while len(self.ucastnici) > 1:
            print("------------------------------------------------------------")
            print(f"Kolo {self.kolo}")

            for ucastnik in self.ucastnici:

                if ucastnik.hp <= 0:
                    # tento účastník je mrtvý, zřejmě zemřel dříve v tomto kole a proto je ještě v listu
                    continue

                # každý účastník udělá náhodnou akci
                akce = self.vygeneruj_akci()
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
                    print(f"{ucastnik.jmeno} našel kus klacku. Ale k čemu mu to je?")


            self.odstran_mrtve()


            print(f"Zbývající počet účastníků: {len(self.ucastnici)}")
            for u in self.ucastnici:
                print(f"  - {u.jmeno}, {u.hp} HP")
            input("Stiskni ENTER pro další kolo\n")
            self.kolo += 1

        print(f"Vyhrál {self.ucastnici[0].jmeno}")