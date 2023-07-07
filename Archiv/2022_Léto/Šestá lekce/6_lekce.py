vek1 = 15
vek2 = 15
print(vek1 == vek2)

# Další operátory
print(vek1 < vek2) # Je vek1 menší než vek2?
print(vek1 > vek2) # Je vek1 větší než vek2?
print(vek1 <= vek2) # Je vek1 menší nebo stejný jako vek2?
print(vek1 >= vek2) # Je vek1 větší nebo stejný jako vek2?
print(vek1 != vek2) # Je vek1 jiný než vek2?

# Výrazu můžeme spojovat logickými spojkami

a = True    # pravda
b = False   # nepravda
c = a or b  # nebo -> True (aspoň b nebo a musí být pravda. a je pravda, takže celý je to pravda)
c = a and b # a zároveň -> False (obojí musí být pravda, ale b není, takže celý je to nepravda)
c = not a   # negace -> False (opak True takže False)

if 15 == 16 or 10 == 10:
    print("15 sice není 16, ale 10 je 10 a to stačí, aby podmínka byla True")

vek = int(input())
kluk = input("Jsi kluk? ano/ne")
if vek > 6 and kluk == 'ano':
    print("Splňuješ podmínky pro účast na klučičím táboře.")
elif kluk == 'ano':
    print("Jsi moc mladý, musí ti být aspoň 7 let.")
elif vek > 6:
    print("Tábor je jen pro kluky.")
else:
    print("Jsi holka a nebylo ti ani 7 let.")


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
    print('Číslo je' + str(randrange(10000)))
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

Ukázková úloha: Uhodni číslo

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


"""
Úkol 1: Součet čísel od 50 do 100

Pomocí cyklu while udělejte program, který spočítá součet čísel od 50 do 100 (včetně).

"""
