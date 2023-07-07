# ŘEŠENÍ BLUDIŠTĚ, pouze za pomocí seznamu (bez front, setů, atd.)

def nacti_bludiste(nazev_souboru):
    bludiste = []
    with open(nazev_souboru, encoding="utf-8") as bludiste_soubor:
        for soubor_radek in bludiste_soubor:
            radek = []
            for znak in soubor_radek:
                if znak!='\n':
                    radek.append(znak)

            bludiste.append(radek)

    vyska_bludiste = len(bludiste)
    sirka_bludiste = len(bludiste[0])
    start = ("?", "?")
    cil = ("?", "?")
    for r in range(vyska_bludiste):
        for c in range(sirka_bludiste):
            if bludiste[r][c] == 'S':
                start = (r, c)
            elif bludiste[r][c] == 'E':
                cil = (r, c)
    return bludiste, start, cil

def zobraz_bludiste(bludiste):
    for r in bludiste:
        radek = ""
        for znak in r:
            radek += znak
        print(radek)

def prazdne_pole(bludiste, pole):
    if pole[0] < 0 or pole[0] >= len(bludiste):
        return False
    if pole[1] < 0 or pole[1] >= len(bludiste[0]):
        return False

    return bludiste[pole[0]][pole[1]] in [" ", "E"]



def vyres_bludiste(bludiste, start, cil):
    navstiveno = []
    fronta = []

    predchudce = {}
    fronta.append(start)
    navstiveno.append(start)

    while len(fronta) != 0:
        aktualni = fronta[0]
        if aktualni == cil:
            return True, predchudce
        fronta.pop(0)
        sousedi = [(aktualni[0]-1, aktualni[1]), (aktualni[0], aktualni[1]-1),
                   (aktualni[0]+1, aktualni[1]), (aktualni[0], aktualni[1]+1)]
        for soused in sousedi:
            if navstiveno.count(soused) == 0 and prazdne_pole(bludiste, soused):
                fronta.append(soused)
                navstiveno.append(soused)
                predchudce[soused] = aktualni

    return False, {}



def nakresli_cestu(bludiste, predchudci, cil):
    aktualni = cil
    while aktualni in predchudci:
        predchudce = predchudci[aktualni]
        bludiste[predchudce[0]][predchudce[1]] = 'o'
        aktualni = predchudce

    return bludiste


bludiste, start, cil = nacti_bludiste("bludiste_1.txt")
print("BLUDIŠTĚ NAČTENO: ")
zobraz_bludiste(bludiste)
nalezeno, predchudci = vyres_bludiste(bludiste, start, cil)

if nalezeno:
    print("CESTA NALEZENA: ")
    bludiste = nakresli_cestu(bludiste, predchudci, cil)
    zobraz_bludiste(bludiste)
else:
    print("Cesta ze startu do cíle neexistuje.")
