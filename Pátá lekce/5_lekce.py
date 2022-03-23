# Příklad na připomenutí

# Společně programujeme, step-by-step: Chci udělat program, kde uživatel zadá jedno písmeno,
# podle toho jestli je kluk (m) nebo holka (h) a program mu řekne, jestli může jen na klučičí tábor.

pass

# Proč jsou příkazy pod ifem odsazené (nezačínají na začátku řádku) ?

# Společně:
# Jaké budou výsledky těchto výrazů?

print(8 < 7)
print(32 > 9)
print(33 == 333)
print(9 * 3 == 27) # násobení má přednost před porovnáním!

# ELIF
# Hodí se také umět pracovat s více možnostmi, tedy nemít jenom když a jinak.
# Můžeme udělat program ve stylu: Pokud je ti méně než 6 let, tak ... Jinak pokud je ti méně než 18, tak...
# Pokud je ti méně než 65 ... A tak dále. Takže můžeme udělat podmínku, která rozlišuje mnoho možností.
vek = int(input())
if vek < 6:
    print("předškolák")
elif vek < 18:        # testuje se, pokud neplatí předchozí podmínka
    print("školák")
elif vek < 65:        # testuje se, pokud neplatí ani jedna předchozí podmínka
    print("dospělý ")
else:                 # provede se, pokud neplatí ani jedna předchozí podmínka
    print("důchodce")
print("Zdravím tě") # Tenhle příkaz není odsazený, spustí se proto vždy, nehledě na věk.

# Vnořený if/else

# Podmínky do sebe můžeme libovolně vnořovat. Jediné pravidlo je, že když použijeme další podmínku, musíme další příkazy ještě víc odsadit.
cislo1 = int(input())
cislo2 = int(input())
if cislo1 == cislo2:
    if cislo1 > cislo2:
        # toto je vnořená podmínka, kód zde se provede, když obě podmínky nahoře platí
        print("Obě podmínky jsou True")
    else:
        # vnořený else, příkazy zde se provedou, když první podmínka platí, ale druhá už ne
        print("Pouze první podmínka je True")
else:
    print("První podmínka je False")

cislo = int(input())
if cislo>0:
    if cislo>1:
        if cislo>2:
            if cislo>3:
                print("Tohle je hodně vnořená podmínka, ale je dost ošklivá. Jak ji zjednodušit?")


cislo = float(input("Zadej číslo!\n"))
if cislo >= 0:
    if cislo == 0:
        print("Nula")
    else:
        print("Kladné číslo")
else:
    print("Záporné")


"""
Úkol 2: Porovnávač čísel

Načtěte od uživatele dvě čísla a řekněte, jestli jsou stejná. Pokud nejsou, 
řekněte, jestli je větší první, nebo druhé číslo.
"""

"""
Úkol 2.5: Největší číslo

Načtěte od uživatele tři čísla a řekněte, které z nich je největší. Pokud je největších čísel více, nevypisujte nic, nebo
řekněte, že je jich víc.
"""


"""
Úkol 3: Známkování testu
Zeptejte se uživatele kolik dostal bodů z testu. 
Podle počtu bodů mu udělte známku.
Známkování si vymyslete. Např. 40 a více bodů jednička, 35 a více bodů dvojka... 20 a méně bodů za pět.
"""



# ***!!!!!!!***
# Logické výrazy
# dobrý zdroj: https://www.umimeinformatiku.cz/programovani-logicke-vyrazy

# OPAKOVÁNÍ
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


"""Úkol 5: Trojúhelník

Zeptejte se uživatele na 3 čísla - délky stran trojúhelníku.
Řekněte mu, jestli je trojúhelník platný. Aby byl trojúhelník platný, ani jedna ze stran nesmí být větší, než zbylé dvě dohromady.

"""

strana1 = float(input("Zadej 1 stranu: \n"))
strana2 = float(input("Zadej 2 stranu: \n"))
strana3 = float(input("Zadej 3 stranu: \n"))


"""
Úkol 6: Progresivní daň

Zeptejte se uživatele, kolik dostal peněz a spočítejte mu, kolik celkem zaplatí na daních.

Pokud má uživatel příjem menší nebo rovno 100 tisíc, zaplatí daň 15 procent.
Pokud má více, zaplatí daň 15 procent z prvních 100 tisíc, ale peníze nad 100 % zdaní sazbou 23 procent.
Pokud je to zloděj, na daních nezaplatí nic.
"""
zlodej = input("Jsi zloděj? Zadej ano nebo ne.")
prijem = int(input("Zadej příjem: \n"))