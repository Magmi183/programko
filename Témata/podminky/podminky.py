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

# co když ale uživateli nebylo 18? Pro to máme příkaz else (jinak)
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

░█▀▀█ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀█ 
░█▄▄█ ░█──░█ ─▄▄▄▀▀ ░█──░█ ░█▄▄▀ 
░█─── ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█─░█

NEŽ BUDEŠ ČÍST DÁLE - TEĎ JE DOBRÝ ČAS ZKUSIT SI ÚLOHY 1. - 3. NA PROCVIČENÍ ZÁKLADNÍCH PODMÍNEK
POTOM MŮŽEŠ POKRAČOVAT DÁLE V MATERIÁLECH
"""

# ----------------------------------------------------------
# Vnořený if/else

# Podmínky do sebe můžeme libovolně vnořovat. Jediné pravidlo je, že když použijeme další podmínku, musíme další příkazy ještě víc odsadit.
vek = int(input())
obcan_cr = input("Zadej jestli jsi občan ČR (ano/ne)").lower()
if vek >= 18:
    print("Můžeš jít k volbám.")
    if vek >= 40:
        if obcan_cr == "ano":
            # toto je vnořená podmínka, kód zde se provede, když všechny tři podmínky nahoře platí
            print("Můžeš kandidovat na prezidenta.")
    else:
        # vnořený else, příkazy zde se provedou, když první podmínka platí, ale druhá už ne
        print("Nemůžeš kandidovat na prezidenta.")
else:
    print("Nemůžeš jít k volbám.")

cislo = int(input())
if cislo>0:
    if cislo>1:
        if cislo>2:
            if cislo>3:
                print("Tohle je hodně vnořená podmínka, ale je dost ošklivá. Jak ji zjednodušit?")
            print("")

cislo = float(input("Zadej číslo!\n"))
if cislo >= 0:
    if cislo == 0:
        print("Nula")
    else:
        print("Kladné číslo")
else:
    print("Záporné")
