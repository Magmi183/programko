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
    print("Vítej v casinu")
    print("Vítej v casinu")

print("....")
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

"""
Úkol 4: Největší číslo

Načtěte od uživatele tři čísla a řekněte, které z nich je největší. Pokud je největších čísel více, napište to uživateli.
"""

"""
Úkol 5: Studium na vysoké škole
Udělejte program, který uživateli řekne, jestli může nastoupit na VŠ.
Podmínky jsou následující: 
- musí mu být 18 let a víc
- musí mít maturitu
- musí mít složené přijímačky
- Pokud je jeho jméno Albert Einstein, nemusí splňovat nic z výše uvedeného.

Použijte kód níže. Pro otestování programu měňte hodnoty z False na True a obráceně.
"""

vek = int(input("Kolik je ti let?\n"))
celejmeno = input("Zadej své celé jméno.\n")
maturita = True
prijimacky = True


"""Úkol 6: Trojúhelník

Zeptejte se uživatele na 3 čísla - délky stran trojúhelníku.
Řekněte mu, jestli je trojúhelník platný. Aby byl trojúhelník platný, ani jedna ze stran nesmí být větší, než zbylé dvě dohromady.

"""

strana1 = float(input("Zadej 1 stranu: \n"))
strana2 = float(input("Zadej 2 stranu: \n"))
strana3 = float(input("Zadej 3 stranu: \n"))


"""
Úkol 7: Progresivní daň

Zeptejte se uživatele, kolik dostal peněz a spočítejte mu, kolik celkem zaplatí na daních.

Pokud má uživatel příjem menší nebo rovno 100 tisíc, zaplatí daň 15 procent.
Pokud má více, zaplatí daň 15 procent z prvních 100 tisíc, ale peníze nad 100 % zdaní sazbou 23 procent.
Pokud je to zloděj, na daních nezaplatí nic.
"""
zlodej = input("Jsi zloděj? Zadej ano nebo ne.")
prijem = int(input("Zadej příjem: \n"))