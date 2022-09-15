"""
Pokročilí:
1. Vaším úkolem je zjistit, jak na tom jste.
2. Chceme co nejdřív všechno zopakovat, abychom se pak mohli naučit funkce a následně začít pracovat na nějaké hře.
3. Je potřeba si zopakovat:
   4. všechno
   5. print a input
   6. proměnné
   7. operátory
   7. podmínky
   7. cykly
   8. seznamy

V TOMTO SOUBORY JSOU ÚLOHY VHODNÉ K OPAKOVÁNÍ.
NEMUSÍTE UDĚLAT VŠECHNY, ALE ZEPTEJTE SE. Je ale nutné, abyste zvládli naprogramovat všechno.
Úlohy jsou seřazeny zhruba podle obtížnosti (v pořadí, jak jsme je dělali minulé pololetí)
"""

"""
Úloha 1 - easy kalkulacka:
Načtěte od uživatele 2 čísla.
Vypište jejich součet, rozdíl a produkt.
Nápověda: dejte si pozor na typy proměnných, použijte přetypování
"""

"""Úloha 4: Cool přezdívka
Zeptejte se uživatele na jeho oblíbene číslo a oblíbené zvíře.
Sestavte mu pak z toho přezdívku tak, že na začátek dáte číslo, doprostřed zvíře a nakonec číslo.
Tedy např. pokud uživatel zvolí zvíře Slon a číslo 66, jeho přezívka bude 66Slon66.
Přezdívku mu napište.
"""

"""
Úkol 3: Známkování testu
Zeptejte se uživatele kolik dostal bodů z testu. 
Podle počtu bodů mu udělte známku.
Známkování si vymyslete. Např. 40 a více bodů jednička,
35 a více bodů dvojka... 20 a méně bodů za pět. Můžete se inspirovat touhle tabulkou:
< 50    5
50 - 69 4
70 - 79 3
80 - 89 2
90 +    1
"""

"""
Úkol 4: Studium na vysoké škole
Udělejte program, který uživateli řekne, jestli může nastoupit na VŠ.
Podmínky jsou následující: 
- musí mu být 18 let a víc
- musí mít maturitu
- musí mít složené přijímačky
- Pokud je jeho jméno Albert Einstein, nemusí splňovat nic z výše uvedeného.

Použijte kód níže. Pro otestování programu měňte hodnoty z False na True a obráceně.
"""

vek = int(input("Kolik je ti let?\n"))
celejmeno = input("Zadej své celé jméno.\n")
maturita = True
prijimacky = True


"""
Úkol 4: Polopyramida

Zeptejte se uživatele na výšku pyramidy a vypište mu tak vysokou polopyramidu z hvězdiček.
Například polopyramida výšky 5 vypadá takto:
*
**
***
****
*****
"""

vyska = int(input("Zadej jak vysokou chceš polopyramidu: \n"))



"""
Úkol 4.5: Legit pyramida (pro rychlíky/na doma)

Stejný úkol jako polopyramida, akorát že to není polopyramida, ale legit pyramida. 
Například legit pyramida výšky 5 vypadá takto:
    *
   ***
  *****
 *******
*********
"""

vyska = int(input("Zadej jak vysokou chceš pyramidu: \n"))



"""

Úkol 5: Uhodni číslo

Udělej hru, kde uživatel bude hádat číslo, které si program myslí. 
Uživatel bude dávat tipy (má jich omezený počet, třeba 10) a pokud číslo uhodne, program končí.
Pokud uživatel neuhodl, program mu řekne, jestli je číslo co si myslí menší nebo větší.
Pokud uživatel neuhodne číslo ani na 10 pokusů, hra končí.

"""
import random
cislo = random.randrange(50)
pocet_pokusu = 10


"""
Úkol 1.5: Seznam čísel od 1 do 100

Vytvořte seznam, který bude obsahovat čísla od 1 do 100. Využijte for cyklus.
"""

"""
Úkol 3: Součet čísel od 50 do 100

Pomocí cyklu while udělejte program, který spočítá součet čísel od 50 do 100 (včetně).
BONUS: Dejte uživateli možnost zvolit si rozsah čísel, který chce sečíst. (Sám si urči "od" a "do".)
"""


"""
Úloha 4:
Máte seznam jmen - žáků ve třídě. Udělejte program, kde uživatel bude opakovaně zadávat jména a program mu bude říkat,
jestli se jméno v seznamu nachází nebo ne.
"""

jmena = ["Kamil", "Michal", "Jarek", "Anezka", "Hugo"]