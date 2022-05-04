# vymyslím si nějakou tajenku
tajenka = "programovani v pythonu"

# udělám si proměnnou, kde budu mít uloženo to, co uživatel zatím uhodl
# místo písmen dám hvězdičky (BONUSOVÝ ÚKOL: vytvoř zahvězdičkované slovo programátorsky)
uhodnuto = "************ * *******"
zivotu = 10

# seznamy, kam si budu ukládat špatné/dobré tipy
seznam_spatne = []
seznam_dobre = []

# počítadlo kol
kolo = 1


# herní cyklus: hraju, dokud uživateli zbývají životy a dokud neuhodl tajenku
# když nemá životy nebo má uhodnuto, můžu herní cyklus skončit
while zivotu > 0 and uhodnuto != tajenka:

    # Na začátku každého kola na začátku vytisknu informace o stavu hry.

    print("------------------------------------------")
    print("Kolo: " + str(kolo))
    print(uhodnuto)
    print("Zbyva ti " + str(zivotu) + " zivotu.")
    print("Zatim si uhodl si pismena " + str(seznam_dobre) + ".")
    print("Spatne sis tipl " + str(seznam_spatne) + ".")

    # Načtu tip od uživatele.

    tip = input("Tipni si pismeno:\n")

    # První možnost je, že uživatel zadal víc, než jedno písmeno - to bereme, jako že se snaží uhodnout tajenku
    if len(tip) > 1:

        # porovnáme tedy tajenku s tipem uživatele
        if tajenka == tip:
            # pokud uhodl správně, nastavíme uhodnuto (uživatelův progress) na tajenku
            # - prostě už uhodl a nemá dál co hádat
            uhodnuto = tip
        else:
            # pokud tip není tajenka, odečteme život a jdeme dál
            print("Tipl sis spatne.")
            zivotu -= 1

    else:
        # sem se dostaneme, pokud si uživatel tipl jedno písmeno (input je délky jedna nebo menší)

        ok_tip = False

        # udělám for cyklus přes všechny indexy písmen v tajence - proměnná i bude postupně
        # nabývat hodnot 0 až (délka tajenky - 1)
        for i in range(len(tajenka)):
            # pokud je pímeno na i-té pozici v tajence stejné jako uživatelův tip, tak...
            if tajenka[i] == tip:
                ok_tip = True
                # ... změním hvězdičku na i-té pozici svého "uhodnuto" stringu na tip (to co uživatel uhodl)
                uhodnuto_list = list(uhodnuto)
                uhodnuto_list[i] = tip
                uhodnuto = "".join(uhodnuto_list)

        if ok_tip:
            # pokud si uživatel tipl správně, přidám to písmeno do seznamu správných tipů
            seznam_dobre.append(tip)
            print("TIP JE OK, PÍSMENO SE V TAJENCE NACHÁZÍ.")
        else:
            # pokud tipl špatně, přídám ho do seznamu špatných tipů a odečtu jeden život
            seznam_spatne.append(tip)
            print("BOHUŽEL, ŠPATNÉ PÍSMENO... PŘICHÁZÍŠ O ŽIVOT.")
            zivotu-=1

    # na konci cyklu přičtu počítadlo kol
    kolo+=1


# vyhodnotím hru - hráč buď přišel o všechny životy a prohrál, nebo nějaké má a tím pádem
# tajenku uhodl, to vím - jinak by herní cyklus neskončil
if zivotu < 1:
    print("Prohrál jsi.")
else:
    print("Gratuluji, uhodl jsi.")
    print("Tajenka byla " + tajenka)