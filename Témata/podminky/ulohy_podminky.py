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
Úkol 5: Studium na vysoké škole

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