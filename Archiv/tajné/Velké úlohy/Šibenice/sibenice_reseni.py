tajenka = "Zaciname s programovanim" # Zvolím si nějakou tajenku.
uhodnuto = "******** * *************" # Tajenku si zahvězdičkuju. (BONUS: Udělejte to programátorsky)

zivotu = 7

spatne = [] # udělám si seznam, kam si budu ukládat písmena, co uživatel uhodl
dobre = [] # seznam, kam si budu ukládat písmena, co uživatel tipl špatně

while uhodnuto != tajenka and zivotu >= 0: # dokud to uživatel neuhol a má životy, tak se hraje dál

    # na začátku každého "kola" řeknu uživateli stav hry
    print(f"Zbývá ti {zivotu} životů. Dobře jsi uhodl písmena {dobre}, špatně písmena {spatne}. \n"
          f"Aktuální stav tajenky je: {uhodnuto}. ")
    tip = input("Hádej písmeno! \n")
    # následně zkontroluji, že uživatel zadal validní vstup, pokud ne, zeptám se znovu
    ok_vstup = False
    while not ok_vstup:
        if tip in dobre or tip in spatne: # písmeno už hádal
            tip = input("Tohle písmeno už jsi hádal, zkus to znovu: \n")
        elif not tip.replace(" ", "").isalpha(): # vstup obsahuje znaky co nejsou v abecedě
            tip = input("Neplatný vstup: \n")
        else:
            ok_vstup = True

    tip = tip.lower()

    if len(tip) > 1 and tip == tajenka.lower(): # uživatel tipl rovnou celou tajenku
        uhodnuto = tajenka
        break # vyskočím z cyklu, nechci pokračovat dál, kolo a hra skončila
    elif len(tip) > 1:
        # uživatel tipl více znaků, ale neuhodl tajenku
        print("Bohužel, to se nepovedlo, do tajenky ses netrefil.")
        zivotu -= 1
        continue # v tomto "kole" dále nepokračuji, jedu cyklus zase od začátku

    if tip in tajenka.lower():
        print("Hezky! Tohle písmeno jsi tipl správně.") # uživatel správně tipl písmeno
        for index in range(len(tajenka)):
            if tajenka[index].lower() == tip: # najdu pozici písmene
                # přepíšu hvězdičku na správné písmeno, proces je složitější - musím převést string na seznam,
                # udělat změnu a pak zase na string
                uhodnuto = list(uhodnuto)
                uhodnuto[index] = tajenka[index]
                uhodnuto = "".join(uhodnuto)
        dobre.append(tip) # přidám správně uhodnuté písmeno do seznamu
    else:
        print("Bohužel... Máš o jeden život méně.")
        spatne.append(tip)
        zivotu -= 1

# cyklus skončil - teď musím zjistit proč - vyhrál uživatel, nebo mu došly životy?
if zivotu <= 0:
    print("Prohrál jsi...")
    print("Tajenka byla: " + tajenka)
else:
    print("Vyhrál si! Gratuluji.")