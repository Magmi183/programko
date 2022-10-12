## TODO ##

"""
Úkol 0: Pacient

Chceme po uživateli, aby řekl Ááá. Když se mu to nepovede, nechceme aby program skončil, ale dáme mu další šanci.
A tak pořád dokola, dokud neřekne Ááá.

Přesné zadání: Zeptejte se uživatele na slovo, pokud řekne Ááá, pochvalte ho a program ukončete.
               Pokud řekne cokoliv jiného, vynadejte mu, ale dejte mu další šanci.
               A takto tak dlouho, dokud to nenapíše správně.

"""

odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')



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
import random
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