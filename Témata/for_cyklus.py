# Hezké vysvětlení for cyklu je zde: https://www.umimeprogramovat.cz/programovani-cyklus-for

"""
For cyklus podobně jako while cyklus slouží k tomu, když chceme vykonat nějaký blok kódu vícekrát.
Narozdíl od while cyklu, který se opakuje dokud je splněná podmínka, for cyklus se provede tolikrát, kolik
např. prvků má seznam/string na které for cyklus voláme, nebo počet opakování přímo určíme metodou range.

Ve for cyklus totiž narozdíl od while NENÍ ŽÁDNÁ PODMÍNKA, rovnou mu řekneme kolikrát se má provést a jak.
"""

"""
Třeba když máme seznam a chceme ho celý vypsat, hodí se for cyklus. Pomocí while cyklu jsem to zvládli taky,
ale museli jsme si nejdříve zjistit délku seznamu, udělat počítadlo atd. S for cyklem to vůbec řešit nemusíme. 
Porovnejte sami:
"""

ucastnici = ["Vítek", "Vojta", "Adam", "Tonda", "Kuba", "Sam", "David"]

# while cyklus:
pocet_ucastniku = len(ucastnici)
pocitadlo = 0
while pocitadlo < pocet_ucastniku:
    print("Ahoj " + ucastnici[pocitadlo])
    pocitadlo += 1
# for cyklus:

for ucastnik in ucastnici:
    print("Ahoj " + ucastnik)

# ... o dost hezčí co? For cyklus dostal seznam (ucastnici) a funguje tak, že se provede tolikrát, kolik je prvků v seznamu.
# Navíc mám možnost si v rámci for cyklu udělat proměnnou (ucastnik) která postupně bude nabývat hodnot z listu.
# Takže v prvním cyklu je ucastnik Vítek, pak Vojta, pak Adam ... A rovnou je pozdravím a nemusím přistupovat do listu,
# tak jako u while cyklu.

# Proměnné ucastnik se říká ŘÍDÍCÍ PROMĚNNÁ. Jak lze vidět, v průběhu cyklu mění svou hodnotu. Jakých hodnot nabývá určuje
# část za "in". Když tedy napíšeme "ucastnik in ucastnici" říkáme tím, že cyklus se provede pro každého ucastnika a řídící
# proměnná (ucastnik) bude postupně nabývat hodnot ze seznamu ucastnici.

# Stejnou myšlenku můžeme aplikovat i na string - postupně pomocí for cyklu projít všechny znaky, které obsahuje.
# Opět porovnáme oba přístupy. Chceme vypsat postupně všechna písmena abecedy (která máme v jednom stringu).

abeceda = "abcdefghijklmnopqrstuvwxyz"

# WHILE:
delka_abecedy = len(abeceda)
pocitadlo = 0
while pocitadlo < delka_abecedy:
    print(abeceda[pocitadlo])
    pocitadlo += 1

# FOR cyklus:

for pismeno in abeceda: # můžeme číst jako: "pro každé písmeno v abecedě (pro každý znak ve stringu) udělej něco"
    print(pismeno)

# ... řídící proměnná je v tomto případě "pismeno", tato proměnná postupně nabývá všech hodnot ze stringu abeceda a cyklus
# se tedy provede tolikrát, kolik má string abeceda písmen - proto nemusím napřed počítat jeho délku a dělat si počítadlo
# jako u while cyklu.

#########
# Často chceme, aby se cyklus opakoval a dopředu známe přesný počet opakování. K tomu se hodí metoda range, kde přímo
# řekneme kolikrát chceme aby se cyklus opakoval. Mechanismus je stejný jako když používáme for cyklus se seznamem/stringem,
# akorát řídící proměnná nabývá hodnot z nějakého rozsahu čísel, který udáme v metodě range. Ukážeme si na příkladech.

# RANGE
# tato metoda se hojně používá spolu s for cyklem
# pokud jí dáte jeden parametr (číslo), generuje hodnoty od 0 až do toho čísla
# pokud dostane dva parametry, generuje čísla v rozmezí
# případný třetí parametr udává step (skok), tedy o kolik se hodnota zvětší po každém cyklu

# proměnná i postupně nabývá hodnot 0 - 9, cyklus se tedy provede 10x
for i in range(10): # range vygeneruje čísla 0 1 2 3 4 5 6 7 8 9 a řídící proměnná postupně nabývá těchto hodnot
    print(i)

# proměnná i postupně nabývá hodnot 1 - 10, cyklus se tedy provede 10x
for i in range(1,11):
    print(i)

# proměnná i nabývá sudých hodnot od 2 do 99 (2 4 6 8 ... 94 96 98) - skok je dva
for i in range(2,100,2):
    print(i)

# často nás hodnota řídící proměnné nezajímá a prostě něco chceme udělat a známe přesný počet opakování, k tomu
# se také hodí použí range, ale zkrátka nevyužijeme hodnotu řídící proměnné. Dejme za příklad, když chceme 10x pozdravit
# našeho milého uživatele.

for x in range(10):
    print("Ahoj milý uživateli.")

# ... jak lze vidět, o proměnnou x se uvnitř cyklu nezajímám.

# OPERÁTOR IN
# Operátor in se dá používat i v podmínkách - jednodušše nám řekne, jestli se danná hodnota vyskytuje v seznamu/stringu
# apod. na který se ptáme.

if "a" in "Michal":
    print("Slovo Michal obsahuje písmeno a.")

# dá se napsat i "not in" - to dělá opak, podmínka platí, pokud se hodnota v seznamu NEvyskytuje
if "a" not in ["a","c","traktor"]:
    print("Seznam neobsahuje písmeno a.")

# Ukázky použití:

# Ukázka 1:
# Program na určení parity (sudé/liché) čísla:
n = 100
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, "je sudé")
    else:
        print(i, "je liché")

# Ukázka 2:
# Součet čísel od někam do někam (podle proměnných od/do)
# (to jsme dělali u while cyklu, s forem je to mnohem jednodušší!)
od = 0
do = 10
soucet = 0
for cislo in range(od, do+1): # POZOR! Pokud chceme zahrnout i číslo "do", musí být ve foru do+1
    soucet = soucet + cislo
print("Součet od " + str(od) + " do " + str(do) + " je " + str(soucet))


"""
Úkol 1: Vypsat čísla od 1 do 100

Vypište čísla od 1 do 100, každé na nový řádek. Využijte for cyklus.
"""


"""
Úkol 1.5: Seznam čísel od 1 do 100

Vytvořte seznam, který bude obsahovat čísla od 1 do 100. Využijte for cyklus.
"""


"""
Úkol 2: Seznam lichých čísel

Vytvořte seznam lichých čísel mezi čísly 1 až 100.

"""


"""
Úkol 3: Součet čísel od 50 do 100

Pomocí cyklu while udělejte program, který spočítá součet čísel od 50 do 100 (včetně).

"""

# ZDE JSEM SKONCIL: TODO doplnit ulohy ( 5 a dál zkontrolovat), sibenice + ukol z nuda.py
# + samozrejme reseni ukolu