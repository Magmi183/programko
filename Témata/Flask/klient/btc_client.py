import requests
import time


api_key = '' # INSERT API KEY HERE!
url = 'https://api.coinranking.com/v2/coin/Qwsogvtv82FCd/price'

headers = {
    'x-access-token': api_key
}
response = requests.get(url, headers=headers)
data = response.json()
price = data['data']['price']

print(price)
