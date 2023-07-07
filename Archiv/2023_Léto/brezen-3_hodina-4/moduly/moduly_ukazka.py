# Modul obsahující MATEMATICKÉ FUNKCE
import math

# např. odmocnina
x = 25
result = math.sqrt(x)
print(result)

# https://docs.python.org/3/library/math.html

# Modul pro práci s náhodou, generování náhodných čísel, vybírání náhodných indexů, míchání...
import random

result = random.randint(1, 10)
print(result)

# https://docs.python.org/3/library/random.html

# Práce s daty a jejich formátování
import datetime

now = datetime.datetime.now()
print(now)

# Knihovna pro práci s OS, na kterém program běží
import os

files = os.listdir()
print(files)