"""
                        ███████╗██╗░░░██╗███╗░░██╗██╗░░██╗░█████╗░███████╗
                        ██╔════╝██║░░░██║████╗░██║██║░██╔╝██╔══██╗██╔════╝
                        █████╗░░██║░░░██║██╔██╗██║█████═╝░██║░░╚═╝█████╗░░
                        ██╔══╝░░██║░░░██║██║╚████║██╔═██╗░██║░░██╗██╔══╝░░
                        ██║░░░░░╚██████╔╝██║░╚███║██║░╚██╗╚█████╔╝███████╗
                        ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚══════╝
"""

# Naklonujte si projekt Python želva

# 1) Připomeň si, jak se s želvou pohybuje, mění barvy atd.
#   - jestli nevíš, koukni do souboru zelva-navod.py, kde je návod na základni práci s želvou

"""
2) Zatím bez vlastních funkcí, udělej želví program, který udělá tyto kroky, jak jdou za sebou:
    - nakresli ČERVENÝ čtverec, jehož strany jsou dlouhé 100 ( ... forward(100) ... )
    - nakresli MODRÝ čtverec, jehož strany jsou dlouhé 100 ( ... forward(100) ... )
    - nakresli ZELENÝ čtverec, jehož strany jsou dlouhé 100 ( ... forward(100) ... )
    
Kde na obrazovce čtverce budou je jedno.
"""

"""
PRVNÍ VLASTNÍ FUNKCE - Zavolej si mě pro tutorial!
3) Kód, který kreslí čtverec o hraně délky 100 dej do funkce. Zatím to bude funkce bez parametrů. Tedy vždy bude kreslit
čtverec s hranami délky 100 a na barvu zatím vůbec nešahá - používá tu, co je nastavená.

Potom svůj program uprav tak, aby na kreslení čtverce používal tu funkci. Stále ale zachovej barvy čtverců, to znamená,
že musíš příkaz color(barva) volat vždy před zavoláním funkce.
"""

"""
FUNKCE BEZ PARAMETRŮ:
Nejdříve si ukážeme nejjednoduší případ funkce - bez parametrů. Obecně funkce používáme, když máme nějaký kus kódu, který 
chceme používat na více místech. Pokud máme v programu na více místech stejný kód (na více řádků), děláme něco špatně a
ten kód je pravděpodobně ošklivý. 

Ukažme si to na jednoduchém příkladu:
"""

# Program, který vypíše malou násobilku čísla 8
# pro přehlednost pak ještě oddělí čárou
cislo = 8
for i in range(11):
    print(f"{i} * {cislo} = {cislo * i}")
print("------------------------------------------------------------------")


# ... a teď nějaký další, random kód ...
print("Tak to byla ta násobilka.")
print("Chceš ji vidět znovu?")
print("OK...")
# ... teď, když ji chceme vytisknout znovu, musíme opsat ten kód


cislo = 8
for i in range(11):
    print(f"{i} * {cislo} = {cislo * i}")
print("------------------------------------------------------------------")


# No jo, ale co když v tom programu třeba byla chyba? Tak ji musíme opravit na více místech. A navíc je toho kódu víc,
# je to méně přehledné...

# Proto z toho uděláme funkci!! Znovupoužitelný kus kódu.

# napíšu def název_funkce():
def ukaz_nasobilku_8(): # do závorek se dávají parametry, které mi ale zatím nemáme
    cislo = 8
    for i in range(11):
        print(f"{i} * {cislo} = {cislo * i}")
    print("------------------------------------------------------------------")

# ... a teď můžu jednoduše volat funkci, kterou jsem si vyrobil!
# ... a kolikrát chci!
ukaz_nasobilku_8()
ukaz_nasobilku_8()
ukaz_nasobilku_8()
ukaz_nasobilku_8()

"""
FUNKCE S PARAMETREM
4) Pokud už máš funkci, která kreslí čtverec a program, který nakreslí červený, modrý a zelený čtverec, tak do funkce přidej
parametr barvy tak, ať nemusíš barvu psát před funkcí a můžeš ji rovnou říct, jakou barvu čtverce chceš.

Program pak uprav tak, ať používá tuto funkci.
"""

"""
FUNKCE S PARAMETREM:

Pokud používám funkci bez parametrů, tak ta vždycky dělá to samé. Často ale chci dělat podobnou věc, ale ne úplně stejně.
Co když bych chtěl ukázat malou násobilku čísla 9 místo 8? Ten program je stejný, akorát se změní jedna proměnná. 
V takovém případě použiju funkci s parametrem.
"""

# do závorek napíšu parametr, který pak musím zadat, až funkci budu volat
def ukaz_nasobilku(cislo):
    for i in range(11):
        print(f"{i} * {cislo} = {cislo * i}")
    print("------------------------------------------------------------------")

ukaz_nasobilku(10)
ukaz_nasobilku(5)

def pozdrav(jmeno):
    print("Zdar " + jmeno)

"""
FUNKCE S VÍCE PARAMETRY
5) Do funkce která kreslí čtverec nějaké barvy přidej ještě další parametr: velikost hrany čtverce.

Program pak uprav tak, ať používá tuto funkci. První čtverec bude mít velikost 100, druhý 200 a třetí 123. Barvy zůstanou
jako v předešlých úkolech.
"""

"""
FUNKCE S VÍCE PARAMETRY:

Do funkce jednoduše přidám další parametr - do těch závorek, za ten první. Např.:
"""

def zkontroluj_vek(jmeno, prijmeni, vek):
    if vek < 18:
        print("Omlouvám se, pane " + jmeno + " " + prijmeni + ", ale sem vás pustit nemůžu.")
    else:
        print("Vítej " + jmeno + " " + prijmeni)

zkontroluj_vek("René", "Novák", 20)
zkontroluj_vek("Kamil", "Smith", 7)

# Hezké a jednoduché shrnutí funkcí je zde:
# https://www.umimeinformatiku.cz/programovani-funkce
## -----------------------------------------------------------------------------
# Další úkoly

# 1 - MNOHOÚHELNÍK
# Udělej funkci, která kreslí mnohoúhelník. Jako parametr přijímá N (kolika úhelník to má být)

# Dále: Vyber si aspoň 2 další úlohy zde: https://www.umimeinformatiku.cz/programovani-funkce
# A vypracuj je. (Úlohy jsou dole v sekci Python Želva)

# TO-DO: Tento úvod by měl obsahovat pouze příklady s želvou, tzn. jiné příklady jako je násobilka smazat.
# K detailnějšímu vysvětlení funkcí pak bude sloužit jiná "lekce".