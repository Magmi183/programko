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
    "Eda": [4, 5, 4, 5, 3, 4, 3, 3, 6],
    "Albert": [3, 2, 3, 2, 4, 2, 3, 4, 2, 2, 1, 3, 2, 2, 1],
    "Kuba": [3, 4, 5, 3, 4, 1, 2, 1, 1, 1, 4],
    "Aleš": [5, 4, 5, 5, 4, 2, 5, 5, 5, 5, 4, 6, 5, 4, 6, 2],
    "Emilie": [2, 2, 2, 3, 3, 3, 4, 3, 1, 3, 6, 4, 3], # zahrnuje počáteční boost
}

# Starší začátečníci
osudi_2 = {
    "Richard": [3, 3, 1, 2, 5, 2, 2, 2, 2, 4, 2, 5, 1, 5, 1, 3, 3, 1],
    "Šimon": [5, 1, 1, 3, 1, 5, 1, 1, 5, 5, 4, 4, 3, 2, 3, 5, 2, 4, 6],
    "Štěpán": [4, 1, 5, 1, 1, 4, 2, 4, 3, 4, 2, 4, 1, 2, 6, 1, 2],
    "Andreii": [1, 2, 4, 1, 1, 1, 4, 1],
    "Kuba" : [5, 4, 1, 5, 3, 4, 1, 1, 1, 5, 3, 3],
    "Jáchym" : [2, 1, 3, 5, 2, 1, 1, 2, 1, 3, 3, 2, 5, 6, 4, 6, 4],
    "Ondra" : [1, 1, 1, 3, 1, 3, 2, 1, 4, 3, 3, 1, 2, 1, 3, 1, 2],
}

# Pokročilí
osudi_3 = {
    "Martin": [1, 2, 3, 1, 1, 5, 2, 3, 3],
    "Petr": [5, 5, 5, 5, 3, 5, 5, 3, 2, 4, 5, 5, 6, 2],
    "Honza": [4, 1, 4, 4, 4, 1, 1, 4],
    "David": [2, 4, 2, 5, 5, 1, 1, 4, 1],
    "Oskar": [4, 2, 5, 3, 3, 2, 5],
    "Tonda": [3, 3, 2, 1, 1, 4, 3, 2, 3, 1, 3],
    "Kuba": [3, 1, 4, 4, 2, 1, 2, 2],
    "Sam" : [2, 2, 3, 3, 6],
}


# zapni_tombolu(osudi_3)