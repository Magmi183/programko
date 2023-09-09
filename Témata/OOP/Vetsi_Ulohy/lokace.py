"""
V tomto souboru můžete realizovat implementaci třídy Lokace a následně ji otestovat pomocí testovacích dat
a jednoduchého programu na procházení Lokací.
"""


# Definice třídy Lokace
class Lokace:
    pass

    # ZDE: Doplňte konstruktor a metody dle zadání


# Testovací data
cesko = Lokace("Česká republika", "Zemský ráj to na pohled")
nemecko = Lokace("Německo", "Země aut a piva")
slovensko = Lokace("Slovensko", "Tatry a Dunaj")
rakousko = Lokace("Rakousko", "Alpy a vídeňský štrúdl")
polsko = Lokace("Polsko", "Historické město Krakov")
francie = Lokace("Francie", "Eiffelova věž a víno")

# Nastavení lokací
cesko.nastav_lokaci_sever(polsko)
cesko.nastav_lokaci_jih(slovensko)
cesko.nastav_lokaci_zapad(nemecko)
cesko.nastav_lokaci_vychod(rakousko)

nemecko.nastav_lokaci_jih(cesko)
nemecko.nastav_lokaci_zapad(francie)

slovensko.nastav_lokaci_sever(cesko)

rakousko.nastav_lokaci_zapad(cesko)

polsko.nastav_lokaci_jih(cesko)

francie.nastav_lokaci_vychod(nemecko)


# Funkce pro pohyb
def prochazeni(start_lokace):
    aktualni_lokace = start_lokace

    while True:
        print(f"Nacházíte se v {aktualni_lokace.jmeno}.")
        print(f"Popis: {aktualni_lokace.popis}")
        print("Kam chcete jít? Možnosti:")

        if aktualni_lokace.lokace_sever:
            print(" - sever (" + aktualni_lokace.lokace_sever.jmeno + ")")
        if aktualni_lokace.lokace_jih:
            print(" - jih (" + aktualni_lokace.lokace_jih.jmeno + ")")
        if aktualni_lokace.lokace_zapad:
            print(" - západ (" + aktualni_lokace.lokace_zapad.jmeno + ")")
        if aktualni_lokace.lokace_vychod:
            print(" - východ (" + aktualni_lokace.lokace_vychod.jmeno + ")")

        volba = input("Vaše volba: ").strip().lower()

        if volba == "sever" and aktualni_lokace.lokace_sever:
            aktualni_lokace = aktualni_lokace.lokace_sever
        elif volba == "jih" and aktualni_lokace.lokace_jih:
            aktualni_lokace = aktualni_lokace.lokace_jih
        elif volba == "západ" and aktualni_lokace.lokace_zapad:
            aktualni_lokace = aktualni_lokace.lokace_zapad
        elif volba == "východ" and aktualni_lokace.lokace_vychod:
            aktualni_lokace = aktualni_lokace.lokace_vychod
        else:
            print("Nelze se pohnout tímto směrem. Zkuste znovu.")


# Spuštění programu
prochazeni(cesko)
