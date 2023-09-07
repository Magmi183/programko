"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

"""
Úkol 1: Horská dráha

Zeptejte se uživatele kolik měří centimetrů.
Pokud má 180 a více, řekněte mu, že může na horskou dráhu.
Pokud má méně, s lítostí mu oznamte, že kvůli bezpečnostním důvodům na horskou dráhu bohužel nesmí.

"""

"""
Úkol 2: Porovnávač čísel

Načtěte od uživatele dvě čísla a řekněte, jestli jsou stejná. Pokud nejsou, 
řekněte, jestli je větší první, nebo druhé číslo.
"""



"""
Úkol 3: Známkování testu

Zeptejte se uživatele kolik dostal bodů z testu. 
Podle počtu bodů mu udělte známku.
Známkování si vymyslete. Např. 40 a více bodů jednička, 35 a více bodů dvojka... 20 a méně bodů za pět. Můžete se inspirovat touhle tabulkou:
< 50    5
50 - 69 4
70 - 79 3
80 - 89 2
90 +    1
"""


"""
Úkol 4: Největší číslo

Načtěte od uživatele tři čísla a řekněte, které z nich je největší. Pokud je největších čísel více, napište to uživateli.
"""

"""
Úkol 5: Pokuta

Udělejte program, který na základě informací o rychlosti a lokaci řidiče vyhodnotí, jestli dostane pokutu, případně jak bude velká.
Uživatel zadá tři informace:
    - rychlost v kilometrech za hodinu (km/h)
    - z jaké je země (Německo nebo ČR), jiné země program nezná
    - jestli je to policajt (ano/ne)
    
PRAVIDLA:
Pokud je uživatel policajt, nikdy žádnou pokutu nedostane, protože byl na služebním výjezdu.
Pokud je uživatel z NĚMECKA, tak platí jediné pravidlo - pokud jede 0 km/h, tedy stojí, dostane pokutu 1 milion kč,
v ostatních případech ale nedostane nic - v Německu na dálnici není rychlostní omezení.
Pokud je ale z ČR, tak:
    - pokud jede 0 km/h, dostane pokutu 1 milion kč za stání na silnici
    - pokud jede mezi 1 - 130 km/h tak pokutu nedostane
    - pokud jede více než 130 km/h, dostane pokudu 1000 kč
    
Na základě vstupu od uživatele rozhodněte a vypište výši pokuty.
"""

rychlost = int(input("Zadej rychlost:\n"))
zeme = input("Zadej zemi: (Německo nebo ČR):\n")
policie = input("Jsi policie? Zadej ano/ne:\n")


"""
Úkol 6: Trojúhelník

Zeptejte se uživatele na 3 čísla - délky stran trojúhelníku.
Řekněte mu, jestli je trojúhelník platný. Aby byl trojúhelník platný, ani jedna ze stran nesmí být větší, než zbylé dvě dohromady.

"""

strana1 = float(input("Zadej 1 stranu: \n"))
strana2 = float(input("Zadej 2 stranu: \n"))
strana3 = float(input("Zadej 3 stranu: \n"))


"""
Úkol 7: Progresivní daň

Zeptejte se uživatele, kolik dostal peněz a spočítejte mu, kolik celkem zaplatí na daních.

Pokud má uživatel příjem menší nebo rovno 100 tisíc, zaplatí daň 15 procent.
Pokud má více, zaplatí daň 15 procent z prvních 100 tisíc, ale peníze nad 100 % zdaní sazbou 23 procent.
Pokud je to zloděj, na daních nezaplatí nic.
"""
zlodej = input("Jsi zloděj? Zadej ano nebo ne.")
prijem = int(input("Zadej příjem: \n"))