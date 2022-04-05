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

while cislo <= 100:
    soucet += cislo # přidám číslo do součtu
    cislo += 1 # zvětším číslo o 1
    # a tak pořád dál, dokud číslo není větší než 100..
    # to znamená, že všechny čísla od 50 do 100 sečtu, a mám co jsem chtěl!

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
zobrazeno_cisel = 2 # udělám si počítadlo, kolik už jsem vypsal čísel (zastavím se, až bude 100)

while zobrazeno_cisel < 100: # dokud jsem ještě nezobrazil 100 čísel, chci aby cyklus pokračoval
    dalsi_cislo = cislo1 + cislo2 # spočítám nové číslo
    print(dalsi_cislo) # vypíšu nové číslo
    zobrazeno_cisel += 1
    cislo1 = cislo2
    cislo2 = dalsi_cislo

"""
Úkol 3: Součty sudých a lichých čísel

Pomocí cyklu while spočítejte a zobrazte součet čísel od 1 do 100 (včetně).
Ale POZOR, nezajímá nás celkový součet, ale součet sudých a lichých čísel zvlášť!
Použijte operátor modulo (zbytek po dělení).
"""

lichy_soucet = 0
sudy_soucet = 0
cislo = 1

while cislo <= 100:
    if cislo % 2 == 0: # když číslo vydělím dvěma a zbyde nula, znamená to, že je číslo sudé
        sudy_soucet += cislo # číslo přidám do sudého součtu
    else: # pokud číslo není sudé, tak je liché
        lichy_soucet += cislo

    cislo += 1 # nezapomenout zvětšit o 1 !

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
hvezd = 1 # polopyramidu budu "kreslit" od shora, proto začnu s jednou hvězdičkou

while hvezd <= vyska: # chci tolik pater, kolik uživatel zadal
    print("*" * hvezd) # vynásobím string a int => dostanu string spojený několikrát za sebe
    hvezd += 1 # počet hvězd zvětším o jedna (pro příští patro)

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
patro = 0 # udělám si počítadlo pater - jeho hodnota bude číslo patra, které jsem vyprintil naposledy, 0 znamená, že jsem ještě nevyprintil nic
hvezd = 1 # polopyramidu budu "kreslit" od shora, proto začnu s jednou hvězdičkou
mezer = vyska - 1 # kolik mezer před hvězdičkou je v horním patře?

while patro < vyska: # dokud jsem ještě nevytiskl poslední patro, cyklus jede dál
    print(mezer*" " + "*" * hvezd) # vyprintím patřičný počet mezer a za to počet hvězd, mezery za hvězdama už printit nemusím
    hvezd += 2 # počet hvězd zvětším o dva (koukni na příklad, v každém patře přibydou dvě hvězdy)
    mezer -= 1 # lze vypozorovat, že v každém patře je o jednu mezeru méně (před hvězdama)
    patro += 1 # udělal jsem další patro, proto si zvýším počítadlo

"""

Úkol 5: Uhodni číslo

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

Úkol 6: Hledání prvočísel (bonus)

TODO

"""
