"""
PRAVIDLA:

Pokud je na kroužku aspoň 7 lidí, hodnotí se prvních 5 míst:
1. místo = 5 lístků do osudí
2. místo = 4 lístky do osudí
3. místo = 3 lístky do osudí
4. místo = 2 lístky do osudí
5. místo = 1 lístek do osudí

Jinak se hodnotí první 3 místa:
1. místo = 3 lístky do osudí
2. místo = 2 lístky do osudí
3. místo = 1 lístky do osudí
"""

osudi_1 = {"Petr": [3, 1, 2, 2, 3, 1, 1, 4, 3, 2, 2, 3, 4],
           "Pavel": [2, 1, 1, 1, 1, 1],
           "Kuba": [1, 3, 2, 2, 2, 3, 1, 1, 1, 1],
           "Martin": [3, 2, 3, 4, 3, 2, 3, 1, 3, 3, 1, 3, 3, 3, 2],
           "David": [2, 1, 1, 2, 5, 2, 2, 1]
           }


osudi = [(name, value) for name, values in osudi_1.items() for value in values]

import random
import time

listky = {}
for listek in osudi:
    if listek[0] not in listky: listky[listek[0]] = listek[1]
    listky[listek[0]] += listek[1]

listky = dict(sorted(listky.items(), key=lambda x: x[1], reverse=True))


def zobraz_stav():
    for hrac in listky.items():
        print("Hráč " + hrac[0] + ": " + str(hrac[1]) + " lístků.")
    print()

zobraz_stav()

hrace_smazat = input("\nZadej hráče, které chceš smazat, oddělené čárkou: ")
hrace_smazat = list(map(str.strip, hrace_smazat.split(",")))
for hrac_ke_smazani in hrace_smazat:
    listky.pop(hrac_ke_smazani, None)

print("\n** ZÁVĚREČNÝ STAV **")
zobraz_stav()

while True:
    losovat = input("Vylosovat dalšího hráče? A/N: ").upper()
    while losovat not in ["A", "N"]:
        losovat = input("Vylosovat dalšího hráče? Zadej A nebo N!: ").upper()

    if losovat == "N": break

    celkem_listku = sum(pl[1] for pl in listky.items())
    if celkem_listku <= 0:
        print("V osudí nejsou žádné lístky!")
        break

    vyherni_listek = random.randrange(1, celkem_listku + 1)
    vitez = ""
    aktualni = 1
    for hrac in listky.items():
        if vyherni_listek < aktualni + hrac[1]:
            vitez = hrac[0]
            break
        aktualni += hrac[1]

    print("VYLOSOVANÉ JMÉNO: ", end="")
    time.sleep(2)
    timer = 1.5
    for p in vitez:
        print(p, end="")
        time.sleep(timer)
        timer = max(0.5, timer - 0.33)
    print()
    # Každé vylosování ubere vítězovi X lístků z tomboly
    X = 3
    listky[vitez] -= X
    listky[vitez] = max(listky[vitez], 0) # minimum lístků je 0
    print("\n** STAV DO DALŠÍHO KOLA: **")
    zobraz_stav()
