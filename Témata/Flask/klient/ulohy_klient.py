# DŮLEŽITÉ: Spouštějte tyto úlohy v PyCharmu nebo jiném lokálním IDE, které máte nainstalované u sebe na počítači.
#           Lépe tím nasimulujeme reálnou situaci - máme server, který běží na Replitu, na nějakém serveru třeba v Anglii,
#           a připojíme se na něj pomocí programu, který beží v ČR, na vašem počítači.

# Úlohy na sebe volně navazují.
# Pro začátek se můžete inspirovat programem `simple_client.py`.


"""
ÚLOHA 0: Ukázka

Vyzkoušej si zprovoznit kód, který je v `simple_client.py`.
K otestování použij svoji vlastní aplikaci, kterou jsi vytvořil na Replitu.

"""

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
ÚLOHA 2: Predikce země

API https://api.nationalize.io?name=JMENO umožňuje predikovat, v jaké zemi se uživatel nachází na základě jeho jména.
Zeptejte se uživatele, jaké je jeho jméno a řekněte mu, s jakou pravděpodobností žije v jaké zemi.

"""

jmeno = "Michal"
url = f"https://api.nationalize.io?name={jmeno}"



"""
ÚLOHA 3: Aktuální cena BITCOINU

Stránka https://api.coindesk.com/v1/bpi/currentprice.json poskytuje cenu bitcoinu v reálném čase, a to ve měnách jako je
euro, libra nebo americký dolar.

Úkol 1:
    Udělejte program, který se zeptá uživatele na měnu, která ho zajímá (EUR, USD nebo GBP) a následně mu řekněte, jaká
    je aktuální cena Bitcoinu v této měně.
    
Úkol 2:
    Udělejte program, který bude každých 10 sekund kontrolovat cenu Bitcoinu a vždy oznámí, jestli se cena zvýšila, snížila,
    nebo jestli zůstala stejná.
    Nápověda: Udělejte nekonečný cyklus a použijte funkci time.sleep(10).

"""



"""
ÚLOHA 4: Vlastní aplikace

Stránka https://apipheny.io/free-api/ obsahuje seznam cca 15 API zdarma.
Vyberte si libovolné API a postavte na něm aplikaci.

Příklady:
    1) API na náhodné vtipy: Aplikace, která každých 5 sekund zobrazuje uživateli jiný vtip. (https://official-joke-api.appspot.com/random_joke)
    2) API na náhodného člověka: Aplikace, která uživateli vygeneruje novou identitu. (https://randomuser.me/api/)
    3) API s tipami na aktivity: Aplikace, která uživateli, který se nudí, doporučí co dělat. (https://www.boredapi.com/api/activity)
    4) ...

"""



"""
ÚLOHA 5: Poké Api

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
