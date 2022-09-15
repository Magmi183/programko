# Seznam (nebo list) je něco, kam si můžu uložit více hodnot.
# Seznamy se dobře vysvětlují rovnou na praktických ukázkách.

# Vezměme si situaci, kdy chceme pozdravit všechny účastníky našeho kroužku.
# Na to se hezky hodí mít někde nějaký seznam účastníků a pak prostě každého z nich pozdravit.

ucastnici = ["Tonda", "Kuba", "Sam", "Vojta", "Vitek", "David", "Adam"]

# A teď třeba pomocí while cyklu ...
ucastnik_cislo = 0
while ucastnik_cislo < len(ucastnici):
    print("Ahoj " + ucastnici[ucastnik_cislo])
    ucastnik_cislo += 1

# ... ale pojďme to vzít trochu od začátku.

# Nový seznam se vytváří podobně jako proměnná. Prostě napíšu jeho jméno, rovná se a na pravou stranu
# do hranatých závorek dám hodnoty, které chci v seznamu mít.

ptaci = ["kos", "čáp", "pštros", "tučňák"]

# Když chci zjistit, jak je seznam dlouhý, tedy kolik je v něm věcí, využiju funkci len().
# Znát délku seznamu se mi může hodit i třeba kvůli cyklům.
print(len(ptaci))

# ... můžu si uložit do proměnné ...
delka_seznamu = len(ptaci)

print("Celkem je v seznamu " + str(delka_seznamu) + " ptáků.")

# Co když chci vypsat nějaký konkrétní prvek seznamu? Co když mě zajímá, jaký prvek je první/poslední/druhý... ?
# Napíšu jméno seznamu, hranaté závorky a do nich index. Index znamená pořadí prvku v seznamu.
# A pozor, 1. prvek seznamu je na indexu nula. V programování se skoro všechno počítá od 0!

zavodnici = ["Bob", "Yarek", "Kamil", "Dominik", "Arnost"]
print("Na prvním místě je: " + zavodnici[0])
print("Na druhém místě je: " + zavodnici[1])

# Python umí indexovat i od zadu! -1 je poslendí prvek. -2 je předposlední atd.
print("Na posledním místě je: " + zavodnici[-1])

# Můžeme si třeba udělat program, který se zeptá uživatele kolikátý chce vidět prvek a my mu ho ukážem.
# Použijeme seznam závodníků.

poradi = int(input("Zadej pořadí závodníka (od 0!)."))
pocet_zavodniku = len(zavodnici)
if poradi < pocet_zavodniku and poradi > -pocet_zavodniku:
    print("Závodník v pořadí: " + str(poradi) + " je " + zavodnici[poradi] + ".")
else:
    print("Tolik závodníků se závodu neúčastnilo.")


# Když chceme napsat jméno a pořadí každého závodníka, můžeme použít while cyklus.
# Tentokrát budem číslovat od 1, aby uživatel nebyl zmatený. Do seznamu ale furt musíme přistupovat od 0.
cislo = 0
while cislo < len(zavodnici):
    print("Na místě " + str(cislo+1) + " se umístil " + zavodnici[cislo] + '.')
    cislo += 1


# Do seznamu můžeme také přidávat! Co když poslední závodník doběhl tak pozdě, že jsme na něj zapomněli?

zavodnici.append("Alfons") # metoda append přidá prvek na KONEC seznamu

# přidáme ještě jednoho

zavodnici.append("Kvido")

print("Poslední je: " + zavodnici[-1])

# Často budu chtít začít s prázdným seznamem a postupně ho naplnit čím chci.

cisla = [] # prázdný seznam
cislo = 0
while cislo <= 50: # dokud je číslo menší nebo rovno 50, tak dělej
    cisla.append(cislo) # přidám číslo do seznamu
    cislo += 1 # zvětším číslo (které v příštím cyklu pak přidám do seznamu)
# Udělal jsem si seznam čísel od 0 do 50.
print(cisla) # Celý seznam můžu vytisknout také tímto způsobem.


# Seznam v Pythonu umí SPOUSTU dalších věcí. Je to takzvaný objekt. A každý objekt má nějaké vlastnosti.
# Nejlepším přítelem programátora je internet - prostě to vygooglíme, nikdo si to nepamatuje všechno nazpaměť.
# https://www.w3schools.com/python/python_lists_methods.asp např. zde najdeme, co všechno seznam umí
# Ukažme si některé metody na tomto seznamu náhodných čísel:
seznam_pismen = ['a','a','b','b','p','b','w','x','l','f','g','h','o','k','s']
seznam_pismen.append('d') # přidám písmeno na konec
print("Poslední písmeno (prvek) seznamu je " + seznam_pismen[-1] + ".") # kouknu se na poslední prvek a vidím, že append funguje správně

seznam_pismen.pop() # metodou pop() smažu prvek z KONCE seznamu
print("Poslední písmeno (prvek) seznamu je " + seznam_pismen[-1] + ".") # když se znovu podívám na konec, už tam není 'd' - to bylo odstaněno

pocet_a = seznam_pismen.count('a') # metodou count() můžu spočítat, kolikrát se něco vyskytuje v seznamu
print("Písmeno 'a' se v seznamu vyskytuje " + str(pocet_a) + " krát.")

pozice_x = seznam_pismen.index('x') # metoda index() mi zjistí na jaké pozici se vyskytuje nějaký prvek POPRVÉ (od začátku)
# Ale pozor, pokud se prvek v seznamu nevyskytuje vůbec, nastane ERROR!
print("První výskyt písmene 'x' je na pozici " + str(pozice_x) + ".")

print(seznam_pismen) # vytisknu si seznam
seznam_pismen.reverse() # metodou reverse() můžu seznam otočit (poslední prvek bude první, první poslední atd.)
print(seznam_pismen) # znovu vytisknu seznam a vidím, že první je písmeno "s"

seznam_pismen.sort() # metodou sort() můžu seznam seřadit
print(seznam_pismen) # a máme seřazený seznam podle abecedy!

"""
Úkol 0: Náhodný list 

Udělejte si list, který bude obsahovat 100 náhodných čísel od -100 do 100.
Bonus: Zeptejte se uživatele kolik chce čísel a z jakého rozsahu.
Inspirujte se kódem pro vygenerování náhodného čísla níže.
"""
# generování náhodného čísla
import random
nahodne_cislo = random.randrange(-100,100) # takto vygeneruju jedno náhodné číslo v rozmezí -100 až 100
# teď to jen udělat vícekrát a nasypat to do listu!

cisla = [] # prázný seznam je dobrý začátek... zbytek je na vás!


"""
Úkol 1: Součet čísel v seznamu.

Sečtěte všechna čísla v listu a vypište součet. Využijte k tomu while cyklus.
Až to budete mít, zkuste najít (nebo se zeptejte) jak to udělat jednodušeji.
"""

cisla = [25, -36, 62, 70, 91, -32, 93, 65, 0, 55, 40, -39, 52, 0, 21, 21, 61, -100, -26, 73, 65, 24, -22, 57, 91, -45, 84, 26, -73, -47, 15, 64, 13, -20, 76, 41, -81, -74, 56, -18, -78, 10, -89, 83, 3, -40, 52, 73, 65, -11, -37, 58, -56, 94, -12, 57, -28, 88, -56, -72, -21, 40, -16, 23, 28, 42, -9, 97, 70, 11, 69, 9, -64, -71, -36, -100, 73, -7, -59, -82, 10, 4, 73, -1, -64, 15, -18, 50, 79, -91, 82, 1, -67, -58, 5, -14, -25, -50, 67, 70]

soucet = 0 # na začátku bude součet nula (prázdná krabička, kam budu přidávat jednotlivá čísla)
delka_seznamu = len(cisla) # uložím si do proměnné délku seznamu
poradi = 0 # udělám si proměnnou, která bude určovat, které číslo ze seznamu (na jaké pozici) právě přičítám do součtu
# udělám si cyklus - postupně projdu celý seznam
while poradi < delka_seznamu: # dokud nejsem na konci seznamu, jedu dál
    soucet += cisla[poradi] # přičtu do součtu aktuální číslo
    poradi += 1 # posunu pořadí o jedna -> příští cyklus budu přičítat "další" číslo

print("Součet všech čísel v seznamu je: " + str(soucet) + ".")

"""
Úkol 2: Sudé nebo liché?

Na základě původníh seznamu čísel udělejte další dva seznamy. Jeden, který bude obsahovat všechna lichá čísla z původního seznamu a druhý, který v sobě bude mít čísla sudá.
Využij operátor modulo (zbytek po dělení).
"""

#TODO

"""
Úkol 3: Extrémy

Vemte si seznam čísel a najděte v něm největší a nejmenší číslo. 
"""


"""
Úkol 4: Tombola

Nasimulujte tombolu. Pomocí seznamu jmen vylosujte náhodného člověka (nebo více), kteří vyhrají nějakou cenu.
Můžete využít metodu shuffle a generátor náhodných čísel.
"""

import random
nahodne_cislo = random.randrange(-100,100) # takto vygeneruju jedno náhodné číslo v rozmezí -100 až 100