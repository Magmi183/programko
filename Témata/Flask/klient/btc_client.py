import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()

currency = input("Zajímá vás cena Bitcoinu v EUR nebo USD? (Zadejte 'EUR' nebo 'USD'): ").upper()
price = data['bpi'][currency]['rate']

if currency not in ['EUR', 'USD']:
    print("Neplatný výběr. Prosím, zadejte 'EUR' nebo 'USD'.")
else:
    print(f"Aktuální cena Bitcoinu v {currency} je: {price}")


