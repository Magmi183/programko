"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

# TODO 2023: Uspořádat úlohy, nějak ať to dává smysl.
# TODO 2023: Více úloh, hlavně na funkce asi.

"""
ÚLOHA: Stupidní Kámen, Nůžky, Papír
    - podmínky, while cyklus
- - - - - - - - - - - - - - - - -

Udělejte program, který s uživatelem do nekonečna bude hrát hru kámen, nůžky, papír.
Uživatel vždy zadává jako první a počítač ho VŽDY porazí. Pokud tedy uživatel zadá např. "papír", počítač odpoví "nůžky".
Po každém kole vypište aktuální skóre. (uživatel by měl mít 0 bodů, počítač by ho měl vždy porazit)

NÁPOVĚDA: Aby program běžel do nekonečna, využijte nekonečný cyklus.

"""

while True: # nekonečný cyklus
    # sem pište svůj kód
    pass


"""
ÚLOHA: MAIL CHECKER
    - práce se stringem, podmínky
- - - - - - - - - - - - - - - - -

Vytvořte jednoduchý program, který zkontroluje platnost e-mailové adresy.
ZEPTEJTE se uživatele na e-mail a následně zkontrolujte:
    1) Adresa musí obsahovat @ (zavináč)
    2) Adresa musí obsahovat . (tečku)
    3) Adresa musí končit na "com" nebo "cz"

Pokud jsou všechny podmínky splněné, řekněte uživateli OK, pokud ne tak stačí, když řeknete, že adresa je neplatná.
Nemusíte vypisovat proč.

NÁPOVĚDA: Použijte funkce count a endswith, či jiné vlastnosti stringu.
"""



"""
ÚLOHA: SMĚNÁRNA
    - slovník, while cyklus
- - - - - - - - - - - - - - - - -

Máte zadaný slovník měnových kurzů. KLÍČ ve slovníku je vždy zkratka nějaké měny (např. CZK pro naší korunu),
HODNOTA pak vyjadřuje kolik dolarů dostaneme za jednu jednotku. Např. za jednu CZK dostaneme 0.04 dolarů. To znamená,
že jeden dolar = 25 korun českých. 


Úkol 1:
    Vaším úkolem je vytvořit program, který se zeptá uživatele na:
        1) Zkratku měny, ve které má peníze
        2) Množství peněz
    Následně program vypíše, kolik dolarů za tento obnos uživatel dostane.
    Např. uživatel zadá NZD a 10, program vypíše "7.2 dolaru". 

Úkol 2:
    Pokud už máte hotový 1. úkol, dodělejte do programu funkcionalitu PŘIDÁNÍ MĚNY. Program tedy poběží v nějakém cyklu
    a opakovaně se uživatele ptá, jestli chce převést měnu (to už byste měli mít hotové z úkolu 1), nebo přidat novou.
    Pokud chce uživatel přidat novou měnu, stačí mu zadat SYMBOL a KURZ.


"""

# slovník kurzů, nijak ho neupravujte, ale použijte ho ve svém programu
dolar_kurz = {
    "CZK": 0.04,  # 1 CZK = 0.04 USD
    "EUR": 1.2,   # 1 EUR = 1.2 USD
    "GBP": 1.4,   # Britská libra
    "JPY": 0.009, # Japonský jen
    "CAD": 0.8,   # Kanadský dolar
    "AUD": 0.77,  # Australský dolar
    "CHF": 1.1,   # Švýcarský frank
    "CNY": 0.16,  # Čínský jüan
    "SEK": 0.12,  # Švédská koruna
    "NZD": 0.72,  # Novozélandský dolar
    "MXN": 0.05   # Mexické peso
}



"""
ÚLOHA: FIZZ BUZZ
    - for cyklus, podmínky
- - - - - - - - - - - - - - - - -

FizzBuzz je programátorská klasika.
Udělejte program, který vypíše všechna čísla od 1 do 100, ALE:
  - místo čísel, která jsou dělitelná 3 vypíše Fizz
  - místo čísel, která jsou dělitelná 5 vypíše Buzz
  - místo čísel, která jsou dělitelná 3 i 5 vypíše FizzBuzz

Tedy např. prvních 15 řádků bude:
            1
            2
            Fizz
            4
            Buzz
            Fizz
            7
            8
            Fizz
            Buzz
            11
            Fizz
            13
            14
            FizzBuzz
"""


""" 
ÚLOHA: ZADÁNÍ HESLA
    - funkce, cyklus
- - - - - - - - - - - - - - - - -

Úkol 1: Udělejte funkci "odpocet", která přijíma jeden parametr (pocet_sekund). Funkce má za úkol udělat odpočet
        od pocet_sekund až do 1. Např. pokud uživatel zavolá odpocet(5), tak funkce vypíše:
            Prosím počkejte ještě 5 sekund.
            Prosím počkejte ještě 4 sekund.
            Prosím počkejte ještě 3 sekund.
            Prosím počkejte ještě 2 sekund.
            Prosím počkejte ještě 1 sekund.
        Přičemž mezi každým výpisem uběhne přesně jedna vteřina.
        
        Inspirujte se kódem níže - dělá to samé, akorát to není ve funkci.

Úkol 2: Potom co máte úkol 1, rozšiřte program následovně:
        1) Uživatel si zvolí nějaké heslo.
        2) Poté se počítač začne ve while cyklu opakovaně ptát na to heslo, pokud uživatel zadá správně, tak program končí.
           Pokud ale uživatel zadá heslo chybně, musí počkat 1 sekundu, než bude moct heslo zadat znovu. Pokaždé když 
           zadá špatné heslo, musí čekat o 2 sekundy déle, než minule. Program končí až uživatel zadá heslo správně.
           K ČEKÁNÍ POUŽIJTE FUNKCI, KTEROU JSTE UDĚLALI V ÚKOLU 1!

"""

from time import sleep

# PŘEDĚLEJTE TENTO KÓD TAK, ABY BYL VE FUNKCI a POČET SEKUND SE DÁ NASTAVOVAT PARAMETREM
pocet_sekund = 5
while pocet_sekund > 0:
    print(f"Prosím počkejte ještě {pocet_sekund} sekund.")
    pocet_sekund -= 1 # snížime počet sekund
    sleep(1) # "spíme" jednu sekundu, tedy program se na jednu sekundu zastaví, než bude pokračovat do dalšího cyklu


"""
ÚKOL: Nejoblíbenější produkt
    - cyklus, slovník
- - - - - - - - - - - - - - - - -

Níže máte seznam věcí, které se prodali v lokálním obchodě. V seznamu se mnoho položek vyskytuje vícekrát, což znamená,
že se jich prodalo více kusů. Vaším úkolem je zjistit, který produkt se prodal nejvícekrát.
  
  
NÁPOVĚDA: 1) Nejdříve si vytvořte prázdný slovník, který bude sloužit k počítání jednotlivých položek.
          2) Postupně v cyklu (nejlépe ve for cyklu) procházejte seznam položku po položce. Pokud dannou položku vidíte
             poprvé, tak ji dejte do slovníku a nastavte počet na jedna. Pokud už tam položka je, zvyšte počet o 1.
          3) Nakonec projděte celý slovník (hodnotu i klíč) a najděte nejvyšší hodnotu (počet prodaných kusů) a zapamatujte
             si klíč (položka). Pokud nevíte jak na to, zeptejte se + ukázky jak procházet slovník najdete v lekci na slovník.
          
          Koukněte se na ukázky níže.
"""

# SEZNAM PRODEJŮ => vaším úkolem je zjistit, který produkt se prodával nejvíce
prodeje = [
    "banán", "okurek", "okurek", "mouka", "papaya", "banán", "okurek", "okurek", "mouka", "papaya",
    "okurek", "banán", "Targa Florio", "mouka", "okurek", "banán", "okurek", "okurek", "mouka", "okurek",
    "Coca-Cola", "okurek", "mouka", "Coca-Cola", "banán", "banán", "okurek", "Coca-Cola", "mouka", "meloun",
    "řízek", "Targa Florio", "papaya", "mouka", "okurek", "banán", "okurek", "Coca-Cola", "mouka", "papaya",
    "banán", "papaya", "Coca-Cola", "mouka", "okurek" "banán", "okurek", "Coca-Cola", "okurek", "okurek",
]


############### NÁPOVĚDA (můžete smazat)
pocet = {} # Vytvoření prázdného slovníku

# UKÁZKA PRÁCE SE SLOVNÍKEM:

if "banán" not in pocet:
    # banán ještě ve slovníku není, takže mám zatím jeden
    pocet["banán"] = 1
else:
    # banán už ve slovníku je, takže jen zvýšíme počítadlo o 1
    pocet["banán"] += 1
################
