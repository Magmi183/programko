# CÍL: Program se zeptá uživatele na město, poté odešle požadavek na server a zobrazí uživateli odpověď serveru,
#      která obsahuje informace o počasí v daném městě.

# Import knihovny umožňující posílání HTTP požadavků na server.
import requests

# Základní URL, na kterou budeme odesílat požadavky.
# base_url = 'http://127.0.0.1:5000'  # Příklad URL pro vývojový server
base_url = 'http://127.0.0.1:80'  # Příklad produkčního URL

mesto = input("Zadej město: ")

# Vytvoření URL pro endpoint '/pocasi/<mesto>'
# Kombinací základního URL a cesty k němu získáme kompletní URL.
url = f'{base_url}/pocasi/{mesto}'

# Odeslání GET požadavku a přijetí odpovědi.
response = requests.get(url)

# Kontrola, zda byl požadavek úspěšný.
if response.status_code == 200:
    # Vypsání obsahu odpovědi od serveru.
    print(f'Odpověď od serveru: {response.text}')
else:
    # Ošetření chyby v případě problémů s komunikací se serverem.
    print('Došlo k chybě při komunikaci se serverem.')

# UKÁZKA, JAK BY MOHL VYPADAT ENDPOINT V APLIKACI FLASK:
"""
@app.route('/pocasi/<mesto>')
def pocasi(mesto):
    # Pro demonstraci použijeme pevně dané předpovědi počasí.
    predpoved = {
        "Praha": "Slunečno s občasnými přeháňkami",
        "Brno": "Zataženo s možností deště",
        "Ostrava": "Částečně zataženo",
        "Plzeň": "Jasno"
    }

    # Získání počasí pro zadané město, výchozí hodnota pro neznámá města.
    pocasi_ve_meste = predpoved.get(mesto, "Počasí pro toto město není k dispozici")
    return f'Počasí ve městě {mesto}: {pocasi_ve_meste}'
"""
