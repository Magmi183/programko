"""
                            ░██████╗███████╗███████╗███╗░░██╗░█████╗░███╗░░░███╗
                            ██╔════╝██╔════╝╚════██║████╗░██║██╔══██╗████╗░████║
                            ╚█████╗░█████╗░░░░███╔═╝██╔██╗██║███████║██╔████╔██║
                            ░╚═══██╗██╔══╝░░██╔══╝░░██║╚████║██╔══██║██║╚██╔╝██║
                            ██████╔╝███████╗███████╗██║░╚███║██║░░██║██║░╚═╝░██║
                            ╚═════╝░╚══════╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
"""

# Seznam (anglicky list) je něco, kam si můžu uložit více hodnot.
# Seznamy se dobře vysvětlují rovnou na praktických ukázkách.

# Vezměme si situaci, kdy chceme pozdravit všechny účastníky našeho kroužku.
# Na to se hezky hodí mít někde nějaký seznam účastníků a pak prostě každého z nich pozdravit.

ucastnici = ["Tonda", "Kuba", "Sam", "Vojta", "Vitek", "David", "Adam"]

# A teď třeba pomocí while cyklu ...
ucastnik_cislo = 0
while ucastnik_cislo < len(ucastnici):
    print("Ahoj " + ucastnici[ucastnik_cislo])
    ucastnik_cislo += 1

# ... nebo ještě lépe, protože seznam je sekvence, tak pomocí for cyklu:

for ucastnik in ucastnici:
    print("Ahoj " + ucastnik)

# ... ale pojďme to vzít trochu od začátku.

# Nový seznam se vytváří podobně jako proměnná. Prostě napíšu jeho jméno, rovná se a na pravou stranu
# do hranatých závorek dám hodnoty, které chci v seznamu mít.

ptaci = ["kos", "čáp", "pštros", "tučňák"]

# v seznamu můžou být různé typy, např.:
bordel = [False, "dedewd", 54, 87, "Michal", 87.4] # seznam ve kterém je boolean, string, int i float

# Dokonce můžu mít seznam, ve kterém jsou další seznamy. To se hodí třeba při dělání 2D her.
piskvorky = [["x","o", "x"],
             ["x","o", "o"],
             ["o","x", "x"]]

# ---- DÉLKA SEZNAMU
# Když chci zjistit, jak je seznam dlouhý, tedy kolik je v něm věcí, využiju funkci len().
# Znát délku seznamu se mi může hodit i třeba kvůli cyklům.
print(len(ptaci))

# ... můžu si uložit do proměnné ...
delka_seznamu = len(ptaci)

print("Celkem je v seznamu " + str(delka_seznamu) + " ptáků.")
# ----

# ---- PŘÍSTUP K PRVKŮM (INDEXOVÁNÍ)
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
# ----

# ---- PROCHÁZENÍ SEZNAMU
# Nějaké možnosti jak projít celý seznam (všechny prvky) a něco s nimi udělat už jsme si ukázali. Pojďme si to shrnout.

# ---- Procházení FOR cyklem
# Jedná se o nejjednodušší způsob jak projít seznam. Hodí se v případě, když nepotřebujeme prvky v seznamu upravovat a
# nepotřebujeme nutně znát jejich pozici.
ucastnici_2 = ["Arnošt", "Marek", "Kamil", "Maty", "Mike Wazowski"]

for ucastnik in ucastnici_2:
    # nevím zde pozici účastníka, tudíž nemůžu vypsat kolikátý je a ani ho v seznamu přímo upravit (třeba přepsat)
    print("Ahoj účastníku " + ucastnik) # můžu ho např. pozdravit

# ---- Procházení FOR cyklem v kombinaci s RANGE
# Využijeme funkci range pro vygenerování sekvence, jejíž prvky budou indexy (pořadí) prvků v seznamu.
# Uděláme si takový range, jak je velký náš seznam a hodnotu řídící proměnné pak použijeme pro přístup k prvkům v seznamu.

for index in range(len(ucastnici_2)): # cyklus se provede tolikrát, kolik je délka seznamu, a v každém cyklu bude index o 1 větší (postupně 0 1 2 3 4)
    print("Ahoj účastníku " + ucastnici_2[index]) # podobně jako u předchozího příkladu můžu účastníka pozdravit, jen musím použít index k nalezení "aktuálního" procházeného účastníka

    ucastnici_2[index] = ucastnici_2[index] + " Novák" # když znám i index, můžu položku v seznamu upravit - např. všem přidat příjmení Novák

# ---- Procházení WHILE cyklem
# Seznam můžu procházet i while cyklem, ale většinou to nepřináší žádné výhody a je to akorát více práce.
# Zamyslete se jak to udělat.


#############################################################################################################
#  METODY (VLASTNOSTI) SEZNAMU                                                                              #
#############################################################################################################

# ---- PŘIDÁNÍ PRVKU do seznamu
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

# ! ! ! ! ! ! - - - > > > > VLASTNOSTI SEZNAMU < < < < - - - - ! ! ! ! ! !
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Seznam v Pythonu umí SPOUSTU dalších věcí. Je to takzvaný objekt. A každý objekt má nějaké vlastnosti.
# Nejlepším přítelem programátora je internet - prostě to vygooglíme, nikdo si to nepamatuje všechno nazpaměť.
# https://www.w3schools.com/python/python_lists_methods.asp např. zde najdeme, co všechno seznam umí
# NEJDŮLEŽITĚJŠÍ je mít povědomí o tom, co všechno se dá se seznamem dělat, detaily si můžete vždycky najít

# Ukažme si některé metody na tomto seznamu náhodných čísel:
seznam_pismen = ['a','a','b','b','p','b','w','x','l','f','g','h','o','k','s']
seznam_pismen.append('d') # přidám písmeno na konec
print("Poslední písmeno (prvek) seznamu je " + seznam_pismen[-1] + ".") # kouknu se na poslední prvek a vidím, že append funguje správně

# ODEBRÁNÍ PRVKU
seznam_pismen.pop() # metodou pop() smažu prvek z KONCE seznamu
print("Poslední písmeno (prvek) seznamu je " + seznam_pismen[-1] + ".") # když se znovu podívám na konec, už tam není 'd' - to bylo odstaněno

seznam_pismen.pop(0) # do metody pop() můžu dát číslo, když to udělám, smaže se prvek na danné pozici
# (když tam číslo nedám, automaticky se maže od konce)
print(seznam_pismen) # vidím, že mi zmizel první prvek, už mám v seznamu jen jedno áčko

seznam_pismen.remove('b') # metodou remove() můžu odstranit konkrétní hodnotu ze seznamu, ale pozor, odstraní se jen první výskyt
# v našem případě se tedy odstraní jedno písmeno 'b' a dvě zůstanou

# SPOČÍTÁNÍ PRVKŮ
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
