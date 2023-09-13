"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

"""
Úloha 1: Osoba

Představte si, že děláte aplikaci, která potřebuje udržovat informace o různých osobách. 
Je potřeba vytvořit třídu Osoba, která to bude umět.

Třída Osoba obsahuje tyto atributy:
    - jmeno: jméno osoby
    - vek: věk osoby
    - oblibena_cinnost: jeho oblíbená činnost

Dodělejte metody v této třídě.
    - predstav_se(self): Vypíše představení, např.: "Ahoj, jsem Milan, je mi 50 let a mám rád pití vody."
    - zestarni(self, pocet_let): Zvýší věk osoby o pocet_let.
    
Po zhotovení metod udělejte instanci této třídy a otestujte ji.
"""

class Osoba:

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
Úloha 2: Kostka

Dokončete následující třídu HerniKostka. Tato třída slouží k simulací hodů kostkou.
Vašim úkolem je udělat konstruktor a dvě metody dle následujícího zadání:

1) Konstruktor (__init__) má jeden parametr - POČET STĚN, který udává, kolik stěn kostka má.
   Výchozí hodnotou tohoto parametru je 6, tzn. pokud uživatel nespecifikuje žádné číslo, bude mít kostka 6 stěn,
   což znamená, že na ni budou padat čísla od 1 do 6.

2) Metoda: hod()
   HerniKostka musí mít metodu hod(), která vrátí náhodné číslo od 1 do počtu stěn kostky (simulace hodu).

3) Metoda: hod_n_krat(n)
   Dále musí mít metodu hod_n_krat(n), což je metoda s jedním parametrem N, která simuluje N hodů a vrátí jejich seznam.
   Metodu udělejte tak, že bude používat metodu hod() - tedy pokud např. N bude 3, tak metoda 3x zavolá metodu hod,
   jejíž výsledky postupně dává do seznamu, který na konci vrátí.
"""


class HerniKostka:

    # ZDE: Udělejte metodu __init__

    def hod(self):
        # ZDE: vygenerujte a vraťte náhodné číslo
        pass

   # ZDE: Udělejte metodu hod_n_krat s parametrem N


"""
Úloha 3: Kniha

Představte si, že děláte software pro online knihovnu. Je potřeba mít strukturu, která bude schopna představovat knihu.

Udělejte třídu Kniha, která:

1) Konstruktor přijímá jeden parametr: název souboru. Na každém řádku tohoto souboru je jedna stránka knihy.
   Celý soubor řádek po řádku přečtěte a uložte si seznam stránek. Kniha tedy bude mít atribut 'self.stranky', který
   bude obsahovat jednotlivé stránky.
   Stránky budou uloženy popořadě, takže třeba: self.stranky[4] bude pátá stránka (protože se čísluje od nuly).
   
   Dále má třída atribut 'aktualni_stranka', který začíná na 0 (nastavte v konstruktoru).

2) Metoda: precti()
   Tato metoda vrátí obsah aktuální stránky - podle hodnoty atributu aktualni_stranka.

3) Metoda: otoc_stranu()
   Tato metoda zvýší atribut 'aktualni_stranka' o 1. Ale pozor - stránka lze otočit jen pokud ještě nejsme na konci knihy!
   
4) Metoda: pocet_stran()
   Tato metoda vrátí celkový počet stran v knize (číslo).
   
5) Metoda: cist_od_zacatku()
   Tato metoda vrátí 'aktualni_stranka' zpět na hodnotu 0. Nevrací nic.
   
6) Metoda: precist_vse()
   Tato metoda vrátí CELÝ OBSAH knihy jako jeden velký string.
   
Soubory, které můžete použít pro testování najdete ve složce Témata/OOP/knihy. (Warning: ChatGPT generated)
"""

class Kniha:

    def __init__(self, soubor):
        self.stranky = []
        with open(soubor, encoding="utf-8") as kniha:
            for stranka in kniha:
                # tento for cyklus prochází soubor řádek po řádku (jednotlivé stránky)
                # ZDE: doplňte seznam stránek
                pass

        # ZDE: nastavte atribut aktualni_stranka

    # ZDE: doplňte ostatní metody dle zadání



"""
Velká Úloha: RODOKMEN

Úlohu najdeš ve složce Témata/OOP/Vetsi_Ulohy.
"""


"""
Velká Úloha: LOKACE

Úlohu najdeš ve složce Témata/OOP/Vetsi_Ulohy.
"""


""" 
ZATÍM POUZE NÁPAD (NEŘEŠTE)
TODO: Zpracovat OOP úlohu na toto téma

Tanková hra:

Dva tanky, každý ovládaný jedním hráčem, se střídají v střelbě na sebe. Hráči mohou měnit úhel a sílu střely.
Terén může být reprezentován různými znaky a může se měnit po každém zásahu.

"""