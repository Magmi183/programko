"""Úloha Word Counter

Úkolem je naprogramovat program, který se uživatele zeptá na nějakou větu. Uživatel napíše větu a program se ho potom
zeptá na nějaké slovo. Úkolem je říct uživateli, kolikrát se danné slovo ve větě nachází.
"""


"""
Úloha Papoušek:

Papoušek, vypujceno z: https://www.itnetwork.cz/python/zaklady/python-tutorial-promenne-zakladni-datove-typy-a-funkce
Udělejte program, který dvakrát zopakuje vstup od uživatele.
"""

print("Ahoj, jsem virtuální papoušek Lóra, rád opakuji!")
slovo = input("Napiš něco: ") #získá od uživatele vstup a uloží jej do proměnné
vysledek = slovo + " " + slovo # vytvoří novou proměnnou
print(vysledek)
input()

"""
Úloha 0 - predikce věku
Zeptejte se uživatele kolik je mu let a řekněte mu, kolik mu bude za 10 let.
"""
pass

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
Úloha 3 - auto
Zeptejte se uživatele kolik je mu let (přesně), akceptujte i desetinná čísla.
Řekněte uživateli, za jak dlouho bude moci řídit auto. (kdy mu bude 18 let)
Předpokládejte, že mu ještě nebylo 18.
"""

vek = input()
vek = float(vek)

print("Auto můžeš řídit za " + str(18-vek) + " let.")

"""Úloha 4: Cool přezdívka
Zeptejte se uživatele na jeho oblíbene číslo a oblíbené zvíře.
Sestavte mu pak z toho přezdívku tak, že na začátek dáte číslo, doprostřed zvíře a nakonec číslo.
Tedy např. pokud uživatel zvolí zvíře Slon a číslo 66, jeho přezívka bude 66Slon66.
Přezdívku mu napište.
"""

cislo = input("Zadej číslo:\n")
zvire = input("Zadej zvíře:\n")

print("Tvoje cool přezdívka je: " + cislo+zvire+cislo)

"""
Úloha 5 - obrazec
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
