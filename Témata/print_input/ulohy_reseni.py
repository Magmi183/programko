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