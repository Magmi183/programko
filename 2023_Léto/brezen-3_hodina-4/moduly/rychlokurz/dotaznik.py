# importujeme si funkcionalitu z našeho souboru "pozdrav"
# chceme pouze použít funkce, které v něm jsou, nechceme aby vykonával nic sám, např. ptal se na jméno

import pozdrav

jazyk = "cj"

jmeno = input("Zadej své jméno prosím:  ")

# používáme funkcionalitu z našeho souboru pozdrav.py
pozdrav.pozdrav(jmeno, jazyk)