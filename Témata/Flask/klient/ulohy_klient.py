# DŮLEŽITÉ: Spouštějte tyto úlohy v PyCharmu nebo jiném lokálním IDE, které máte nainstalované u sebe na počítači.
#           Lépe tím nasimulujeme reálnou situaci - máme server, který běží na Replitu, na nějakém serveru třeba v Anglii,
#           a připojíme se na něj pomocí programu, který beží v ČR, na vašem počítači.

# Úlohy na sebe volně navazují.
# Pro začátek se můžete inspirovat programem `simple_client.py`.

"""
ÚLOHA 1: Basic client

Udělejte program, který se uživatele zeptá na:
 1. Základní URL (např. https://3119fe87-5da3-4947-929a-7f2bf23cc062-00-3g0ca1enjpsgt.picard.replit.dev)
 2. Cestu (např. /ukazka)

Následně proveďte požadavek na server s danným URL a cestou,
např.: https://3119fe87-5da3-4947-929a-7f2bf23cc062-00-3g0ca1enjpsgt.picard.replit.dev/ukazka
a následně uživateli zobrazte odpověď serveru.

"""

import requests


"""
ÚLOHA 2: Poké Api

Využijeme veřejně dostupný server poskytující informace o Pokemonech, https://pokeapi.co/api/v2/pokemon/.
Zkuste se na stránku připojit z vašeho webového prohlížeče, otevřete si např. https://pokeapi.co/api/v2/pokemon/pikachu
a prozkoumejte, jak vypadá odpověď serveru. Všimněte si, že formátem velmi připomíná SLOVNÍK. 

Kroky:
1. Zeptejte se uživatele na název Pokémona, o kterého má zájem.
2. Použijte knihovnu requests k odeslání GET požadavku na PokeAPI s cílem získat informace o zadaném Pokémonovi.
   Použijte URL ve formátu https://pokeapi.co/api/v2/pokemon/{name}, kde {name} je název Pokémona, který uživatel zadal.
3. Zpracujte odpověď od serveru (převeďte na slovník) a extrahujte z ní základní informace o Pokémonovi. 
   Je na vás, co si vyberete, např.: jeho ID, typ(y) a schopnosti.
4. Zobrazte tyto informace uživateli.

Příklad, jak by mohl vypadat výsledek:

Zadejte název Pokémona: pikachu
ID Pokémona: 25
Typy: electric
Schopnosti: static, lightning-rod
"""

import requests

