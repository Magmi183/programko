# jak zvětším/zmenším hodnotu proměnné o 1?

# += -= /= *=

# stejně můžu aplikovat i na násobení/dělení


# Programy, co jsme zatím dělali, měly jedno společné - byly poměrně jednoduché v tom, že se každý příkaz vykonal maximálně jednou.
# Např. pokud jsme udělali kalkulačku, tak na jedno spuštění programu jsme mohli vypočítat jen jeden příklad.
# Pro spočítání 100 příkladů bychom program museli pustit 100x... a nebo 100x za sebou napsat ten stejný kód, což by bylo velmi nepěkné.
# Co kdybychom chtěli, aby se program opakoval? K tomu máme CYKLUS!

# CYKLUS WHILE
# While znamená anglicky DOKUD. Tohle je cyklus, který se bude opakovat tak dlouho, dokud je podmínka splněná.
# Je to hodně podobné jako IF, akorát se příkazy nevykonají jen jednou, ale budou se vykonávat pořád dokola, dokud je ta
# podmínka platná.

# Představte si podmínku (if). Pokud předpoklad platí, tak se vykonají příkazy, co jsou pod podmínkou (python to pozná
# podle odsazení. Cyklus WHILE (dokud) je velmi podobný, akorát se příkazy (pokud platí podmínka) nevykonají jen jednou,
# ale budou se dělat tak dlouho, dokud podmínka bude platit. Takže python normálně od shora dolů vykonává příkazy a když dorazí
# na konec cyklu (tam, kde končí odsazení), znovu zkontroluje podmínku a když pořád platí, tak znova vykonává příkazy od shora dolu.
# A takhle pořád dokola.

pohlavi = input("Zadej, jestli jsi kluk (k) nebo holka (h).")
while pohlavi != 'k' and pohlavi != 'h':
    print("Zadal jsi to blbě. Tak znovu...")
    pohlavi = input("Zadej, jestli jsi kluk (k) nebo holka (h).")

if pohlavi == 'k':
    print("Ahoj kluku")
else:
    print("Ahoj holko")

# Chceme po uživateli, aby řekl Ááá. Když se mu to nepovede, nechceme aby program skončil, ale dáme mu další šanci.
# A tak pořád dokola, dokud neřekne Ááá.
import random

odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')

# zdroj: https://naucse.python.cz/lessons/beginners/while/

# Všimněte si, že proměnná co se používá v podmínce se v cyklu mění. Kdyby se neměnila, tak by cyklus nikdy neskončil.
# Jak se bude chovat tento program, když uživatel zada věk menší než 18 ?
vek = int(input("Zadej svůj věk pro ověření, zda-li můžeš vstoupit do baru."))
while vek < 18:
    print("Zadal jsi moc nízký věk. ")
    print("Zkus to znovu.")

# Nikdy neskončí a bude neustále psát to samé. Kde je chyba?
# Podmínka je sice hezká, ale my se uživatele na věk už nikdy nezeptáme a hodnota věku zůstane už na furt stejná.
# No a proto se hodnota podmínky nikdy nezmění a program zůstane do nekonečna zaseklý.


# Někdy se ale může hodit mít nekonečný cyklus, co když chci třeba něco dělat každou sekundu?
# Využijeme funkci sleep (spi), které řekneme, kolik sekund má program spát - zastavit se.
import time
tik = True
while True:
    if tik==True:
        print("Tik")
    else:
        print("Tak")
    tik = not tik
    time.sleep(1)


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

soucet = 0
cislo = 50 # číslo, od kterého chci začít

# SEM PIŠ SVŮJ KÓD

print("Součet čísel od 50 do 100 (včetně) je: " + str(soucet))

"""
Úkol 2: Fibonacciho čísla

Zobrazte prvních 100 čísel Fibonacciho posloupnosti.
Začíná se s 0 a 1, a každé další číslo je součtem dvou předchozích.
Takže 0, 1, 1, 2, 3, 5 ... 
"""

cislo1 = 0 # první číslo fibonacciho posloupnosti
cislo2 = 1 # druhé číslo fibonacciho posloupnosti
print(cislo1) # zobrazím první číslo
print(cislo2) # zobrazím druhé číslo
# teď už jen vypsat zbytek...

# SEM PIŠ SVŮJ KÓD

"""
Úkol 3: Součty sudých a lichých čísel

Pomocí cyklu while spočítejte a zobrazte součet čísel od 1 do 100 (včetně).
Ale POZOR, nezajímá nás celkový součet, ale součet sudých a lichých čísel zvlášť!
Použijte operátor modulo (zbytek po dělení).
"""

lichy_soucet = 0
sudy_soucet = 0

# SEM PIŠ SVŮJ KÓD

print("Součet sudých čísel od 1 do 100 (včetně) je:", sudy_soucet)
print("Součet lichých čísel od 1 do 100 (včetně) je:", lichy_soucet)

"""
Úkol 4: Polopyramida

Zeptejte se uživatele na výšku pyramidy a vypište mu tak vysokou polopyramidu z hvězdiček.
Například polopyramida výšky 5 vypadá takto:
*
**
***
****
*****
"""

vyska = int(input("Zadej jak vysokou chceš polopyramidu: \n"))

"""
Úkol 4.5: Legit pyramida (pro rychlíky/na doma)

Stejný úkol jako polopyramida, akorát že to není polopyramida, ale legit pyramida. 
Například legit pyramida výšky 5 vypadá takto:
    *
   ***
  *****
 *******
*********
"""

vyska = int(input("Zadej jak vysokou chceš pyramidu: \n"))

"""

Úkol 5: Uhodni číslo

Udělej hru, kde uživatel bude hádat číslo, které si program myslí. 
Uživatel bude dávat tipy (má jich omezený počet, třeba 10) a pokud číslo uhodne, program končí.
Pokud uživatel neuhodl, program mu řekne, jestli je číslo co si myslí menší nebo větší.
Pokud uživatel neuhodne číslo ani na 10 pokusů, hra končí.

"""

cislo = random.randrange(50)
pocet_pokusu = 10

