plocha = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

symbol = "X" # hráč 1 bude mít symbol x (budeme jej měnit vždy na konci kola)

vitez = 0 # před tím, než začne hra, nastavíme vitez na nula, zatím nikdo nevyhrál
while vitez == 0:
    # Vypsání herní plochy (aktuální stav hry)
    print("   1 2 3")  # čísla sloupců
    for cislo_radku in range(3):  # projdu každý řádek
        radek = str(cislo_radku + 1) + " |"  # přidám číslo řádku a stěnu
        for cislo_sloupce in range(3):  # projdu každý sloupec
            radek += plocha[cislo_radku][
                         cislo_sloupce] + "|"  # přidám do řádku aktuální políčko (kombinace řádku a sloupce)
        print(radek)  # řádek který jsem si sestavil vypíšu, vnější cyklus bude pokračovat dalším řádkem

    print("Na tahu je hráč: " + symbol)
    radek = int(input("Zadej řádek: ")) - 1
    sloupec = int(input("Zadej sloupec: ")) - 1

    while radek not in [0, 1, 2] or sloupec not in [0, 1, 2] or plocha[radek][sloupec] != " ":
        print("Zadal jsi neplatné pole! Zkus to znovu.")
        radek = int(input("Zadej řádek: ")) - 1
        sloupec = int(input("Zadej sloupec: ")) - 1

    plocha[radek][sloupec] = symbol

    # Kontrola řádků
    if plocha[0][0] != ' ' and plocha[0][0] == plocha[0][1] and plocha[0][0] == plocha[0][2]:
        vitez = symbol
    elif plocha[1][0] != ' ' and plocha[1][0] == plocha[1][1] and plocha[1][0] == plocha[1][2]:
        vitez = symbol
    elif plocha[2][0] != ' ' and plocha[2][0] == plocha[2][1] and plocha[2][0] == plocha[2][2]:
        vitez = symbol

    # Kontrola sloupců
    elif plocha[0][0] != ' ' and plocha[0][0] == plocha[1][0] and plocha[0][0] == plocha[2][0]:
        vitez = symbol
    elif plocha[0][1] != ' ' and plocha[0][1] == plocha[1][1] and plocha[0][1] == plocha[2][1]:
        vitez = symbol
    elif plocha[0][2] != ' ' and plocha[0][2] == plocha[1][2] and plocha[0][2] == plocha[2][2]:
        vitez = symbol

    # Kontrola diagonál
    elif plocha[0][0] != ' ' and plocha[0][0] == plocha[1][1] and plocha[0][0] == plocha[2][2]:
        vitez = symbol
    elif plocha[0][2] != ' ' and plocha[0][2] == plocha[1][1] and plocha[0][2] == plocha[2][0]:
        vitez = symbol

    if vitez == 0 and " " not in plocha[0] and " " not in plocha[1] and " " not in plocha[2]:
        vitez = -1

    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"

if vitez != 0:
    print("Vyhrál hráč: " + vitez + "!")
else:
    print("Nastala remíza!")