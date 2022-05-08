"""
HRA - Šibenice:
# TODO dát se aktuální zadání
"""
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

# ZAČÁTEK KÓDU - PRO INSPIRACI
# # - # - # - #
# vymyslím si nějakou tajenku

# TODO: Dát sem začátek OG řešení

# ... A SEM PŘIJDE VÁŠ KÓD (ZBYTEK HRY...)