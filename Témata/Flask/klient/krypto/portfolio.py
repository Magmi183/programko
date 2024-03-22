import requests
import time
from datetime import datetime


def get_price(api_key, coin_id):
    url = f'https://api.coinranking.com/v2/coin/{coin_id}/price'
    headers = {'x-access-token': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return float(data['data']['price'])

def parse_portfolio(filename):
    portfolio = {}
    with open(filename, 'r') as file:
        for line in file:
            symbol, amount = line.split()
            portfolio[symbol] = float(amount)
    return portfolio

def main():
    api_key = 'coinranking0ee244eb7642e50318955cd522a5a24e6785e7570bf47b0e'
    portfolio_filename = 'data/portfolio.txt'

    portfolio = parse_portfolio(portfolio_filename)

    print(">>>> Portfolio tracker <<<<<")
    print("- - - - - - - - - - - - - - -")
    coin_ids = {
        'BTC': 'Qwsogvtv82FCd',
        'DOGE': 'a91GCGd_u96cF',
        'ADA': 'qzawljRxB5bYu',
    }

    prev_value = 0
    while True:
        total_value = 0.0
        for symbol, amount in portfolio.items():
            if symbol in coin_ids:
                price = get_price(api_key, coin_ids[symbol])
                value = price * amount
                total_value += value
                print(f'{symbol}: {amount} * {price} = {value}')
            else:
                print(f'Coin ID for {symbol} not found.')
        print(f"Čas: {datetime.now()}")
        if prev_value == 0:
            print(f'Celková hodnota portfolia: {total_value}\n')
        elif prev_value < total_value:
            print(f'Celková hodnota se zvětšila o {total_value - prev_value} na: {total_value}\n')
        elif prev_value > total_value:
            print(f'Celková hodnota se snížila o {prev_value - total_value} na: {total_value}\n')
        else:
            print(f'Celková hodnota portfolia zůstala na: {total_value}\n')
        prev_value = total_value
        time.sleep(5)

if __name__ == '__main__':
    main()
