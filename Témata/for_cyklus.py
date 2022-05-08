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

######
# Často nás hodnota řídící proměnné nezajímá a prostě něco chceme udělat a známe přesný počet opakování, k tomu
# se také hodí použí range, ale zkrátka nevyužijeme hodnotu řídící proměnné. Dejme za příklad, když chceme 10x pozdravit
# našeho milého uživatele.

for x in range(10):
    print("Ahoj milý uživateli.")

# ... jak lze vidět, o proměnnou x se uvnitř cyklu nezajímám.

# ####
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

# Pozor, poslední číslo už se "nepočítá", proto pokud chci vypsat i 100, musí být range do 101
for i in range(1, 101):
    print(i) # prostě vypíšu hodnotu řídící proměnné, to je vše

"""
Úkol 1.5: Seznam čísel od 1 do 100

Vytvořte seznam, který bude obsahovat čísla od 1 do 100. Využijte for cyklus.
"""
cisla_seznam = [] # na začátku si udělám prázdný seznam

# zbytek je stejný jako předtím, akorát místo výpisu přidávám čísla do seznamu
for i in range(1, 101):
    cisla_seznam.append(i)

"""
Úkol 2: Seznam lichých čísel

Vytvořte seznam lichých čísel mezi čísly 1 až 100.
"""

licha_cisla = []

for i in range(1, 101):
    if i % 2 == 1: # Pokud číslo vydělím 2 a zbyde mi 1, číslo je liché
        licha_cisla.append(i)
print("Seznam lichých čísel: " + str(licha_cisla))

"""
Úkol 3: Součet čísel od 50 do 100

Pomocí cyklu while udělejte program, který spočítá součet čísel od 50 do 100 (včetně).
BONUS: Dejte uživateli možnost zvolit si rozsah čísel, který chce sečíst. (Sám si urči "od" a "do".)
"""
soucet = 0

for cislo in range(50, 101):
    soucet += cislo

print("Součet čísel od 50 do 100 je: " + str(soucet))

"""
Úloha 4:
Máte 2 seznamy - seznam lidí a seznam známek.
1. člověk v seznamu lidí dostal 1. známku ze seznamu známek.
2. člověk 2. známku atd.
Vaším úkolem je vytvořit program, který se opakovaně ptá na jméno a následně řekne, jakou má ten člověk známku,
případně že ho nezná. Program může klidně běžet do nekonečna (while True) nebo naprogramujte mechanismus jeho ukončení.
např:
znamky = [4, 5, 1, 2, "2-"]
jmena = ["Kamil", "Michal", "Jarek", "Anezka", "Hugo"]
"""
# TODO: Koment this kod
znamky = [4, 5, 1, 2, "2-"]
jmena = ["Kamil", "Michal", "Jarek", "Anezka", "Hugo"]

while True:
    jmeno = input("Zadej jméno: \n")
    if jmeno in jmena:
        for i in range(len(jmena)):
            if jmena[i] == jmeno:
                print(jmeno + " dostal známku: " + str(znamky[i]) + ".")
    else:
        print("Toto jméno neznám. Zkus to znovu.")

    if jmeno == "KONEC PLS":
        break

"""
HRA - Šibenice:
Úkolem je naprogramovat hru Šibenice.
V programu je slovo, které se uživatel snaží uhodnout. Na začátku vidí místo písmen ve slově
jen samé hvězdičky. Hráč začíná s 10 životy.
Každé kolo hráč buď: 1) tipne písmeno
                     2) tipne celou hádanku
V případě, že tipne celou hádanku - hra končí. V případě, že tipne jedno písmeno se odkryjí
všechny hvězdičky, na jejichž pozici se písmeno nachází. Pokud se písmeno ve slově nenachází vůbec, tak
hráč ztrácí život.

Začněte základní verzí hry a postupně ji vylepšujte. Slovo, které bude uživatel hádat si pro začátek vymyslete.

DOPORUČENÍ: - Ze začátku si vymyslete tajenku, která bude používat buď jen malá, nebo jen velká písmena.
            - Nepoužívejte háčky a čárky.
"""
# TODO: Koment this kod
tajenka = "Zaciname s programovanim"
uhodnuto = "******** * *************"

zivotu = 10

spatne = []
dobre = []

while uhodnuto != tajenka and zivotu >= 0:

    print(f"Zbývá ti {zivotu} životů. Dobře jsi uhodl písmena {dobre}, špatně písmena {spatne}. \n"
          f"Aktuální stav tajenky je: {uhodnuto}. ")
    tip = input("Hádej písmeno! \n")
    ok_vstup = False
    while not ok_vstup:
        if tip in dobre or tip in spatne:
            tip = input("Tohle písmeno už jsi hádal, zkus to znovu: \n")
        elif len(tip) != 1 or not tip.isalpha():
            tip = input("Neplatný vstup: \n")
        else:
            ok_vstup = True

    tip = tip.lower()

    if tip in tajenka.lower():
        print("Hezky! Tohle písmeno jsi zandal správně.")
        for index in range(len(tajenka)):
            if tajenka[index].lower() == tip:
                uhodnuto = list(uhodnuto)
                uhodnuto[index] = tajenka[index]
                uhodnuto = "".join(uhodnuto)
        dobre.append(tip)
    else:
        print("Bohužel... Máš o jeden život méně.")
        spatne.append(tip)
        zivotu -= 1

if zivotu <= 0:
    print("Prohrál jsi...")
    print("Tajenka byla: " + tajenka)
else:
    print("Vyhrál si! Gratuluji.")


# TODO: ZKONTROLOVAT
# TODO: Pridat ulohy? 5+ v o.z., a dalsi mozna OC ?
