"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""

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