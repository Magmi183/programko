#### REPLIT !!! 10 minut

#### OPAKOVÁNÍ 15 minut

print("Michal")
print("""M
i
ch
a
l""")

# Můžeme vypsat více věcí, oddělíme je čárkou
print("Dnes je rok ", 2022)

# Obyčejný input - čekáme, až uživatel něco napíše, ale pak jdeme dál a nic s tím neděláme
input()

# Lepší je input používat i s otázkou - jinak uživatel těžko pozná, že se ho program na něco ptá
input("Kolik je ti let?")

# Výsledek si můžeme také uložit do proměnné - to budeme chtít většinou dělat.
# Jinak totiž hned zapomeneme, co nám uživatel řekl.
uzivateluv_vek = input("Kolik je ti let?")
print("Je ti ",uzivateluv_vek, " let.")

## ÚKOL NA ZOPAKOVÁNÍ (a pak na něj navážeme)
"""ÚKOL: KVÍZ
   Udělejte program, který se uživatele zeptá na nějakou otázku a vypíše mu 4 možnosti odpovědi (a, b, c, d).
   Pomocí příkazu input() načtěte uživatelovu odpověd. Odpověď pak vypište.
   Ještě uživateli nebudeme říkat, jestli odpověděl správně - ale dostanem se k tomu ještě dnes.
"""
print("Jaká je nejvyšší hora světa?")
print("")
print("a) Smrk")
print("b) Sněžka")
print("c) Mariánský příkop")
print("d) Mt. Everest")
odpoved = input()
print("Tak ty si myslíš, že odpověď je ", odpoved, "... Jestli to máš správně ti ale zatím neřeknu.")

#### PROMĚNNÉ 10 minut

# Co je to proměnná?
# - pojmenovaný kousek paměti
# - něco jako krabička, do které si můžu něco schovat na později - pak si ji podle názvu najdu, otevřu a podívám se co v ní je
# - Je to taková krabička, úschovna - kam si uložíme nějakou hodnotu, třeba číslo a později, podle jména si můžeme hodnotu vyzvednout.

# Jak udělat proměnnou v pythonu?
# - jednodušše napíšu název proměnné (pozor na pravidla) a přiřadím do ní hodnotu
# - přiřadit hodnotu znamená napsat = a hodnotu, např.:
jmeno = "Michal"
prijmeni = "Janecek"
hra = "Minecraft"

# Hodnotu proměnných pak můžu použít např. v printu:
print("Máma mi říká: ", jmeno, "e, přestaň už hrát ten ", hra)

## TYPY PROMĚNNÝCH 10 minut
# Každá proměnná v Pythonu má nějaký typ.
# Jaký typ ? - to závisí na tom, co máme v proměnné uložené.
# V pythonu je každá proměnná objekt - v tuhle chvíli nám stačí vědet to, že každý objekt má nějaké vlastnosti - podle jeho typu.

# Jaké jsou nějaké druhy proměnných?

jmeno = "Michal" # proměnná typu string
prijmeni = "Janecek" # proměnná typu string
tel_cislo = "608381565" # proměnná typu string - ikdyž je to "číslo", pokud je v uvozovkách tak je to pro Python string
vek = 10 # proměnná typu int
kurak = False # proměnná typu boolean
neco = input() # proměnný typu string - input vrátí vždy string!! Ikdyž je na vstupu číslo.

# Práci si můžeme usnadnit přiřazením do více proměnných najednou
a = b = c = 1
a, b, c = 1,2,3

# typ proměnných si můžeme zobrazit příkazem type
print(type(jmeno))
print(type(vek))

#### STRING 15 minut
# Proměnná, v které máme uložený text, je typu String.
# Pro vytvoření stringu použijeme uvozovky.
# Co je v uvozkovách, to je string!
# String má spoustu užitečných vlastností... Jaké vás napadnou?
# Můžeme se podívat třeba sem: https://www.w3schools.com/python/python_ref_string.asp

text = input("Zadej nějaký text a já ti o něm řeknu informace\n:")
print("Text je dlouhy: ", len(text))
print("Písmeno a se v textu vyskytuje: ", text.count('a'), " krát.")

# Můžu se podívat, jestli text začíná na nějaké písmenko - funkce (vlastnost) startswith mi řekne True/False
print(text.startswith('a'))
print(text.startswith('b'))
print(text.startswith('c'))

jmeno = "MICHAL"
jmeno = jmeno.lower() # převedení stringu na malá písmena
print(jmeno)
jmeno = jmeno.upper() # převedení na velká písmena
print(jmeno)
# Pozor! Nestačí napsat jmeno.lower()!! Nezapomínat na přiřazení.

## ÚKOL:
# Úloha 1 - odpoved na kviz:
# Vemte si váš kvíz (z úlohy na příkaz print).
# Nechte uživatele napsat odpověď a pomocí některé z funkcí, které můžete volat na stringu, např. startswith vymyslete
# program, který napíše True/False na základě toho, zdali uživatel odpověděl na otázku správně.

# Způsobů, jak to naprogramovat je nekonečně. Tady je jeden z nich.

print("Jaká je nejvyšší hora světa?")
print("")
print("a) Smrk")
print("b) Sněžka")
print("c) Mariánský příkop")
print("d) Mt. Everest")

odpoved = input()
print(odpoved.lower().startswith('d'))

# INTEGER, FLOAT

# integer, zkráceně int je celočíselná proměnná
# vytvořím jej přiřazením celého čísla do proměnné
a = 15

# float je desetinné číslo
b = 0.5

# PŘETYPOVÁNÍ

# Co když chci třeba načíst číslo od uživatele? Říkali jsme, že input vždycky vrací string.
# Naštěstí máme způsob, jak změnit typ proměnné. Tomu se říká PŘETYPOVÁNÍ.

vek = input()
vek = int(vek)
# nebo
vek = int(input())

presny_vek = float(input())

# S proměnnými můžeme dále pracovat - vytisknout je, sčítat..
# tady je to v pohodě, sčítám texty - to python umí, prostě je spojí za sebe, takže sečtením slov dostanu větu
print("Ahoj " + jmeno + " " + prijmeni)

# Ale co když chci zobrazit i věk?
# print("Ahoj " + jmeno + " " + prijmeni + " je ti " + vek + " let.")
# ... tohle NEBUDE FUNGOVAT! Program spadne. Proč? Proměnná vek je Integer a já se jí pokouším sčítat s textem (String). To nejde.

# Jaké operace můžu s proměnnými dělat?
# - Můžu sčítat dvě čísla?
# - Můžu sčítat číslo a string?
# - Můžu násobit string intem?
# - Můžu sčítat dva stringy?



"""
Úloha 1 - easy kalkulacka:
Načtěte od uživatele 2 čísla.
Vypište jejich součet, rozdíl a produkt.
Nápověda: dejte si pozor na typy proměnných, použijte přetypování
"""


cislo1 = int(input())
cislo2 = int(input())

# Součet
print("Součet je: " + str(cislo1 + cislo2) )

# Rozdíl
rozdil = cislo1 - cislo2
rozdil = str(rozdil)
print("Rozdíl je: " + rozdil )

# Produkt

produkt = cislo1 * cislo2
print("Produkt je: " + str(produkt) )

"""
Úloha 2 - výplata
Zeptejte se uživatele, kolik pracoval hodin a jaký má plat na hodinu. Řekněte mu, kolik má dostat peněz celkem.
Program musí umět zpracovat i desetinná čísla, tedy např. 10.5 hodiny nebo plat 150.25 kč na hodinu.
"""

nahodinu = float(input("Zadej kolik máš na hodinu: "))
odpracoval = float(input("Zadej kolik si pracoval hodin: "))

print("Máš dostat zaplaceno:")
print(nahodinu*odpracoval)


"""
Úloha 3 - obrazec
Úkolem je pomocí jednoho příkazu print vytisknout obrazec, který je danný vstupem uživatele. Obrazec se skládá z textu, který je
tvořen znakem * a #
Načti od uživatele 3 čísla: 
    - 1. číslo je počet řádek obrazce
    - 2. číslo je šířka obrazce
    - 3. číslo je počet hvězdiček na řádku (a zbytek jsou #), nejdřív jsou vždy * pak až #
(Pozor, počet hvězdiček logicky nesmí být větší, než šířka řádku... tak pozor až budete zadávat čísla)

Např: pro čísla 5 (počet řádků), 10 (šířka) a 2 (počet hvězd) by se mělo ukázat toto:

**########
**########
**########
**########
**########


"""

radku = int(input())
sirka = int(input())
hvezdicek = int(input())

print(radku * (hvezdicek*"*"+(sirka-hvezdicek)*"#"+"\n"))