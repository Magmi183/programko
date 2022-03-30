# Programy, co jsme zatím dělali měly jedno společné - byly poměrně jednoduché v tom, že se každý příkaz vykonal maximálně jednou.
# Např. pokud jsme udělaly kalkulačku, tak na jedno spuštění programu jsme mohli vypočítat jen jeden příklad.
# Pro spočítání 100 příkladů bychom program museli pustit 100x...
# Co kdybychom chtěli, aby se program opakoval? K tomu máme CYKLUS!

# CYKLUS WHILE
# While znamená anglicky DOKUD. Tohle je cyklus, který se bude opakovat tak dlouho, dokud je podmínka splněná.
# Je to hodně podobné jako IF, akorát se příkazy nevykonají jen jednou, ale budou se vykonávat pořád dokola, dokud je ta
# podmínka platná.


# Chceme po uživateli, aby řekl Ááá. Když se mu to nepovede, nechceme aby program skončil, ale dáme mu další šanci.
# A tak pořád dokola, dokud neřekne Ááá.
import random

odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')

# zdroj: https://naucse.python.cz/lessons/beginners/while/

# Co když je podmínka splněna vždy?
from random import randrange
while True:
    print('Číslo je', randrange(10000))
    print('(Počkej, než se počítač unaví...)')
# CTRL C
# zdroj: https://naucse.python.cz/lessons/beginners/while/

# Sečíst čísla od 1 do 10:
n = 1
soucet = 0
while n <= 10: # Dokud je n menší nebo rovno 10, budu přičítat do součtu. Začínám od 1, končím u 10.
    soucet = soucet + n # zvýším součet o číslo n
    # soucet += n # tohle je jednodušší zápis příkazu nad tím
    n = n + 1 # Zvýším číslo n o jedna

print("Součet čísel od 1 do 10 je: " + str(soucet))


"""
Úkol 1: Součet čísel od 50 do 100

Pomocí cyklu while udělejte program, který spočítá součet čísel od 50 do 100 (včetně).

"""


"""

Úkol 10: Uhodni číslo

Udělej hru, kde uživatel bude hádat číslo, které si program myslí. 
Uživatel bude dávat tipy (má jich omezený počet, třeba 10) a pokud číslo uhodne, program končí.
Pokud uživatel neuhodl, program mu řekne, jestli je číslo co si myslí menší nebo větší.
Pokud uživatel neuhodne číslo ani na 10 pokusů, hra končí.

"""

cislo = random.randrange(50)
pocet_pokusu = 10
tip = 0
while pocet_pokusu > 0 and tip != cislo:
    tip = int(input("Zadej svůj tip:\n"))
    if tip > cislo:
        print("Myslím si menší číslo.")
    elif tip < cislo:
        print("Myslím si větší číslo.")
    pocet_pokusu -= 1
    print("Máš ještě " + str(pocet_pokusu) + " pokusů.")
if tip == cislo:
    print("Gratuluji, myslel jsem si " + str(tip) + ". Uhádl si!")
else:
    print("Prohrál jsi... Myslel jsem si " + str(cislo) + " .")