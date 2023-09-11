"""
██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

"""
Úloha 1: Search and Destroy 💣

Každá střílečka má herní mód Search and Destroy. Hráči jsou rozděleni do dvou týmů, úkolem prvního týmu je položit bombu.
Bomba od položení začne odpočítávat čas do výbuchu, mezitím druhý tým se snaží bombu deaktivovat, než uplyne čas.
Tvým úkolem je rekurzivně naprogramovat funkci, která bude odpočítávat čas do výbuchu.

Je na tobě, jestli budeš skutečně čekat (např. pomocí příkazu sleep), nebo čísla jen najednou vypíšeš. 
Pokud ale program bude opravdu čekat 1 sekundu mezi odpočty, bude to vypadat lépe. (Zeptej se mě, googlu nebo ChatGPT)
"""

def casomira_vybuch(cas):
    # TO-DO: Zde napiš svůj kód (parametr cas jsou sekundy do výbuchu)
    pass


"""
Úloha 2: Random ❓

Udělej funkci, která vygeneruje náhodné číslo od nuly do sta. Pokud je číslo dělitelné deseti, zastaví se, pokud ne, zavolá se znovu.
Čísla vypisuj pomocí print. Výstupem programu budou tedy náhodná čísla o nuly do sta, která nebudou dělitelná 10.

"""

def generuj():
    # TO-DO: Sem piš svůj kód
    pass

"""
Úloha 3: Rekurzivní mocnina

Naprogramujte rekurzivní funkci, která vypočte mocninu zadaného čísla (základ) na zadanou celočíselnou mocninu (exponent).

Příklad:
mocnina(3, 4) = 3 * 3 * 3 * 3 = 81
"""

def mocnina(zaklad, exponent):
    # TO-DO: Sem napiš svůj kód
    pass
    # return ?

"""
Úloha 4: Fibonacciho čísla

Udělej funkci, která spočítá n-té Fibonacciho číslo. První Fibonacciho číslo je 0, druhé je 1. Každé další vznikne tak, že se sečtou dvě čísla předchozí.
Příklad:
0 1 1 2 3 5 8 13 21 34 55 ...

Pokud uživatel chce např. sedmé Fibonacciho čísla, tvůj program vypíše: 8
"""


def fibonacciho_cislo(poradi):
    # TO-DO: Sem napiš svůj kód
    pass
    # return ?


"""
Úloha 5*: Rekurzivní binární vyhledávání

Naprogramujte rekurzivní funkci pro binární vyhledávání, která vrátí index hledaného prvku v seřazeném seznamu nebo -1, pokud prvek v seznamu není.

Příklad:
binarni_vyhledavani([1, 3, 5, 7, 9], 5) = 2
binarni_vyhledavani([1, 3, 5, 7, 9], 8) = -1
"""

"""
Úloha 6**: Schody

Stojíš dole pod schodištěm, které má X schodů. Můžeš buď udělat normální krok nahoru, tj. o jeden schod, nebo jeden schod přeskočit (velký krok).
Udělej funkci, která spočítá, kolik je celkem všech možných způsobů, jak se dají schody vylézt (různé sekvence kroků). 

"""


def schody(pocet_schodu):
    pass