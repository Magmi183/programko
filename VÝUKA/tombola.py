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

# Mladší začátečníci
osudi_1 = {
    "Eda": [5, 1, 4, 4, 2, 2, 5, 4, 4],
    "Albert": [4, 2, 2, 2, 1, 4, 2, 3, 5],  # majty
    "Kuba": [3, 3, 1, 4, 3, 4, 3, 4, 1, 2],
    "Ondra": [2, 2, 1, 3, 5, 1, 3, 2],
    "Aleš": [1, 3, 5, 5, 1, 3, 3, 5, 4, 2, 5, 3], # kuře
    "Vašek": [5, 1, 1, 3],
    "Andrej": [4, 4], # drak
    "Sofia": [3, 1, 5, 1, 1]
}
# TODO: mravenec - 2

# Starší začátečníci
osudi_2 = {
    "Richard": [5, 5, 3, 3, 3, 4, 2, 4, 5, 2, 5], # paul
    "Matěj": [4, 4, 4, 4, 5, 1],
    "Šimon": [3, 3, 2, 1, 3, 5, 2, 1, 2],
    "Štěpán": [2, 3, 5, 2, 5, 5, 4, 2], # lednacek
    "Andreii": [1, 1, 3, 2, 3, 4],
    "Kuba" : [2, 5, 1, 2, 3, 3, 3],
    "Jáchym" : [4, 1, 2, 4, 4, 4, 5], # naruto
    "Ondra" : [3, 1, 1, 3, 1, 1]
}

# Pokročilí
osudi_3 = {
    "Martin": [5, 5, 1, 3, 5, 4, 2, 4],
    "Petr": [4, 2, 4, 5, 5, 1, 5, 4, 5],
    "Honza": [3, 1, 3, 3, 4, 1, 4, 5, 1],
    "David": [2, 4, 4, 3, 3, 3],
    "Oskar": [1, 3, 1, 5, 4, 2, 2, 2, 5],
    "Tonda": [2, 3, 1, 1, 4, 3],
    "Kuba": [2, 2, 1, 3, 2, 1, 2],
    "" : [3]
}
