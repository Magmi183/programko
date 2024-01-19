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
    "Eda": [5, 1, 4, 4, 2, 2, 5, 4, 4, 4, 2],
    "Albert": [4, 2, 2, 2, 1, 4, 2, 3, 5, 4, 2, 1],  # majty
    "Kuba": [3, 3, 1, 4, 3, 4, 3, 4, 1, 2, 1, 1],
    "Ondra": [2, 2, 1, 3, 5, 1, 3, 2, 2],
    "Aleš": [1, 3, 5, 5, 1, 3, 3, 5, 4, 2, 5, 3, 5, 5, 3], # kuře
    "Vašek": [5, 1, 1, 3, 3, 3],
    "Andrej": [4, 4], # drak
    "Sofia": [3, 1, 5, 1, 1]
}

# Starší začátečníci
osudi_2 = {
    "Richard": [5, 5, 3, 3, 3, 4, 2, 4, 5, 2, 5, 3, 3], # paul
    "Matěj": [4, 4, 4, 4, 5, 1],
    "Šimon": [3, 3, 2, 1, 3, 5, 2, 1, 2, 4, 2],
    "Štěpán": [2, 3, 5, 3, 5, 5, 4, 2], # lednacek
    "Andreii": [1, 1, 3, 2, 3, 4],
    "Kuba" : [2, 5, 1, 2, 3, 3, 3, 1, 1],
    "Jáchym" : [4, 1, 2, 4, 4, 4, 5, 4], # naruto
    "Ondra" : [3, 1, 1, 3, 1, 1, 2]
}

# Pokročilí
osudi_3 = {
    "Martin": [5, 5, 1, 3, 5, 4, 2, 4, 2],
    "Petr": [4, 2, 4, 5, 5, 1, 5, 4, 5, 4, 4],
    "Honza": [3, 1, 3, 3, 4, 1, 4, 5, 1, 5, 3],
    "David": [2, 4, 4, 3, 3, 3, 1],
    "Oskar": [1, 3, 1, 5, 4, 2, 2, 2, 5, 3],
    "Tonda": [2, 3, 1, 1, 4, 3, 1],
    "Kuba": [2, 2, 1, 3, 2, 1, 2, 2],
    "" : [3]
}


zapni_tombolu(osudi_2)