"""
██████╗░██████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗███╗░░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║████╗░██║██╔════╝
██████╔╝██████╔╝██║░░██║██╔████╔██║█████╗░░██╔██╗██║██╔██╗██║█████╗░░
██╔═══╝░██╔══██╗██║░░██║██║╚██╔╝██║██╔══╝░░██║╚████║██║╚████║██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝██║░╚═╝░██║███████╗██║░╚███║██║░╚███║███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝
"""

# Co je to proměnná?
# - pojmenovaný kousek paměti
# - něco jako krabička, do které si můžu něco schovat na později - pak si ji podle názvu najdu, otevřu a podívám se co v ní je
# - Je to taková krabička, úschovna - kam si uložíme nějakou hodnotu, třeba číslo a později, podle jména si můžeme hodnotu vyzvednout.

# Jak udělat proměnnou v pythonu?
# - jednodušše napíšu název proměnné (pozor na pravidla) a přiřadím do ní hodnotu
# - přiřadit hodnotu znamená napsat = a hodnotu, např.:
jmeno = "Arnost"
prijmeni = "Novotný"
hra = "LoLko"
status = "peak silver"

# Hodnotu proměnných pak můžu použít např. v printu:
print("Máma mi říká: " + jmeno + "e, přestaň už hrát to " + hra)

## TYPY PROMĚNNÝCH 10 minut
# Každá proměnná v Pythonu má nějaký typ.
# Jaký typ ? - to závisí na tom, co máme v proměnné uložené.
# V pythonu je každá proměnná objekt - v tuhle chvíli nám stačí vědet to, že každý objekt má nějaké vlastnosti - podle jeho typu.

# Jaké jsou nějaké druhy proměnných?

jmeno = "Arnost" # proměnná typu string
prijmeni = "Novotny" # proměnná typu string
tel_cislo = "608381565" # proměnná typu string - ikdyž je to "číslo", pokud je v uvozovkách tak je to pro Python string
vek = 10 # proměnná typu int (celá čísla)
presny_vek = 10.5 # proměnná typu float (desetinná čísla)
kurak = False # proměnná typu boolean (může být jen True - pravda, nebo False - nepravda/lež, lze si taky představit jako ANO/NE)
neco = input() # proměnný typu string - input vrátí vždy string!! Ikdyž je na vstupu číslo.

# PROTIP:
# Práci si můžeme usnadnit přiřazením do více proměnných najednou
a = b = c = 1
a, b, c = 1, 2, 3

# typ proměnných si můžeme zobrazit příkazem type
print(type(jmeno))
print(type(vek))

#### STRING 15 minut
# Proměnná, v které máme uložený text, je typu String.
# Pro vytvoření stringu použijeme uvozovky.
# Co je v uvozkovách, to je string!
# String má spoustu užitečných vlastností... Jaké vás napadnou?
# Můžeme se podívat třeba sem: https://www.w3schools.com/python/python_ref_string.asp
# Každý správný programátor musí umět pořádně googlit

text = input("Zadej nějaký text a já ti o něm řeknu informace\n:")
print("Text je dlouhy: ")
print(len(text))

# Proč nefunguje toto??:
print("Text je dlouhý " + len(text))
# nebo toto
print("Písmeno a se v textu vyskytuje: " + text.count('a') + " krát.")
# ... si řekneme za chvíli.

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
print(odpoved.startswith('d'))

# ... k zamyšlení: Co když uživatel zadá velké písmeno? Jak tento problém vyřešit?

# INTEGER, FLOAT

# integer, zkráceně int je celočíselná proměnná
# vytvořím jej přiřazením celého čísla do proměnné
a = 15
a = "15" # co je tady špatně? Proč to není integer? (int)

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


print(15*10)
print("15"*10)
print(10+10)
print("10"+10)
print("10"+"10")

#
print("Text je dlouhý " + str(len(text)))
# nebo toto
print("Písmeno a se v textu vyskytuje: " + str(text.count('a')) + " krát.")

