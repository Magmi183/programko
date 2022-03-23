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

# ELIF
# Hodí se také umět pracovat s více možnostmi, tedy nemít jenom když a jinak.
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


"""
Úkol 1: Horská dráha

Zeptejte se uživatele kolik měří centimetrů.
Pokud má 180 a více, řekněte mu, že může na horskou dráhu.
Pokud má méně, s lítostí mu oznamte, že kvůli bezpečnostním důvodům na horskou dráhu bohužel nesmí.

"""

vyska = input("Zadej výšku:\n")
vyska = int(vyska)
if vyska < 180:
    print("Na horskou dráhu bohužel nesmíš")
else:
    print("Vítej!")

"""
Úkol 2: Porovnávač čísel

Načtěte od uživatele dvě čísla a řekněte, jestli jsou stejná. Pokud nejsou, 
řekněte, jestli je větší první, nebo druhé číslo.
"""

cislo1 = int(input("Zadej první číslo:\n"))
cislo2 = int(input("Zadej druhé číslo:\n"))
if cislo1 == cislo2:
    print("Čísla jsou stejná!")
elif cislo1 > cislo2:
    print("První číslo je větší.")
else:
    print("Druhé číslo je větší.")


"""
Úkol 2.5: Největší číslo

Načtěte od uživatele tři čísla a řekněte, které z nich je největší. Pokud je největších čísel více, nevypisujte nic, nebo
řekněte, že je jich víc.
"""

cislo1 = int(input("Zadej první číslo:\n"))
cislo2 = int(input("Zadej druhé číslo:\n"))
cislo3 = int(input("Zadej třetí číslo:\n"))

if cislo1 > cislo2:
    if cislo1 > cislo3:
        print("Největší číslo je: " + str(cislo1))
    elif cislo3 > cislo1:
        print("Největší číslo je: " + str(cislo3))
else:
    if cislo2 > cislo3:
        print("Největší číslo je: " + str(cislo2))
    elif cislo3 > cislo2:
        print("Největší číslo je: " + str(cislo3))





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

bodu = input("Kolik si dostal bodů:\n")
if int(bodu) >= 90:
    print("Dostal jsi známku: 1")
elif int(bodu) >= 75:
    print("Dostal jsi známku: 2")
elif int(bodu) >= 60:
    print("Dostal jsi známku: 3")
elif int(bodu) >= 45:
    print("Dostal jsi známku: 4")
else:
    print("Dostal jsi známku: 5")


"""
Úkol 4: Studium na vysoké škole
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

if maturita == True and prijimacky == True and vek >= 18:
    print("Gratuluji, můžeš nastoupit ke studiu.")
elif celejmeno == "Albert Einstein":
    print("Gratuluji, můžeš nastoupit ke studiu.")
else:
    print("Nesplňuješ podmínky, nashle.")


"""Úkol 5: Trojúhelník

Zeptejte se uživatele na 3 čísla - délky stran trojúhelníku.
Řekněte mu, jestli je trojúhelník platný. Aby byl trojúhelník platný, ani jedna ze stran nesmí být větší, než zbylé dvě dohromady.

"""

strana1 = float(input("Zadej 1 stranu: \n"))
strana2 = float(input("Zadej 2 stranu: \n"))
strana3 = float(input("Zadej 3 stranu: \n"))

if strana1+strana2 > strana3 and strana1+strana3 > strana2 and strana3+strana2 > strana1:
    print("Ano, z těchto stran se dá složit trojúhelník.")
else:
    print("Z těchto stran se nedá složit trojúhelník.")

"""
Úkol 6: Progresivní daň

Zeptejte se uživatele, kolik dostal peněz a spočítejte mu, kolik celkem zaplatí na daních.

Pokud má uživatel příjem menší nebo rovno 100 tisíc, zaplatí daň 15 procent.
Pokud má více, zaplatí daň 15 procent z prvních 100 tisíc, ale peníze nad 100 % zdaní sazbou 23 procent.
Pokud je to zloděj, na daních nezaplatí nic.
"""
zlodej = input("Jsi zloděj? Zadej ano nebo ne.")
prijem = int(input("Zadej příjem: \n"))
if zlodej == "ano":
    print("Na daních zaplatíš: " + str(0) + " korun.")
elif prijem <= 100000:
    print("Na daních zaplatíš: " + str(prijem*0.15) + " korun.")
else:
    print("Na daních zaplatíš: " + str(100000*0.15 + (prijem-100000)*0.15) + " korun.")
