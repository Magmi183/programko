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
    "Eda": [],
    "Albert": [],
    "Kuba": [],
    "Aleš": [],
    "Vašek": [],
    "Andrej": [],
}

# Starší začátečníci
osudi_2 = {
    "Richard": [],
    "Matěj": [],
    "Šimon": [],
    "Štěpán": [],
    "Andreii": [],
    "Kuba" : [],
    "Jáchym" : [],
    "Ondra" : [],
}

# Pokročilí
osudi_3 = {
    "Martin": [],
    "Petr": [],
    "Honza": [],
    "David": [],
    "Oskar": [],
    "Tonda": [],
    "Kuba": [],
    "Sampy" : [],
}


# zapni_tombolu(osudi_3)