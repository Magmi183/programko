"""
PRAVIDLA:

Lístky do tomboly se získávájí za:
  1) Pořadí ve kvízech
    1. místo = 5 lístků do osudí
    2. místo = 4 lístky do osudí
    3. místo = 3 lístky do osudí
    4. místo = 2 lístky do osudí
    5. místo = 1 lístek do osudí

  2) Řešení úloh (mini-soutěže) a programování větších programů
    - Vyřešení malé úlohy (na rychlost): 1 lístek
    - Naprogramování většího projektu: 1 - 10 lístků


CENY PRO VÍTĚZE: Krypto

"""

from tombola_tools import *

# Mladší začátečníci
osudi_1 = {
    "Eda": [4],
    "Albert": [3],
    "Kuba": [],
    "Aleš": [5],
    "Vašek": [],
    "Emilie": [2], # docházka = 2 body
}

# Starší začátečníci
osudi_2 = {
    "Richard": [3, 3],
    "Matěj": [],
    "Šimon": [5],
    "Štěpán": [4],
    "Andreii": [1, 2],
    "Kuba" : [5, 4],
    "Jáchym" : [2],
    "Ondra" : [1],
}

# Pokročilí
osudi_3 = {
    "Martin": [1],
    "Petr": [5],
    "Honza": [4],
    "David": [2],
    "Oskar": [],
    "Tonda": [3],
    "Kuba": [],
    "Sampy" : [],
}


# zapni_tombolu(osudi_3)