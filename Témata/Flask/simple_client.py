import requests

# Základní URL vaší Flask aplikace
# base_url = 'http://127.0.0.1:5000'
base_url = 'http://127.0.0.1:80'

mesto = input("Zadej město: ")

# Vytvoření URL pro endpoint '/pocasi/<mesto>'
url = f'{base_url}/pocasi/{mesto}'

# Odeslání GET požadavku a získání odpovědi
response = requests.get(url)

# Kontrola, zda požadavek proběhl úspěšně
if response.status_code == 200:
    # Vypsání obsahu odpovědi
    print(f'Odpověď od serveru: {response.text}')
else:
    print('Došlo k chybě při komunikaci se serverem.')

"""
@app.route('/pocasi/<mesto>')
def pocasi(mesto):
  # Pro jednoduchost zde použijeme pevně dané počasí pro demonstraci
  predpoved = {
    "Praha": "Slunečno s občasnými přeháňkami",
    "Brno": "Zataženo s možností deště",
    "Ostrava": "Částečně zataženo",
    "Plzeň": "Jasno"
  }

  pocasi_ve_meste = predpoved.get(mesto, "Počasí pro toto město není k dispozici")
  return f'Počasí ve městě {mesto}: {pocasi_ve_meste}'
"""