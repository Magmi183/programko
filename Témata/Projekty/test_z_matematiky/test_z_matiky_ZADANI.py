
""" Zadání:
#### TEST Z MATEMATIKY ####
###########################

Úkolem bude udělat program, který bude uživateli dávat příklady a na konci ho oznámkuje.
Uživatel si před každým příkladem vybere, jestli chce příklad na sčítání, odčítání, násobení, nebo dělení.
Na konci se také uživateli znovu zobrazí všechny příklady, které měl špatně.
"""



"""
## 1. ČÁST

Jako první udělejte program, který dá uživateli pouze jeden příklad a to na sčítání.
Pokud uživatel odpoví správně, přičtěte mu bod.

POSTUP:
1. Přivítejte uživatele.
2. Udělejte proměnnou, kam si budete ukládat, kolik má uživatel bodů. Za každý příklad správně je jeden bod.
3. Udělejte si dvě proměnné a dejte do nich náhodná čísla. Jak se dělá náhodné číslo je ukázáno níže.
4. Udělejte si proměnnou výsledek, kam uložíte součet těch dvou čísel.
5. Zeptejte se uživatele, kolik si myslí, že je výsledek a jeho odpověď si uložte do proměnné.
6. Pomocí podmínky (if, else) zjistěte, zda je je výsledek stejný jako odpověď a jestli jo, tak dejte uživatelovi bod.
   Kromě přičtení bodu ještě uživateli řekněte, jestli odpověděl dobře, nebo špatně. Pokud to měl špatně, řekněte mu,
   co byla správná odpověď.
"""

import random # Tento řádek mějte nahoře v programu, stačí jednou
nahodne_cislo = random.randrange(0,10) # Takto vygenerujete náhodné číslo od 0 do 10 a uložíte do proměnné



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



"""
## 4. ČÁST

Teď do programu přidáme známkování. Uživatel už ví, kolik dostal bodů, ale zajímá ho i, co je to za známku.

POSTUP:
1. Udělejte si proměnnou 'znamka' a dejte do ní hodnotu nula (nebo cokoliv jiného, pak to přepíšem).
2. Na konci programu, tedy po skončení cyklu, udělejte velkou podmínku if/elif/elif/... a podle toho kolik
   bodů uživatel nasbíral nastavte proměnnou známka.
3. Známkování:
    - 9 až 10 bodů: 1
    - 7 až 8  bodů: 2
    - 6       bodů: 3
    - 4 až 5  bodů: 4
    - 0 až 3  body: 5
"""



"""
## 5. ČÁST

Abychom mohli uživateli na konci říci, které příklady měl špatně, musíme si je průběžne ukládat.
Na to se hodí seznam.

POSTUP:
1. Někde na začátku programu vytvořte prázdný seznam, např. jménem 'spatne_priklady'.
2. Před částí, kde se ptáte uživatele na odpověď si udělejte proměnnou 'priklad', do které vložte příklad, na který se
   zrovna chcete ptát, něco jako priklad = str(cislo1) + znamenko + str(cislo2)
3. Pokud uživatel odpoví špatně, vložte tento příklad do vašeho seznamu pomocí metody append. (spatne_priklady.append(priklad)).
4. Na konci programu seznam vypište libovolným způsobem, stačí print(spatne_priklady).
"""



"""
## BONUS

Dodělejte program tak, aby fungovalo i dělení. Výsledek dělení by ale vždy mělo být celé číslo. 
Přidejte daší funkcionalitu, dle vlastní fantazie.
"""