import random
import datetime
"""
ceska_mesta = ["Praha", "Brno", "Ostrava", "Plzeň", "Liberec", "Olomouc", "České Budějovice", "Hradec Králové", "Ústí nad Labem", "Pardubice", "Zlín", "Karviná", "Teplice", "Děčín", "Chomutov", "Jablonec nad Nisou", "Prostějov", "Třebíč", "Kolín", "Kroměříž", "Šumperk", "Česká Lípa", "Jihlava", "Kladno", "Havířov", "Mladá Boleslav", "Trutnov", "Tábor", "Žďár nad Sázavou", "Rakovník", "Přerov", "Litvínov", "Valašské Meziříčí", "Jindřichův Hradec", "Vsetín", "Brandýs nad Labem-Stará Boleslav", "Jičín", "Náchod", "Benešov", "Břeclav", "Litoměřice", "Cheb", "Kopřivnice", "Uherské Hradiště", "Blansko", "Žatec", "Klatovy", "Sušice", "Jirkov", "Frýdek-Místek", "Český Těšín", "Beroun", "Rumburk", "Nový Jičín", "Louny", "Jeseník", "Uherský Brod", "Pelhřimov", "Ostrov"]


with open("texty/teploty.csv", "w", encoding="utf-8") as soubor:



    for i in range(10000):
        # Nastavení rozmezí datumů
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date.today()

        # Generování náhodného data
        random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

        teplota = random.randrange(-15, 35)
        soubor.write(random.choice(ceska_mesta)+","+str(teplota)+","+str(random_date)+"\n")
"""

ceska_jmena_kluci = ["Tomík", "Bertík", "Míša", "Honza", "Vojtík", "Pája", "Adam", "Lukáš"]

with open("texty/kluci.csv", "w", encoding="utf-8") as soubor:
    for i in range(4324):
        penez = str(random.randrange(100, 100000))
        soubor.write(random.choice(ceska_jmena_kluci) + "," + penez + "\n")

