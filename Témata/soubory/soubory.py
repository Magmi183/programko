"""
                        ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░██████╗░██╗░░░██╗
                        ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
                        ╚█████╗░██║░░██║██║░░░██║██████╦╝██║░░██║██████╔╝░╚████╔╝░
                        ░╚═══██╗██║░░██║██║░░░██║██╔══██╗██║░░██║██╔══██╗░░╚██╔╝░░
                        ██████╔╝╚█████╔╝╚██████╔╝██████╦╝╚█████╔╝██║░░██║░░░██║░░░
                        ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
Dobré zdroje: https://naucse.python.cz/lessons/beginners/files/
              https://www.itnetwork.cz/python/soubory/prace-s-textovymi-soubory-v-pythonu
"""

# Budeme se zabývat prací s TEXTOVÝMI SOUBORY
# Soubory, které jsou použity pro ukázky v této lekci (a na úlohy) se nacházejí ve složce "texty"


# OTEVŘENÍ SOUBORU
# k otevření souboru používáme příkaz open

# otevřeme soubor a uchováme si jej v proměnné "basnicka"
basnicka_soubor = open("texty/python-krouzek-basnicka.txt", encoding="utf-8")

# PŘEČTENÍ SOUBORU
# soubor jsme otevřeli, ale pokud chceme získat jeho obsah, musíme na něm zavolat metodu read

# na souboru který chci přečíst zavolám metodu read()
basnicka_text = basnicka_soubor.read()

# ZAVŘENÍ SOUBORU
# po tom co už soubor nepotřebujeme (jeho obsah už jsme si přečetli), musíme soubor ZAVŘÍT
# pokud to neuděláme, může se stát, že se ostatní programy k souboru nebudou moci dostat, jelikož operační systém si
# bude myslet, že se souborem stále pracujeme a čeká, až mu dáme najevo, že jsme skončili (pomocí zavolaní metody close)

basnicka_soubor.close()

# Soubory se dají přirovnat k ledničce: abys něco mohl/a z ledničky vzít, nebo dát dovnitř, musíš ji předtím otevřít a potom zavřít.
# Bez zavření to sice na první pohled funguje taky, ale pravděpodobně potom brzo něco zplesniví. Zdroj: python.cz

# VYPSÁNÍ OBSAHU
# obsah jsme si už přečetli - načetli jsme si jej do proměnné, pojďme se na něj podívat
print(basnicka_text)
# ... zajímavá básnička, autor: ChatGPT, 2023

######## AUTOMATICKÉ ZAVÍRÁNÍ SOUBORŮ ########
# Většinou se soubory otevírají společně s příkazem with, který zajistí to, že se soubor automaticky zavře.

with open("texty/python-krouzek-basnicka.txt", encoding="utf-8") as basnicka_soubor:
    basnicka_text = basnicka_soubor.read()
    # soubor se automaticky zavře, když blok skončí
    # zde je stále otevřený
    print("Soubor je stále otevřený.")


# zde už je soubor zavřený (skončil with blok)
print("Zde už je soubor zavřený.")


# POUŽITÍ FOR CYKLU SE SOUBOREM (ITERACE NAD SOUBOREM)
# Soubor můžeme procházet for cyklem, řádek po řádku. (Jak počítač pozná, kde začíná další řádek?)

print("+----------------------------------------------------------------+")
# otevřeme soubor - obsahuje jméno kluka a informace o něm (Autor: ChatGPT, 2023)
with open("texty/deti.csv", encoding="utf-8") as deti:

    # první řádek načteme manuálně - jedná se o pojmenování sloupců, mohlo by nám to zkazit práci ve for cyklu
    pojmenovani_sloupcu = deti.readline() # když řádek načteme takhle, ve for cyklu se už procházet nebude

    for radek in deti: # procházíme soubor řádek po řádku
        # print(radek) # takhle by řádky byly odděleny prázdným řádkem, musíme použít end="", proč?
        print(radek, end="")

print("+----------------------------------------------------------------+")


####################
# >>  PSANÍ DO SOUBORU
# - - - - - - - - -

# Často nechceme soubor jen číst, ale buď ho změnit (založit/přepsat) nebo do něj něco přidat. Tyto dva scénáře
# je nutno odlišit. Liší se je mírně - způsobem, jakým voláme metodu open.

# ZALOŽENÍ SOUBORU/PŘEPSÁNÍ EXISTUJÍCÍHO

# použiji open s parametrem "w", jako write

with open("novy_soubor.txt", "w", encoding="utf-8") as soubor:
    # máme otevřený soubor, teď existuje víc možností, jak do něj něco zapsat

    # budeme zapisovat tyto zeleniny, které vygeneroval ChatGPT
    zeleniny = ["okurky", "mrkev", "kohlrabi", "červená řepa", "pastinák", "špenát", "křen", "fíkový kaktus", "ředkvičky", "jícama"]

    # Zapisování pomocí metody WRITE
    soubor.write("ZELENINY: ")
    for zelenina in zeleniny:
        # zeleninu do souboru zapíšu pomocí metody write
        soubor.write(zelenina + " ") # POZOR, write nedělá mezery/entery, musíme si je přidat

    # Zapisování pomocí PRINT
    ovoce = ["jablka", "banány", "hrušky", "kiwi", "mango", "granátové jablko", "pomelo", "tamarilo", "kaki",
             "rambutan"]
    print("- - - - - - - - - - - - - - -", file=soubor)
    print("OVOCE:", file=soubor, end=" ")
    for o in ovoce:
        # použijeme příkaz print jak jsme zvyklí, s tím rozdílem, že specifikuje, do jakého souboru chceme zapisovat
        #print(o, file=soubor)
        # příkaz print automaticky udělá nový řádek, pokud bychom místo toho chtěli např. mezeru, vypadalo by to takto:
        print(o, file=soubor, end=" ")


# TODO: Připsání do souboru


# SLOŽITĚJŠÍ PŘÍKLAD - HLEDÁNÍ TEPLOTNÍCH EXTRÉMŮ
"""
V souboru teploty.csv máme tisíce záznamů teplotních meření (smyšlené).
Každý jeden řádek (záznam) je tvořen trojicí: město, naměřená teplota, datum

Hodnoty jsou oddělené čárkami.

Naším úkolem je NAJÍT MĚSTO KDE BYLA NAMĚŘENA NEJVĚTŠÍ TEPLOTA.
"""

# otevřu soubor s teplotami
with open("texty/teploty.csv", encoding="utf-8") as teploty:
    # počáteční inicializace - prozatímní největší teplotu si nastavím na minus nekonečno, čímž zajístím, že jakákoliv jiná teplota bude větší
    max_teplota = float('-inf')
    max_mesto = "?"
    max_datum = "?"

    # for cyklem budu procházet soubor řádek po řádku a budu se dívat, jestli náhodou aktuální teplota není větší, než ta největší, kterou jsem zatíl viděl
    for zaznam in teploty:
        # řádek rozdělím podle čárky, text (string) se mi rozpadne do tří proměnných
        mesto, teplota, datum = zaznam.split(',')
        teplota = int(teplota) # převedení na číslo

        # koukám se, jestli náhodou naměřená teplota není největší, kterou jsem zatím potkal
        if teplota > max_teplota:
            # pokud ano, uložím si údaje o záznamu
            max_teplota = teplota
            max_mesto = mesto
            max_datum = datum

# podívám se na výsledek
print("Největší teplota byla " + str(max_teplota) + " ve městě " + max_mesto + " dne " + max_datum)




