"""
░██╗░░░░░░░██╗██╗░░██╗██╗██╗░░░░░███████╗░░░░░░░█████╗░██╗░░░██╗██╗░░██╗██╗░░░░░██╗░░░██╗░██████╗
░██║░░██╗░░██║██║░░██║██║██║░░░░░██╔════╝░░░░░░██╔══██╗╚██╗░██╔╝██║░██╔╝██║░░░░░██║░░░██║██╔════╝
░╚██╗████╗██╔╝███████║██║██║░░░░░█████╗░░░░░░░░██║░░╚═╝░╚████╔╝░█████═╝░██║░░░░░██║░░░██║╚█████╗░
░░████╔═████║░██╔══██║██║██║░░░░░██╔══╝░░░░░░░░██║░░██╗░░╚██╔╝░░██╔═██╗░██║░░░░░██║░░░██║░╚═══██╗
░░╚██╔╝░╚██╔╝░██║░░██║██║███████╗███████╗░░░░░░╚█████╔╝░░░██║░░░██║░╚██╗███████╗╚██████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝░░░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚═════╝░╚═════╝░
"""

# Programy, co jsme zatím dělali měly jedno společné - byly poměrně jednoduché v tom, že se každý příkaz vykonal maximálně jednou.
# Např. pokud jsme udělaly kalkulačku, tak na jedno spuštění programu jsme mohli vypočítat jen jeden příklad.
# Pro spočítání 100 příkladů bychom program museli pustit 100x...
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


# Všimněte si, že proměnná co se používá v podmínce se v cyklu mění. Kdyby se neměnila, tak by cyklus nikdy neskončil.
# Jak se bude chovat tento program, když uživatel zada věk menší než 18 ?
vek = int(input("Zadej svůj věk pro ověření, zda-li můžeš vstoupit do baru."))
while vek < 18:
    print("Zadal jsi moc nízký věk. ")
    print("Zkus to znovu.")

# Nikdy neskončí a bude neustále psát to samé. Kde je chyba?
# Podmínka je sice hezká, ale my se uživatele na věk už nikdy nezeptáme a hodnota věku zůstane už na furt stejná.
# No a proto se hodnota podmínky nikdy nezmění a program zůstane do nekonečna zaseklý.

# zdroj: https://naucse.python.cz/lessons/beginners/while/

# Co když je podmínka splněna vždy?
from random import randrange
while True:
    print('Číslo je' + str(randrange(10000)))
    print('(Počkej, než se počítač unaví...)')
# CTRL C
# zdroj: https://naucse.python.cz/lessons/beginners/while/


# Někdy se ale může hodit mít nekonečný cyklus, co když chci třeba něco dělat každou sekundu?
# Využijeme funkci sleep (spi), které řekneme, kolik sekund má program spát - zastavit se.
import time
tik = True
while True:
    if tik == True:
        print("Tik")
    else:
        print("Tak")
    tik = not tik
    time.sleep(1)


# Sečíst čísla od 1 do 10:
n = 1
soucet = 0
while n <= 10: # Dokud je n menší nebo rovno 10, budu přičítat do součtu. Začínám od 1, končím u 10.
    soucet = soucet + n # zvýším součet o číslo n
    # soucet += n # tohle je jednodušší zápis příkazu nad tím
    n = n + 1 # Zvýším číslo n o jedna

print("Součet čísel od 1 do 10 je: " + str(soucet))

# Jak zvětším/zmenším hodnotu proměnné o 1?

# += -= /= *=
pocitadlo = 10
pocitadlo = pocitadlo + 1
# ... je to samé jako ...
pocitadlo += 1 # hezčí a jednodušší zápis
# stejně můžu aplikovat i na násobení/dělení/odčítání
