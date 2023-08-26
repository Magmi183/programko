"""
HRA - PIŠKVORKY - Jednoduchá verze (3x3)

Naprogramuj jednoduché piškvorky na hrací ploše o velikosti 3x3, tedy celkem 9 polí.
Hráči se budou střídat. Pozici, na kterou chtějí umístit svůj symbol budou zadávat ve formátu souřadnic, tedy např.:
1 2 -> což znamená, že hráč si přeje umístit svůj symbol (křížek nebo kolečko) do druhého sloupce v prvním řádku.

Hraje se tak dlouho, dokud není znám vítěz, nebo dokud není remíza.

JAK NA TO:
    1) Udělej si "2D pole" (nech si vysvětlit!) znaků, která bude reprezentovat herní plochu.
    2) Vytvoř herní smyčku - hra se bude hrát DOKUD není vítěz/remíza.
    Herní smyčka:
        - zobraz aktuální stav hry (herní plochu)
        - vyzvi hráče, který je právě na tahu, aby zadal kam chce umístit svůj symbol
        - zkontroluj, že uživatel zadal správné hodnoty, pokud ne, ať je zadá znovu
        - umísti symbol na hráčem zvolené místo
        - zkontroluj vítěze/remízu
        - pokud nikdo nevyhrál, změň hráče, který je na tahu a cyklus může jet znova
"""
########### CO SE MŮŽE HODIT: #############
###########################################
# Takto může na začátku vypadat herní plocha, seznam, který obsahuje další 3 seznamy, které obsahují jednotlivá políčka (stringy)
plocha = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

# Takto změním např. políčko vlevo nahoře (nultý řádek, nultý sloupec) na křížek:
plocha[0][0] = "x"

# Vypsání herní plochy (aktuální stav hry)
print("   1 2 3") # čísla sloupců
for cislo_radku in range(3): # projdu každý řádek
    radek = str(cislo_radku + 1) + " |" # přidám číslo řádku a stěnu
    for cislo_sloupce in range(3): # projdu každý sloupec
        radek += plocha[cislo_radku][cislo_sloupce] + "|" # přidám do řádku aktuální políčko (kombinace řádku a sloupce)
    print(radek) # řádek který jsem si sestavil vypíšu, vnější cyklus bude pokračovat dalším řádkem
###########################################

#  ... SEM PIŠTE VÁŠ KÓD ...







"""
HRA - PIŠKVORKY - Těžká verze (NxN)

Cílem je naprogramovat hru piškvorky. Uživatel si na začátku zvolí, jak velkou chce hrací plochu - plocha bude čtvercová,
uživatel tedy zadá jedno číslo, např. pokud zadá 8, tak hrací plocha bude mít 8 řádků a 8 sloupců.

Hru hrají dva hráči, kteří se postupně střídají. Pozici, na kterou chtějí umístit svůj symbol budou zadávat ve formátu souřadnic,
tedy např. 1 2 -> což znamená, že hráč si přeje umístit svůj symbol (křížek nebo kolečko) do druhého sloupce v prvním řádku.

"""
"""
velikost_plochy = int(input("Zadej velikost hrací plochy: "))

plocha = []
for cislo_radku in range(velikost_plochy):
    radek = []
    for cislo_sloupce in range(velikost_plochy):
        radek.append(" ")
    plocha.append(radek)

vitez = 0  # -1 => remíza, 0 => zatím nikdo, 1 => hráč 1 vyhrál, 2 => hráč 2 vyhrál

# herní smyčka, hraje se DOKUD není znám vítěz a není remíza
while vitez == 0:

    # --- ZOBRAZENÍ AKTUÁLNÍHO STAVU HRY

# TODO
"""