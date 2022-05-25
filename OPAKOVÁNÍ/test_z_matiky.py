"""
Tato úloha slouží k zopakování téměř všech témat, co jsme zatím dělali:
- vstup/výstup, proměnné, podmínky, cyklus, seznam ...

Program dělejte postupně podle návodu. Jsou zde napsané kroky, které je třeba udělat, programování je ale na vás.
"""

""" Zadání:
#### TEST Z MATEMATIKY ####
###########################

Úkolem bude udělat program, který bude uživateli dávat příklady a na konci ho oznámkuje.
Uživatel si před každým příkladem vybere, jestli chce příklad na sčítání, odčítání, násobení, nebo dělení.
"""

"""
## 1. ČÁST

Jako první udělejte program, který dá uživateli pouze jeden příklad a to na sčítání.
Pokud uživatel odpoví správně, přičtěte mu bod.

POSTUP:
1. Přivítejte uživatele.
2. Udělejte proměnnou, kam si budete ukládat, kolik má uživatel bodů. Za každý příklad správne je jeden bod.
3. Udělejte si dvě proměnné a dejte do nich náhodná čísla. Jak se dělá náhodné číslo je ukázáno níže.
4. Udělejte si proměnnou výsledek, kam uložíte součet těch dvou čísel.
5. Zeptejte se uživatele, kolik si myslí, že je výsledek a jeho odpověď si uložte do proměnné.
6. Pomocí podmínky (if, else) zjistěte, zda je je výsledek stejný jako odpověď a jestli jo, tak dejte uživatelovi bod.
   Kromě přičtení bodu ještě uživateli řekněte, jestli odpověděl dobře, nebo špatně. Pokud to měl špatně, řekněte mu,
   co byla správná odpověď.
"""

import random # Tento řádek mějte nahoře v programu, stačí jednou
nahodne_cislo = random.randrange(0,10) # Takto vygenerujete náhodné číslo od 0 do 10 a uložíte do proměnné

print("Vítej. Užij si testík.") # 1
body = 0 # 2
cislo1 = random.randrange(0,10) # 3
cislo2 = random.randrange(0,10) # 3
vysledek = cislo1 + cislo2 # 4
odpoved = int(input("Kolik je " + str(cislo1) + " + " + str(cislo2) + "?\n")) # 5
if vysledek == odpoved: # 6
    print("Správně! Dostáváš bod.")
    body += 1
else:
    print("Špatně. Výsledek je: " + str(vysledek) + ".")

"""
## 2. ČÁST

V této části do programu přidáme odčítání a násobení (dělení zatím ne).

POSTUP:
1. Ještě než spočítáte výsledek programu (před proměnnou výsledek), zeptejte se uživatele, jestli chce příklad na
   sčítání, odčítání, nebo násobení. (uživatel zadá +, - nebo *) Uložte si to do proměnné 'znamenko'.
2. Proměnnou výsledek nastavte na 0. Později do ní uložíme správnou hodnotu, ještě nevíme, jestli to bude součet, rozdíl....
3. Udělejte podmínku (if,elif,elif) podle toho co uživatel zadal. (if znamenko == "+":) atd.
   V každé podmínce spočtěte kolik má být výsledek a uložte si ho do proměnné. Výsledek se bude lišit podle toho,
   jestli čísla sčítáme, odčítáme či násobíme.
4. Zeptejte se uživatele, kolik je výsledek - pozor, místo plusu použijte správné znaménko! (Stačí jen upravit starý
   program.)
"""

print("Vítej. Užij si testík.")
body = 0
cislo1 = random.randrange(0,10)
cislo2 = random.randrange(0,10)
znamenko = input("Chceš příklad na sčítání, odčítání nebo násobení? Zadej +, -, nebo *.\n") # 1
vysledek = 0 # 2
if znamenko == "+": # 3
    vysledek = cislo1 + cislo2
elif znamenko == "-":
    vysledek = cislo1 - cislo2
elif znamenko == "*":
    vysledek = cislo1 * cislo2
odpoved = int(input("Kolik je " + str(cislo1) + znamenko + str(cislo2) + "?\n")) # 4
if vysledek == odpoved: # 6
    print("Správně! Dostáváš bod.")
    body += 1
else:
    print("Špatně. Výsledek je: " + str(vysledek) + ".")

"""
## 3. ČÁST

V této části zařídíme to, aby uživatel dostal příkladů více. Tedy aby se určitá část programu opakovala. Příkladů v testu
chceme celkem 10. Maximální počet bodů tedy bude 10.

POSTUP:
1. Zamyslete se, kterou část programu budete chtít opakovat (dát do cyklu).
2. Udělejte si proměnnou 'pocitadlo', které bude udávat, kolikátý příklad právě budeme zobrazovat. Na začátku ji nastavte
   na 1 (nejdřív zobrazíme příklad číslo 1).
3. Celou část programu, kde se generují čísla, počítá výsledek, zadává odpověď a přičítají body obalte do while cyklu. 
     - Označte si řádky, které chcete dát to cyklu a zmáčkněte tabulátor. Potom napište while.
     - Podmínka u while cyklu bude, že příklad který budu zobrazovat je menší nebo rovno 10 (while pocitadlo <= 10:). To znamená, že když
       začínám od 1, tak dostanu celkem 10 příkladů.
4. Na konci cyklu (ale ještě uvnitř) nezapomeňte počítadlo zvětšit o 1. Jinak by program dával příklady do nekonečna.
5. Na konci programu (za while cyklem) řekněte uživateli, kolik celkem nasbíral bodů.
"""

print("Vítej. Užij si testík.")
body = 0
pocitadlo = 1  # 2
while pocitadlo <= 10: # 3
    cislo1 = random.randrange(0,10)
    cislo2 = random.randrange(0,10)
    znamenko = input("Chceš příklad na sčítání, odčítání nebo násobení? Zadej +, -, nebo *.\n") # 1
    vysledek = 0 # 2
    if znamenko == "+": # 3
        vysledek = cislo1 + cislo2
    elif znamenko == "-":
        vysledek = cislo1 - cislo2
    elif znamenko == "*":
        vysledek = cislo1 * cislo2
    odpoved = int(input("Kolik je " + str(cislo1) + znamenko + str(cislo2) + "?\n")) # 4
    if vysledek == odpoved: # 6
        print("Správně! Dostáváš bod.")
        body += 1
    else:
        print("Špatně. Výsledek je: " + str(vysledek) + ".")
    pocitadlo += 1

print("Celkem si nasbíral " + str(body) + " bodů.")