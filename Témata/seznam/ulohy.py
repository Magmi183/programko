"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

# TODO 2023: Revize úloh.


"""
Úkol 0: Náhodný list 

Udělejte si list, který bude obsahovat 100 náhodných čísel od -100 do 100.
Bonus: Zeptejte se uživatele kolik chce čísel a z jakého rozsahu.
Inspirujte se kódem pro vygenerování náhodného čísla níže.
"""
# generování náhodného čísla
import random
nahodne_cislo = random.randrange(-100, 100) # takto vygeneruju jedno náhodné číslo v rozmezí -100 až 100
# teď to jen udělat vícekrát a nasypat to do listu!

cisla = [] # prázný seznam je dobrý začátek... zbytek je na vás!


"""
Úkol 1: Součet čísel v seznamu.

Sečtěte všechna čísla v listu a vypište součet. Využijte k tomu while cyklus.
Až to budete mít, zkuste najít (nebo se zeptejte) jak to udělat jednodušeji.
"""

cisla = [25, -36, 62, 70, 91, -32, 93, 65, 0, 55, 40, -39, 52, 0, 21, 21, 61, -100, -26, 73, 65, 24, -22, 57, 91, -45, 84, 26, -73, -47, 15, 64, 13, -20, 76, 41, -81, -74, 56, -18, -78, 10, -89, 83, 3, -40, 52, 73, 65, -11, -37, 58, -56, 94, -12, 57, -28, 88, -56, -72, -21, 40, -16, 23, 28, 42, -9, 97, 70, 11, 69, 9, -64, -71, -36, -100, 73, -7, -59, -82, 10, 4, 73, -1, -64, 15, -18, 50, 79, -91, 82, 1, -67, -58, 5, -14, -25, -50, 67, 70]

"""
Úkol 1.5: Kolikrát to tam je

Zeptejte se uživatele na nějaké číslo a řekněte mu, kolikrát se v seznamu vyskytuje. Využijte cyklus while nebo metodu count.
"""

cisla = [25, -36, 62, 70, 91, -32, 93, 65, 0, 55, 40, -39, 52, 0, 21, 21, 61, -100, -26, 73, 65, 24, -22, 57, 91, -45, 84, 26, -73, -47, 15, 64, 13, -20, 76, 41, -81, -74, 56, -18, -78, 10, -89, 83, 3, -40, 52, 73, 65, -11, -37, 58, -56, 94, -12, 57, -28, 88, -56, -72, -21, 40, -16, 23, 28, 42, -9, 97, 70, 11, 69, 9, -64, -71, -36, -100, 73, -7, -59, -82, 10, 4, 73, -1, -64, 15, -18, 50, 79, -91, 82, 1, -67, -58, 5, -14, -25, -50, 67, 70]


"""
Úkol 2: Sudé nebo liché?

Na základě původního seznamu čísel udělejte další dva seznamy. Jeden, který bude obsahovat všechna lichá čísla z původního seznamu a druhý, který v sobě bude mít čísla sudá.
Využij operátor modulo (zbytek po dělení).
"""


"""
Úkol 3: Extrémy

Vemte si seznam čísel a najděte v něm největší a nejmenší číslo. 
"""


"""
Úkol 4: Tombola

Nasimulujte tombolu. Pomocí seznamu jmen vylosujte náhodného člověka (nebo více), kteří vyhrají nějakou cenu.
Můžete využít metodu shuffle a generátor náhodných čísel.

Pokud děláte více losování, nezapomeňte vylosovaného člověka ze seznamu odebrat (jednou) - jako v reálné tombole.
"""

import random
nahodne_cislo = random.randrange(-100,100) # takto vygeneruju jedno náhodné číslo v rozmezí -100 až 100

# random.shuffle(nazev_seznamu)  # takto se dá zamíchat seznam


"""
Úloha 5:
Máte seznam jmen - žáků ve třídě. Udělejte program, kde uživatel bude opakovaně zadávat jména a program mu bude říkat,
jestli se jméno v seznamu nachází nebo ne.
"""

jmena = ["Kamil", "Michal", "Jarek", "Anezka", "Hugo"]


"""
Úloha 5.1:
Máte 2 seznamy - seznam lidí a seznam známek. 
1. člověk v seznamu lidí dostal 1. známku ze seznamu známek.
2. člověk 2. známku atd.
Vaším úkolem je vytvořit program, který se opakovaně ptá na jméno a následně řekne, jakou má ten člověk známku,
případně že ho nezná. Program může klidně běžet do nekonečna (while True) nebo naprogramujte mechanismus jeho ukončení.
např:
znamky = [4, 5, 1, 2, "2-"]
jmena = ["Kamil", "Michal", "Jarek", "Anezka", "Hugo"]
Úloha volně navazuje na úlohu 5.
"""

znamky = [4, 5, 1, 2, "2-"] # Seznam známek - jde vidět, že může obsahovat více typů (string, int...)
jmena = ["Kamil", "Michal", "Jarek", "Anezka", "Hugo"] # seznam jmen - první jméno odpovídá první známce atd.

while True: # while True znamená, že se kód provádí do nekonečna, nebo pokud není přerušen jinak (ale podmínka vždy platí)
    jmeno = input("Zadej jméno: \n")

    # ... ZDE PIŠTE SVŮJ KÓD ...
    # VYUŽIJTE PROMĚNNOU JMÉNO, KTERÁ UŽ JE DEFINOVÁNA NAHOŘE

    if jmeno == "KONEC PLS": # pokud uživatel zadá místo jména tento string, tak
        break # se cyklus ukončí - příkazem BREAK se vyskočí z cyklu


