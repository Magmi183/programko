"""
                                    ███████████████████████████████████████████████
                                    █─▄▄▄▄█▄─▄█▄─▄─▀█▄─▄▄─█▄─▀█▄─▄█▄─▄█─▄▄▄─█▄─▄▄─█
                                    █▄▄▄▄─██─███─▄─▀██─▄█▀██─█▄▀─███─██─███▀██─▄█▀█
                                    ▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
"""




"""
HRA - Šibenice:
Úkolem je naprogramovat hru Šibenice.
V programu je slovo, které se uživatel snaží uhodnout. Na začátku vidí místo písmen ve slově
jen samé hvězdičky. Hráč začíná s 10 životy.
Každé kolo hráč buď: 1) tipne písmeno
                     2) tipne celou hádanku
V případě, že tipne celou hádanku - hra končí. V případě, že tipne jedno písmeno se odkryjí
všechny hvězdičky, na jejichž pozici se písmeno nachází. Pokud se písmeno ve slově nenachází vůbec, tak
hráč ztrácí život.

Začněte základní verzí hry a postupně ji vylepšujte. Slovo, které bude uživatel hádat si pro začátek vymyslete.

DOPORUČENÍ: - Ze začátku si vymyslete tajenku, která bude používat buď jen malá, nebo jen velká písmena.
            - Nepoužívejte háčky a čárky.
"""
###############################################š
#  CO SE MŮŽE HODIT:
# v Pythonu se nedá přímo změnit písmeno ve stringu, musí se to trochu obejít
# dá se totiž měnit položka v seznamu -> převedem si string na seznam, změníme co chceme a převedeme zpět
slovo = "Mich*l"
print(slovo)
slovo = list(slovo)  # vytvoří ze stringu seznam
print(slovo)
slovo[4] = 'a'  # změníme políčko v seznamu
slovo = "".join(slovo)  # vezme prvky v seznamu a spojí je za sebe (a máme opět string)
print(slovo)  # a mám, co jsem chtěl

# další věc je operátor in, ten nám řekne, jestli se něco vyskytuje ve stringu, listu, atd.
if "a" in "Michal":
    print("Slovo Michal obsahuje písmeno a.")
if "a" not in ["a", "c", "traktor"]:
    print("Seznam neobsahuje písmeno a.")


# Příkazy BREAK a CONTINUE!

##################################################
# ZAČÁTEK KÓDU - PRO INSPIRACI
# # - # - # - #
tajenka = "Zaciname s programovanim" # Zvolím si nějakou tajenku.
uhodnuto = "******** * *************" # Tajenku si zahvězdičkuju. (BONUS: Udělejte to programátorsky)

zivotu = 7

spatne = []
dobre = []

# ... A SEM PŘIJDE VÁŠ KÓD (ZBYTEK HRY...)
