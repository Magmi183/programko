# Moc hezký úvod do for cyklů, ze kterého jsem také trochu čerpal, je zde (v češtině): https://www.itnetwork.cz/python/zaklady/cykly-v-pythonu
"""
            ███████╗░█████╗░██████╗░░░░░░█████╗░██╗░░░██╗██╗░░██╗██╗░░░░░██╗░░░██╗░██████╗
            ██╔════╝██╔══██╗██╔══██╗░░░░██╔══██╗╚██╗░██╔╝██║░██╔╝██║░░░░░██║░░░██║██╔════╝
            █████╗░░██║░░██║██████╔╝░░░░██║░░╚═╝░╚████╔╝░█████═╝░██║░░░░░██║░░░██║╚█████╗░
            ██╔══╝░░██║░░██║██╔══██╗░░░░██║░░██╗░░╚██╔╝░░██╔═██╗░██║░░░░░██║░░░██║░╚═══██╗
            ██║░░░░░╚█████╔╝██║░░██║░░░░╚█████╔╝░░░██║░░░██║░╚██╗███████╗╚██████╔╝██████╔╝
            ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚═════╝░╚═════╝░
"""

# Úvod do FOR cyklů

# SEKVENCE
# Co je to sekvence v Pythonu a proč to potřebujeme vědět?
# SEKVENCE jsou, zjednodušeně, takové proměnné, které obsahují více položek, v nějakém pořadí.

# 1) STRING - S jednou sekvencí jsme se již potkali - STRING - je sekvence znaků.
# Co je to vlastně string, text? Nějaké znaky, v nějakém pořadí.

# např. tento string je sekvence písmen v abecedním pořadí
abeceda = "abcdefghijklmnopqrstuvwxyz"

# ... EXISTUJÍ I DALŠÍ SEKVENCE, ale v tuto chvíli si vystačíme se stringem ...

# Ochutnávka: později se seznámíme se seznamy, které vypadají třeba takto:
seznam_lidi = ["Sam", "Oskar", "Honza", "Filip", "Lukáš", "Leo", "Tobiáš", "Dmytro", "Diana", "Bohumír"]
# ... je vidět, že seznam je taky sekvence - v tomto případě je to sekvence za sebou jdoucích stringů.


################################################################################
###### FOR CYKLUS
################################################################################
"""
For cyklus podobně jako while cyklus slouží k tomu, když chceme VYKONAT NĚJAKÝ BLOK KÓDU VÍCEKRÁT.
Narozdíl od while cyklu, který se opakuje dokud je splněná podmínka, for cyklus se provede tolikrát, kolik
prvků má danná SEKVENCE. 

Ve for cyklu totiž narozdíl od while NENÍ ŽÁDNÁ PODMÍNKA. Místo toho očekává nějakou SEKVENCI.
Pojďme si to ukázat na příkladu.
"""

                                        ######  PŘÍKLAD 1 ######

# uděláme si string abeceda (což je sekvence znaků)
abeceda = "abcdefghijklmnopqrstuvwxyz"

# Jaká je délka tohoto stringu? Zjistíme to pomocí funkce len()
delka_abecedy = len(abeceda) # napíšu len(), do závorek dám string, jehož délka mě zajímá
print(delka_abecedy) # toto vypíše 26 (což je délka našeho stringu 'abeceda')

# FOR cyklus:
# Teď použijeme for cyklus k tomu, aby postupně prošel celou sekvenci, v tomto případě abeceda.
# Cyklus se provede tolikrát, kolik je délka sekvence, v našem případě 26x.
# Proměnné 'pismeno' se říká řídící proměnná a postupně nabývá hodnot ze sekvence - tedy v našem případě se cyklus
# spustí 26x a nejdříve je 'pismeno' a, pak b, pak c, d, e, f ... a tak dále. Uvnitř for cyklu se pak můžu rozhodnout,
# co s tím písmenem budu dělat. Nemusím s ním klidně dělat nic. My si ho zkusíme vypsat:

for pismeno in abeceda: # pismeno je řídící proměnná (může se jmenovat jakkoliv!), důležité je, že postupně nabývá hodnot písmen z abecedy
    # zde můžu proměnnou pismeno použít
    print(pismeno) # zde jsem se ji rozhodl vypsat

# Zkuste si tento příklad pustit! Co dělá a proč?

                                        ######  PŘÍKLAD 2 ######

# Ukažme si ješte jeden příklad. Co když bychom měli číslo a chtěli sečíst jeho číslice?
# Tedy například pro číslo 12345 chceme znát součet 1 + 2 + 3 + 4 + 5.

cislo = 12345

# for cislice in cislo: # TAKHLE to nejde, proč?

# ... protože int (číslo) není sekvence! Musíme z toho čísla udělat string, pokud jej chceme procházet ve for cyklu.

soucet = 0 # udělám si proměnnou, kam budu ukládat výsledek (součet číslic)
# 'cislice' zde bude řídící proměnná a bude postupně nabývat hodnot ze stringu "12345"
for cislice in str(cislo):
    # cyklus se provede tolikrát, kolik má string "12345" znaků
    # každou číslici (znak) chci přičíst do svého součtu
    # nemůžu ale sčítat stringy, nesmím proto zapomenou přetypovat string ("5") na int (5)
    soucet = soucet + int(cislice) # soucet se bude rovnat to co předtím, PLUS do něj ještě přidám hodnotu číslice

# po skončení for cyklu vypíšu výsledek
print("Součet číslic v čísle " + str(cislo) + " je " + str(soucet) + ".")


"""
█████████████████████████▀███████
█▄─▄▄▀██▀▄─██▄─▀█▄─▄█─▄▄▄▄█▄─▄▄─█
██─▄─▄██─▀─███─█▄▀─██─██▄─██─▄█▀█
▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀

Velmi často se společně s for cyklem používá funkce RANGE. Ta umí vygenerovat čísla z nějakého rozsahu a ten rozsah pak
můžeme použít jako sekvenci, kterou dáme for cyklu. Nejlepší bude ukázat si to na příkladech.

"""

# RANGE
# tato metoda se hojně používá spolu s for cyklem
# pokud jí dáte jeden parametr (číslo), generuje hodnoty od 0 až do toho čísla
# pokud dostane dva parametry, generuje čísla v jejich rozmezí např. range(0, 10) generuje 0 1 2 3 ... 9 (10 už ne!)
# případný třetí parametr udává step (skok), tedy o kolik se hodnota zvětší po každém cyklu
#   ---> range(0, 10, 2) generuje čísla od 0 do 9, ale skáče vždy o dva: 0 2 4 6 8

# proměnná i postupně nabývá hodnot 0 - 9, cyklus se tedy provede 10x
for i in range(10): # range vygeneruje čísla 0 1 2 3 4 5 6 7 8 9 a řídící proměnná postupně nabývá těchto hodnot
    print(i)

# proměnná i postupně nabývá hodnot 1 - 10, cyklus se tedy provede 10x
for i in range(1,11):
    print(i)

# proměnná i nabývá sudých hodnot od 2 do 99 (2 4 6 8 ... 94 96 98) - skok je dva
for i in range(2,100,2):
    print(i)

pocet_tiku = 5 # určíme kolikrát ma program tiknout
for i in range(pocet_tiku): # cyklus se provede 5x, sekvence je totiž 0 1 2 3 4 - tedy 5 čísel, a pro každé se cyklus provede jednou
    # všimněte si, že zde ani nepoužívám hodnotu řídící proměnné 'i', k ničemu ji totiž nepotřebuji
    # ne vždy mě totiž zajímají prvky sekvence, občas chci prostě jen něco zopakovat několikrát
    print("Tik tak.") # například to, že budu jednoduše vypisovat "Tik tak."

print("Crrrrrr.") # Po skončení for cyklu vypíšu Crrrrrr. (Budík dotikal ...)

# VNOŘENÝ FOR CYKLUS
# Podobně jako podmínky či while cyklus, můžeme do sebe vnořovat více for cyklů.
# Akorát si musíme dát pozor na odsazení, s každým dalším for cyklem, podmínkou, while cyklem atd.
# se začátek řádku posouvá dále doprava.


print("Tabulka malé násobilky:")
for j in range(1, 11): # Pro všechny čísla od 1 do 10 (11 se nepočítá), udělej toto:
    for i in range(1, 11): # Vem všechny čísla od 1 do 10 a ...
        print(i * j) # obě čísla vynásob a vypiš výsledek
    print()

# Kontrolní otázky k příkladu s malou násobilkou:
#   - Kolik celkem cyklů se provede?
#   - Proč se řídící proměnné jmenujou jinak?


"""
Úkol 1: Vypsat čísla od 1 do 100

Vypište čísla od 1 do 100, každé na nový řádek. Využijte for cyklus.
"""


"""
Úkol 2: Číselná pyramida

Udělej program, který se zeptá uživatele na výšku pyramidy a pak vypíše pyramidu z čísel. Např. pokud uživatel zadá 5,
tak program vypíše tuto pyramidu:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

"""
Úkol 3: Diamant

Udělej program, který vypíše následující obrazec:

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

Použij for cyklus.
"""

"""
Úkol 4: Prvočísla (BONUSový úkol)

Řekni uživateli ať zadá nějaké číslo.
Udělej program, který vypíše všechna prvočísla menší než to číslo, které uživatel zadal.
"""