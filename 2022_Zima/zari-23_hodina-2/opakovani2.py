# PŘIPOMENUTÍ FOR CYKLU

for i in range(10): # range vygeneruje čísla 0 1 2 3 4 5 6 7 8 9 a řídící proměnná (to je to i)postupně nabývá těchto hodnot
    print(i)

# proměnná i postupně nabývá hodnot 1 - 10, cyklus se tedy provede 10x
for i in range(1,11):
    print(i)

"""    
Zkrátka for cyklu dáme něco, co může rozdělit na kousky, cyklus se pak provede tolikrát, kolik je
těch kousků a řídící proměnná (nahoře v příkladech "i") postupně nabývá hodnot těch "kousků". Např.
u řetězce jsou to písmena, u range jsou to čísla z rozsahu, u seznamu jsou to jeho prvky atd.
"""

jmena = ["Michal", "Kamil", "Jarek", "Dominik", "Jirka", "Sultán"]

for jmeno in jmena:
    # proměnná jmeno postupně nabývá všech hodnot (jmen) ze seznamu jmena
    # v každé iteraci vypíšu pozdrav - nakonec budou všichni pozdraveni
    print("Ahoj, " + jmeno)



#
#   ÚKOL NA FOR CYKLUS
#
"""
Úkol opakování na for cyklus: Legit pyramida

Zeptejte se uživatele jak vysokou chce mít pyramidu a následně mu ji vytiskněte. V horním patře pyramidy je jedna hvězda,
pak s každým patrem o dvě více.
Například legit pyramida výšky 5 vypadá takto:
    *
   ***
  *****
 *******
*********

Nápověda:
 - použijte for cyklus s metodou range, promyslete si kolik má být mezer na každém řádku a kolik hvězdiček přidáváte v každém cyklu
 - promyslete si, kolik je mezer před hvězdičkou na prvním řádku
 - kolik mezer ubývá s každým řádkem?
"""

vyska = int(input("Zadej jak vysokou chceš pyramidu: \n"))



############################################################################################################################################################################################################################
############################################################################################################################################################################################################################
############################################################################################################################################################################################################################
############################################################################################################################################################################################################################

# PŘIPOMENUTÍ SEZNAMŮ


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

# pro vypsání všeho ze seznamu můžu použít for cyklus:
for zavodnik in zavodnici:
    print(zavodnik) # takhle vypisuji závodniky pod sebe tak, jak jsou v pořadí v seznamu

# Seznam v Pythonu umí SPOUSTU dalších věcí. Je to takzvaný objekt. A každý objekt má nějaké vlastnosti.
# Nejlepším přítelem programátora je internet - prostě to vygooglíme, nikdo si to nepamatuje všechno nazpaměť.
# https://www.w3schools.com/python/python_lists_methods.asp např. zde najdeme, co všechno seznam umí
# Ukažme si některé metody na tomto seznamu náhodných čísel:
seznam_pismen = ['a','a','b','b','p','b','w','x','l','f','g','h','o','k','s']
seznam_pismen.append('d') # !!!!! PŘIDÁNÍ DO SEZNAMU !!!!!
print("Poslední písmeno (prvek) seznamu je " + seznam_pismen[-1] + ".") # kouknu se na poslední prvek a vidím, že append funguje správně

seznam_pismen.pop() # metodou pop() smažu prvek z KONCE seznamu
print("Poslední písmeno (prvek) seznamu je " + seznam_pismen[-1] + ".") # když se znovu podívám na konec, už tam není 'd' - to bylo odstaněno

seznam_pismen.pop(0) # do metody pop() můžu dát číslo, když to udělám, smaže se prvek na danné pozici
# (když tam číslo nedám, automaticky se maže od konce)
print(seznam_pismen) # vidím, že mi zmizel první prvek, už mám v seznamu jen jedno áčko

seznam_pismen.remove('b') # metodou remove() můžu odstranit konkrétní hodnotu ze seznamu, ale pozor, odstraní se jen první výskyt
# v našem případě se tedy odstraní jedno písmeno 'b' a dvě zůstanou

pocet_a = seznam_pismen.count('a') # metodou count() můžu spočítat, kolikrát se něco vyskytuje v seznamu
print("Písmeno 'a' se v seznamu vyskytuje " + str(pocet_a) + " krát.")

pozice_x = seznam_pismen.index('x') # metoda index() mi zjistí na jaké pozici se vyskytuje nějaký prvek POPRVÉ (od začátku)
# Ale pozor, pokud se prvek v seznamu nevyskytuje vůbec, nastane ERROR!
print("První výskyt písmene 'x' je na pozici " + str(pozice_x) + ".")


"""
ÚKOL NA OPAKOVÁNÍ 

Udělejte si list, který bude obsahovat 100 náhodných čísel od -100 do 100.
Bonus: Zeptejte se uživatele kolik chce čísel a z jakého rozsahu.
Inspirujte se kódem pro vygenerování náhodného čísla níže.

DÁLE:
1. Udělejte součet těchto čísel
2. Spočítejte kolik je tam čísel větších než 50.
3. Smažte ze seznamu všechna záporná čísla.
4. Seznam vypište.

Nápověda: 
- pro přidání nečeho do seznamu použijte metodu append
- pro spočítání součtu využijte for cyklus, udělejte si proměnnou kde budete postupně přičítat čísla
- pro smazání prvku využijte metodu remove, např. seznam.remove(-1) ze seznamu smaže jedno číslo -1
- pro vypsání klidně udělejte jen print(seznam)
"""
# generování náhodného čísla
import random
nahodne_cislo = random.randrange(-100,100) # takto vygeneruju jedno náhodné číslo v rozmezí -100 až 100
# teď to jen udělat vícekrát a nasypat to do listu!

cisla = [] # prázný seznam je dobrý začátek... zbytek je na vás!




