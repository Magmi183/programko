# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# PRACOVNÍ LIST
#
# Tento soubor slouží k procvičení důležitých konceptů, které pak můžeme využít při programování piškvorek.
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


"""
Téma 1: Seznam v seznamu
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# tohle jsou 3 obyčejné seznamy, každý má 3 položky
ovoce = ["🍎", "🍌", "🍇"]
zelenina = ["🥕", "🥒", "🍅"]
sladkosti = ["🍫", "🍪", "🍩"]

# Výpis délek seznamů
print("Délka seznamu ovoce je: " + str(len(ovoce)))
print("Délka seznamu zelenina je: " + str(len(zelenina)))
print("Délka seznamu sladkosti je: " + str(len(sladkosti)))

# Můžeme se podívat na položku na konkrétním míste, číslujeme OD NULY!
print("První položka v seznamu ovoce je: " + ovoce[0])
print("Druhá položka v seznamu zelenina je: " + ovoce[1])

# - - - - -
# Co se stane, když všechny 3 seznamy dáme ještě do jiného seznamu?
jidla = [["🍎", "🍌", "🍇"],
         ["🥕", "🥒", "🍅"],
         ["🍫", "🍪", "🍩"]]

# Délka bude 3!
# Je to proto, že seznam se počítá jako jedna položka.
print("Délka seznamu jídel je: " + str(len(jidla)))

# to ale znamená, že když uděláme:
print(jidla[0])
# ... vytiskne se celá první položka, to znamená celý seznam ["🍎", "🍌", "🍇"]!

# pokud bychom chtěli vytisknout nebo změnit konkrétní jídlo, musíme na to jít následovně:
print("První jídlo v prvním seznamu je: " + jidla[0][0])
print("Druhé jídlo v třetím seznamu je: " + jidla[2][1])

# Změnit jídlo, například vyměnit okurku za lilek, která je v druhém seznamu na druhém místě, můžeme následovně:
jidla[1][1] = "🍆"

"""
Úkoly 1:

Pracujte se seznamem jídel, který máte zadaný dole. Pak postupně udělejte následující úlohy:

1) Vyměňte lilek zpátky za okurku.
2) Nahraďte čokoládu za banán.
3) Nahraďte donut slovem "donut".

4) Zeptejte se uživatele, jaká věc z prvního řádku mu nejméně chutná (ať zadá 1, 2 nebo 3).
   Pak se ho zeptejte, jakým jídlem by tu věc chtěl nahradit a v seznamu ji nahraďte.
   Příklad: Uživatel zadá 3 (nechutnají mu hrozny) a pak zadá "párek v rohlíku", vaším úkolem je
   nahradit hrozny za párek v rohlíku (nemusíte emoji). POZOR: Musíte odečíst 1 od toho co uživatel zadá, protože
   v Pythonu se čísluje od nuly. Tedy když uživatel zadá např. 1 , tak v Pythonu to bude 0.
5) Zeptejte se uživatele na řádek a sloupec, pak jídlo na danné pozici smažte tak, že ho nahradíte za mezeru.
   Příklad: uživatel zadá 1, 2 - tedy první řádek a druhý sloupec, takže banán nahradíte za mezeru.
   
6) Pomocí for cyklu postupně vypište všechny pod-seznamy v seznamu jídel.
"""

jidla = [["🍎", "🍌", "🍇"],
         ["🥕", "🍆", "🍅"],
         ["🍫", "🍪", "🍩"]]



"""
Téma 2: Kontrola vstupu
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# představme si, že chceme, aby uživatel zadal své pohlaví
# očekáváme, že zadá muž nebo žena, pokud zadá nějaký nesmysl, zeptáme se znova

# poprvé se zeptáme mimo cyklus:
pohlavi = input("Zadej jestli jsi muž nebo žena prosím: ")

# budeme se ptát DOKUD pohlaví není muž NEBO dokud pohlaví není žena
# pokud uživatel zadal správně hned napoprvé, cyklus se neprovede ani jednou, což nevadí
while pohlavi != "muž" or pohlavi != "žena":
    pohlavi = input("Zadej jestli jsi muž nebo žena prosím: ")


# v piškvorkách řešíme podobný problém, chceme, aby uživatel zadal ŘÁDEK a SLOUPEC
# obojí musí být v rozmezí 1 až 3, protože máme přesně 3 řádky a každý má 3 sloupce


radek = int(input("Zadej řádek: "))
while radek < 1 or radek > 3:
    print("Zadal jsi moc malé nebo velké číslo, zkus to znovu.")
    radek = int(input("Zadej řádek: "))

"""
Úkoly 2:

1) Zeptej se uživatele na řádek i sloupec a u obojího prověď kontrolu vstupu. Až bude obojí správně, hodnoty vypiš.
   Nápověda: Mechanismus pro řádek už je hotový v ukázce, stačí udělat načtení sloupce (podobně).
   
2) Obojí spoj do jedné velké podmínky. Tedy nejdřív se zeptej na řádek i sloupce a pak zkontroluj obě věci najednou.

TODO: Zkusit ještě nějak zapojit kontrolu, jestli je pole volné.

"""



"""
Téma 3: Herní cyklus
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# představte si primitivní hru, kde hráč zadává čísla, hraje se tak dlouho, dokud nezadá číslo 7

vitez = "nikdo"

while vitez == "nikdo": # podmínka: hraje se dokud je vitez nikdo

    tip = int(input("Zadej číslo"))
    if tip == 7:
        vitez = "Hráč 1" # nastavíme proměnnou vitez, aby cyklus dál nepokračoval


# zde cyklus skončil, takže víme, že hra skončila
print("Hra skončila, vyhrál: " + vitez)


# STŘÍDÁNÍ HRÁČŮ
# Představte si tu stejnou hru, ale jsou 2 hráči, co se střídají na tahu.
# Uděláme si proměnnou HRAC, ve které si uložíme, který hráč zrovna hraje a budeme to na konci cyklu měnit,
# čímž zajistíme, že se hráči budou střídat.


vitez = "nikdo"
HRAC = 1 # začíná hráč číslo 1

while vitez == "nikdo": # podmínka: hraje se dokud je vitez nikdo

    tip = int(input("Zadej číslo"))
    if tip == 7:
        vitez = HRAC # vítěz je aktuální hráč (ten, který byl právě na tahu)

    # na konci tahu musíme změnit hráče!!
    if HRAC == 1:
        # pokud byl teď na tahu hráč 1, tak příští cyklus bude hráč 2
        HRAC = 2
    else:
        # pokud nebyl na tahu hráč 1, tak příští cyklus bude
        HRAC = 1

# zde cyklus skončil, takže víme, že hra skončila
print("Hra skončila, vyhrál: " + vitez)

"""
Úkoly 3:

Zkopírujte si kód hry se dvěma hráči nahoře.

1) Místo čísel pro hráče použijte symboly (text) "X" a "O".
   Stačí pouze do proměnné HRAC nedávat čísla, ale tyto symboly.
2) Přidejte tam ještě jednoho hráče, tedy celkem budou 3 a budou se střídat.
   Jaký symbol bude hráč 3 mít je na vás.
   Nápověda: Jediné co stačí udělat je rozšířit podmínku na konci cyklu.
"""



