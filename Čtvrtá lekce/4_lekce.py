# hezký zdroj na podmínky v Pythonu (v češtině) je zde: https://www.umimeinformatiku.cz/programovani-podmineny-prikaz-if
# nějaké text/kódy zde jsou právě z tohoto zdroje

# Zatím jsme dělali programy, které vždy vykonali každý příkaz, co jsme napsali.
# Co když ale chceme dělat rozdílné věci například na základě pohlaví uživatele?
# Nebo co když nechceme, aby program mohli používat děti pod 10 let?
# Použijeme PODMÍNKY. Podívejme se na následující kód:

vek = input()
vek = int(vek) # nesmíme zapomenout na přetypování!!! Jinak věk nemůžeme porovnávat jako číslo!
if vek >= 18:
    print("Vítej v casinu") # do casina smí pouze lidé, kterým je 18 nebo víc

# co když ale uživateli nebylo 18? Pro to máme přikaz else (jinak)
if vek >= 18:
    print("Vítej v casinu") # do casina smí pouze lidé, kterým je 18 nebo víc
else:
    print("Nesmíš do casina")

# VŠIMNĚTE SI POUŽITÍ MEZER
# Příkazy pod ifem/elsem musí být odsazené, aby python poznal, jaké příkazy patří k podmínce.
# Příkazy, které už nejsou odsazené už do podmínky nepatří.

# Hodí se také umět pracovat s více než dvěma výstupy, tedy nemít jenom když a jinak.
# Můžeme udělat program ve stylu: Pokud je ti méně než 6 let, tak ... Jinak pokud je ti méně než 18, tak...
# Pokud je ti méně než 65 ... A tak dále. Takže můžeme udělat podmínku, která rozlišuje mnoho možností.

if vek < 6:
    print("předškolák")
elif vek < 18:        # testuje se, pokud neplatí předchozí podmínka
    print("školák")
elif vek < 65:        # testuje se, pokud neplatí ani jedna předchozí podmínka
    print("dospělý ")
else:                 # provede se, pokud neplatí ani jedna předchozí podmínka
    print("důchodce")
print("Zdravím tě") # Tenhle příkaz není odsazený, spustí se proto vždy, nehledě na věk.

# ***!!!!!!!***
# Logické výrazy
# dobrý zdroj: https://www.umimeinformatiku.cz/programovani-logicke-vyrazy

# Často chceme porovnat hodnoty proměnných.
# Chceme například vědět, jestli jsou stejné. Pokud jde o čísla, často se nám hodí
# vědět, jestli je jedno větší než druhé atd. Výsledek porovnání je vždy True/False.
# Tedy zjistíme jestli to platí, nebo neplatí. Nic mezi tím.

# ROVNOST
# Pokud chceme zjistit, jestli mají dvě proměnné stejnou hodnotu, využiju operátor rovnosti.
# Jsou to dvě rovnítka. ==  (proč nemůže být jen jedno?)
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


"""
Úkol 1: Horská dráha

Zeptejte se uživatele kolik měří centimetrů.
Pokud má 180 a více, řekněte mu, že může na horskou dráhu.
Pokud má méně, s lítostí mu oznamte, že kvůli bezpečnostním důvodům na horskou dráhu bohužel nesmí.

"""

"""
Úkol 2: Porovnávač čísel

Načtěte od uživatele dvě čísla a řekněte, jestli jsou stejná. Pokud nejsou, 
řekněte, jestli je větší první, nebo druhé číslo.
"""


"""
Úkol 3: Známkování testu
Zeptejte se uživatele kolik dostal bodů z testu. 
Podle počtu bodů mu udělte známku.
Známkování si vymyslete. Např. 40 a více bodů jednička, 35 a více bodů dvojka... 20 a méně bodů za pět. Můžete se inspirovat touhle tabulkou:
< 50    5
50 - 69 4
70 - 79 3
80 - 89 2
90 +    1
"""

