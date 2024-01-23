def sumy(osudi):
    osudi.pop("", None)
    soucty = {jmeno: sum(hodnoty) for jmeno, hodnoty in osudi.items()}
    serazene_soucty = sorted(soucty.items(), key=lambda x: x[1], reverse=True)
    for jmeno, soucet in serazene_soucty:
        print(f"{jmeno}: {soucet}")


#### LOSOVAČ SIMPLE V.1

import random
import time


def zobraz_stav(listky):
    for hrac, listky_hraca in listky.items():
        print(f"Hráč {hrac}: {sum(listky_hraca)} lístků.")
    print()

def vyber_jmeno(osudi):
    celkem_listku = sum(sum(listky) for listky in osudi.values())
    if celkem_listku == 0:
        return None

    vyherni_cislo = random.randint(1, celkem_listku)
    soucet = 0
    for jmeno, listky in osudi.items():
        soucet += sum(listky)
        if vyherni_cislo <= soucet:
            return jmeno
    return None

def zapni_tombolu(osudi):
    """
    Simple mód, pokud někdo vyhraje, jsou z osudí odebrány všechny jeho lístky.
    Dává tedy smysl losovat od hlavní ceny směrem dolů.
    """

    while True:
        zobraz_stav(osudi)
        losovat = input("Vylosovat dalšího hráče? A/N: ").upper()
        if losovat == "N":
            break

        vybrane_jmeno = vyber_jmeno(osudi)
        if vybrane_jmeno is None:
            print("V osudí nejsou žádné lístky!")
            break

        print("VYLOSOVANÉ JMÉNO: ", end="")
        time.sleep(2)

        for i, pismeno in enumerate(vybrane_jmeno):
            if i == 0:
                time.sleep(3)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(1)
            else: time.sleep(0.5)
            print(pismeno, end="", flush=True)

        print()

        # Odstranění vylosovaného jména z tomboly
        osudi.pop(vybrane_jmeno, None)