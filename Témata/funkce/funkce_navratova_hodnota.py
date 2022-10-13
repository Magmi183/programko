"""
███╗░░██╗░█████╗░██╗░░░██╗██████╗░░█████╗░████████╗░█████╗░██╗░░░██╗░█████╗░
████╗░██║██╔══██╗██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗
██╔██╗██║███████║╚██╗░██╔╝██████╔╝███████║░░░██║░░░██║░░██║╚██╗░██╔╝███████║
██║╚████║██╔══██║░╚████╔╝░██╔══██╗██╔══██║░░░██║░░░██║░░██║░╚████╔╝░██╔══██║
██║░╚███║██║░░██║░░╚██╔╝░░██║░░██║██║░░██║░░░██║░░░╚█████╔╝░░╚██╔╝░░██║░░██║
╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝

        ██╗░░██╗░█████╗░██████╗░███╗░░██╗░█████╗░████████╗░█████╗░
        ██║░░██║██╔══██╗██╔══██╗████╗░██║██╔══██╗╚══██╔══╝██╔══██╗
        ███████║██║░░██║██║░░██║██╔██╗██║██║░░██║░░░██║░░░███████║
        ██╔══██║██║░░██║██║░░██║██║╚████║██║░░██║░░░██║░░░██╔══██║
        ██║░░██║╚█████╔╝██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║░░██║
"""

"""
NÁVRATOVÁ HODNOTA FUNKCE:

Do teď jsme měli funkce jako takovou krabičku, co se zavolá, něco vykreslí nebo udělá a konec.
Většinou ale po funkci chceme, aby něco dělala, například nějaký výpočet a potom
nám výsledek vrátila (řekla) ať s ním můžeme dále pracovat.

Funguje to tak, že když už funkce končí, můžu pomocí slova return něco z funkce vrátit,
tím se ta hodnota co vracím "pošle na místo, odkud jsem funkci volal".
"""

import random
def generuj_cislo(od, do):
    # vygeneruji si cislo
    generovane_cislo = random.randrange(od, do)
    # vygenerované číslo vrátím na místo, odkud se funkce volala
    return generovane_cislo

# zavolá se funkce, ta vrátí vygenerované číslo a to se pak uloží do proměnné
cislo = generuj_cislo(1,10)
cislo2 = generuj_cislo(44,283)
print(f"Součet dvou vygenerovaných čísel je: {cislo + cislo2}")

# Tato funkce dostane věk a rozhodne, jestli je mezi 10 a 16 a tedy může chodit na Python kroužek
# Výsledek pak funkce vrátí
def muze_na_krouzek(vek):
    if vek < 10 or vek > 16:
        return False
    else:
        return True

vek = int(input("Zadej věk a zjistíš, jestli můžeš chodit na kroužek: \n"))

if muze_na_krouzek(5):
    print("Můžeš.")
else:
    print("Bohužel nesmíš.")

"""
Úkol 1: Objem kvádru

Udělej funkci, která přijímá 3 parametry - strany nějakého kvádru (a, b, c).
Funkce spočítá objem tohoto kvádru a vrátí výsledek.
"""

"""
Úkol 2: Random příklad

Udělej funkci, která vygeneruje náhodný příklad a zobrazí ho uživateli.
Součástí funkce je i načtení odpovědi.
Funkce vrátí True, pokud uživatel odpověděl správně, jinak vrátí False.

Obtížnost a typ příkladu je na vás, čísla ale musí být vygenerována náhodně.

Rozšíření:
    - přidejte do funkce nějaké parametry, například:
        - maximální rozsah čísel
        - typ příkladu (sčítání, dělení, násobení)
"""

def zadej_priklad():
    """Sem pište váš kód"""