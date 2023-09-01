"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

# TODO 2023: Zpracovat

"""
Úloha x: Kluk

Třída Kluk obsahuje tyto atributy:
    - jmeno: jméno kluka
    - vek: věk kluka
    - oblibena_cinnost: jeho oblíbená činnost

Dodělejte metody v této třídě.
    - predstav_se(self): Vypíše představení, např.: "Ahoj, jsem Milan, je mi 50 let a mám rád pití vody."
    - zestarni(self, pocet_let): Zvýší věk kluka o pocet_let.
"""

class Kluk:

    def __init__(self, jmeno, vek, oblibena_cinnost):
        self.jmeno = jmeno
        self.vek = vek
        self.oblibena_cinnost = oblibena_cinnost

    def predstav_se(self):
        # ZDE DODĚLEJTE
        print("")

    def zestarni(self, pocet_let):
        # ZDE DODĚLEJTE
        pass



"""
Úloha x: Kostka

Dokončete následující třídu HerniKostka. Tato třída slouží k simulací hodů kostkou.

Konstruktor (__init__) má jeden parametr - POČET STĚN, který udává, kolik stěn kostka má.
Výchozí hodnotou tohoto parametru je 6, tzn. pokud uživatel nespecifikuje žádné číslo, bude mít kostka 6 stěn,
což znamená, že na ni budou padat čísla od 1 do 6.

HerniKostka musí mít metodu hod(), která vrátí náhodné číslo od 1 do počtu stěn kostky (simulace hodu).

"""


class HerniKostka:

    # ZDE: Udělejte metodu __init__

    def hod(self):
        # ZDE: vygenerujte a vraťte náhodné číslo
        pass



"""
Velká Úloha: RODOKMEN

Úlohu najdeš ve složce Témata/OOP/Vetsi_Ulohy.
"""


"""
Velká Úloha: LOKACE

Úlohu najdeš ve složce Témata/OOP/Vetsi_Ulohy.
"""



""" ZATÍM POUZE NÁPAD
TODO: Zpracovat OOP úlohu na toto téma

Tanková hra:

Dva tanky, každý ovládaný jedním hráčem, se střídají v střelbě na sebe. Hráči mohou měnit úhel a sílu střely.
Terén může být reprezentován různými znaky a může se měnit po každém zásahu.

"""