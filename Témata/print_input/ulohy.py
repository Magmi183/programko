"""

██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗  ░░░░░░  ███████╗░█████╗░██████╗░░█████╗░███╗░░██╗██╗
██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝  ░░░░░░  ╚════██║██╔══██╗██╔══██╗██╔══██╗████╗░██║██║
██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░  █████╗  ░░███╔═╝███████║██║░░██║███████║██╔██╗██║██║
██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░  ╚════╝  ██╔══╝░░██╔══██║██║░░██║██╔══██║██║╚████║██║
╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░  ░░░░░░  ███████╗██║░░██║██████╔╝██║░░██║██║░╚███║██║
░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░░░░░░  ╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
"""

"""
Úloha 1 - Pozdrav:

Zeptej se uživatele na jméno a potom ho jménem pozdrav.

"""

"""
Úloha 2 - KVÍZ:
Zobrazte uživateli kvíz - otázku a třeba 4 možnosti odpovědí
Načtěte jeho odpověď do proměnné a vytiskněte ji. Nebo nepoužívejte proměnnou a odpověď rovnou vytiskněte.
Zatím není úkolem vyhodnotit správnost odpovědi.
"""


"""
█████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█▄─▄█
██─▄─▄██─▄█▀█▄▄▄▄─██─▄█▀██─█▄▀─███─██
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀
█████████████████████████████████████
"""

"""
Úloha 1 - Pozdrav (ŘEŠENÍ)
"""

jmeno = input("Jak se jmenuješ?\n")

print("Ahoj " + jmeno + ".")

uzivateluv_vek = input("Zadej kolik je ti let: ")
# Můžu sečíst kolik textů (stringů) chci, třeba i takhle:
print("Ahoj, " + jmeno + ", je ti " + uzivateluv_vek + " let.")

###############################################################################

"""
Úloha 2 - KVÍZ (ŘEŠENÍ)
"""

print("Jaká je nejvyšší hora světa?")
print("")
print("a) Smrk")
print("b) Sněžka")
print("c) Mariánský příkop")
print("d) Mt. Everest")

odpoved = input()
print(odpoved)

# alternativne:
print(input())