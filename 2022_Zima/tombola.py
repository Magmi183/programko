"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████──────────██████─██████████████───██████████████─██████─────────██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─
─██████░░██████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██───██░░██████░░██─██░░██─────────██░░██████░░██─
─────██░░██─────██░░██──██░░██─██░░██████░░██████░░██─██░░██──██░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██─
─────██░░██─────██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████░░████─██░░██──██░░██─██░░██─────────██░░██████░░██─
─────██░░██─────██░░██──██░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─
─────██░░██─────██░░██──██░░██─██░░██──██████──██░░██─██░░████████░░██─██░░██──██░░██─██░░██─────────██░░██████░░██─
─────██░░██─────██░░██──██░░██─██░░██──────────██░░██─██░░██────██░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─
─────██░░██─────██░░██████░░██─██░░██──────────██░░██─██░░████████░░██─██░░██████░░██─██░░██████████─██░░██──██░░██─
─────██░░██─────██░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─
─────██████─────██████████████─██████──────────██████─████████████████─██████████████─██████████████─██████──██████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                            ─────────────────────────────────────────────────────────────
                            ─██████████████─██████████████─██████████████─██████████████─
                            ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
                            ─██████████░░██─██░░██████░░██─██████████░░██─██████████░░██─
                            ─────────██░░██─██░░██──██░░██─────────██░░██─────────██░░██─
                            ─██████████░░██─██░░██──██░░██─██████████░░██─██████████░░██─
                            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
                            ─██░░██████████─██░░██──██░░██─██░░██████████─██░░██████████─
                            ─██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────
                            ─██░░██████████─██░░██████░░██─██░░██████████─██░░██████████─
                            ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
                            ─██████████████─██████████████─██████████████─██████████████─
                            ─────────────────────────────────────────────────────────────
PRAVIDLA:
Jak získat lístek:
1. Přijít na kroužek - 1 lístek
2. Umístit se v Kahootu

Pokud je na kroužku aspoň 7 lidí, hodnotí se prvních 5 míst:
1. místo = 5 lístků do osudí
2. místo = 4 lístky do osudí
3. místo = 3 lístky do osudí
4. místo = 2 lístky do osudí
5. místo = 1 lístek do osudí

Jinak se hodnotí první 3 místa:
1. místo = 4 lístky do osudí
2. místo = 3 lístky do osudí
3. místo = 2 lístky do osudí

Lístky za docházku se zapisují hromadně jednou za čas, ne každou hodinu.


CENY:
Jedna hlavní cena a 1-2 ceny útěchy.
"""
import time

osudi_1 = [("Filip", 1), ("Martin", 1), ("Viki", 1), ("Sam", 5), ("Filip", 4), ("Petr", 3), ("Martin", 2), ("Kuba", 1),
           ("Filip", 3), ("Martin", 2), ("Kuba", 1), ("Viki", 3), ("David", 2), ("Petr", 1), ("David", 3), ("Petr", 2),
           ("Filip", 1),
           ("Martin", 3), ("Kuba", 2), ("Petr", 1), ("Filip", 3), ("David", 2), ("Petr", 1), ("Petr", 3), ("Martin", 2),
           ("Pavel", 1),
           ("Filip", 3), ("David", 2), ("Martin", 1), ("David", 3), ("Kuba", 2), ("Martin", 1), ("David", 3),
           ("Martin", 2),
           ("Filip", 1), ("David", 3), ("Martin", 2), ("Petr", 1), ("Martin", 3), ("David", 2), ("Petr", 1),
           ("Martin", 3),
           ("Petr", 2), ("David", 1)]

osudi_2 = [("Oskar", 1), ("Honza", 1), ("Sam", 1), ("Oskar", 3), ("Dmytro", 2), ("Tobiáš", 1), ("Dmytro", 5),
           ("Sam", 4),
           ("Lukáš", 3), ("Oskar", 2), ("Honza", 1), ("Oskar", 5), ("Lukáš", 4), ("Honza", 3), ("Tobiáš", 2),
           ("Diana", 1), ("Tobiáš", 3),
           ("Oskar", 2), ("Lukáš", 1), ("Oskar", 5), ("Honza", 4), ("Dmytro", 3), ("Tobiáš", 2), ("Lukáš", 1),
           ("Oskar", 3),
           ("Lukáš", 2), ("Honza", 1), ("Oskar", 3), ("Lukáš", 2), ("Filip", 1), ("Sam", 3), ("Honza", 2),
           ("Tobiáš", 1),
           ("Lukáš", 3), ("Dmytro", 2), ("Honza", 1), ("Dmytro", 3), ("Diana", 2), ("Honza", 1), ("Dmytro", 3),
           ("Oskar", 2),
           ("Lukáš", 1), ("Honza", 3), ("Oskar", 2), ("Diana", 1), ("Honza", 5), ("Dmytro", 4), ("Filip", 3),
           ("Lukáš", 2), ("Tobiáš", 1)]

osudi = osudi_1

import random

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
    time.sleep(5)
    timer = 3
    for p in vitez:
        print(p, end="")
        time.sleep(timer)
        timer = max(1, timer - 2)
    print()
    # SMAZÁNÍ VYLOSOVANÉHO HRÁČE Z TOMBOLY - KAŽDÝ MŮŽE VYHRÁT MAX. JEDNOU
    listky.pop(vitez)
