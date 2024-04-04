# Portfolio tracker

Stránka https://api.coinranking.com/v2/ nabízí API, které nabízí data o cenách kryptoměn v reálném čase.
Data jsou aktualizovaná přibližně **každou minutu**.

Základním endpointem je endpoint pro zjištění ceny konkrétní kryptoměny.
URL vypadá následovně:
```djangourlpath
https://api.coinranking.com/v2/coin/{coin_id}/price
```
Nahraďte `coin_id` ID konkrétní kryptoměny. Seznam všech ID najdete na této adrese: https://api.coinranking.com/v2/coins
Příklad mapování ID na symboly kryptoměn:
```python
coin_ids = {
        'BTC': 'Qwsogvtv82FCd',
        'DOGE': 'a91GCGd_u96cF',
        'ADA': 'qzawljRxB5bYu',
    }
```

## Jak udělat request + API klíč

Při tvorbě `requestu`, tedy požadavku na server, je k němu ještě potřeba připojit API klíč.
Jde to i bez něj, ale je riziko, že vás server nebude obsluhovat.
API klíč se k requesty připojí následovně:

```python
url = f'https://api.coinranking.com/v2/coin/{coin_id}/price'
api_key = "VÁŠ API KLÍČ"
headers = {'x-access-token': api_key}
response = requests.get(url, headers=headers)
```

O API klíč si zažádej u mě.

## Limit

Na API klíč zdarma je limit několik stovek za měsíc.
Proto prosím posílej max. jeden požadavek za 15 sekund. Pokud uděláš nekonečný cyklus, který nebude mít žádnou pauzu, můžeš ten limit instantné vyčerpat.


## Úloha

Úkolem je udělat program, který načte portfolio kryptoměn ze souboru `data/portfolio.txt`
a bude monitorovat, jak se vyvíjí jeho hodnota.

### Načtení souboru

```python
with open("data/portfolio.txt", 'r') as file:
    for line in file:
        symbol, amount = line.split()
```


### Zaokrouhlení desetinných míst

```python
# zajímají nás jen 3 desetinná místa
round(float(total_value), 3)
```

### Vytisknutí aktuálního času

```python
import datetime
print(f"Čas: {datetime.now()}")
```


### Příklad výstupu programu

```text
>>>> Portfolio tracker <<<<<
- - - - - - - - - - - - - - -
Čas: 2024-03-22 13:09:39.903908
BTC: 0.005 * 64215.41370095826 = 321.0770685047913
DOGE: 1234.0 * 0.15550727116348192 = 191.8959726157367
ADA: 500.0 * 0.6191158077064782 = 309.5579038532391
Celková hodnota portfolia: 822.531 dollarů

Čas: 2024-03-22 13:10:25.270718
BTC: 0.005 * 64552.82792543954 = 322.7641396271977
DOGE: 1234.0 * 0.15635054288717018 = 192.936569922768
ADA: 500.0 * 0.6219655912238717 = 310.98279561193584
Celková hodnota se zvětšila o 4.153 na: 826.684 dollarů

Čas: 2024-03-22 13:11:10.631776
BTC: 0.005 * 64552.82792543954 = 322.7641396271977
DOGE: 1234.0 * 0.15635054288717018 = 192.936569922768
ADA: 500.0 * 0.6219655912238717 = 310.98279561193584
Celková hodnota portfolia zůstala na: 826.684 dollarů

Čas: 2024-03-22 13:11:56.026927
BTC: 0.005 * 64587.6908669859 = 322.9384543349295
DOGE: 1234.0 * 0.15634701679316693 = 192.932218722768
ADA: 500.0 * 0.6220922537512773 = 311.04612687563866
Celková hodnota se zvětšila o 0.233 na: 826.917 dollarů
```
