# Hezké vysvětlení for cyklu je zde: https://www.umimeprogramovat.cz/programovani-cyklus-for

"""
For cyklus podobně jako while cyklus slouží k tomu, když chceme vykonat nějaký blok kódu vícekrát.
Narozdíl od while cyklu, který se opakuje dokud je splněná podmínka, for cyklus se provede tolikrát, kolik
např. prvků má seznam/string na které for cyklus voláme, nebo počet opakování přímo určíme metodou range.
"""

# RANGE
# tato metoda se hojně používá spolu s for cyklem
# pokud jí dáte jeden parametr (číslo), generuje hodnoty od 0 až do toho čísla
# pokud dostane dva parametry, generuje čísla v rozmezí
# případný třetí parametr udává step, tedy o kolik se hodnota zvětší po každém cyklu

# proměnná i postupně nabývá hodnot 0 - 9, cyklus se tedy provede 10x
for i in range(10):
    print(i)

# proměnná i postupně nabývá hodnot 1 - 10, cyklus se tedy provede 10x
for i in range(1,11):
    print(i)

# proměnná i nabývá sudých hodnot od 2 do 99
for i in range(2,100,2):
    print(i)

# proměnná i postupně nabývá hodnot písmenek v Hello World! tak jak jdou popořadě
for i in "Hello World!":
    print(i)

"""    
Zkrátka for cyklu dáme něco, co může rozdělit na kousky, cyklus se pak provede tolikrát, kolik je
těch kousků a řídící proměnná (nahoře v příkladech "i") postupně nabývá hodnot těch "kousků". Např.
u řetězce jsou to písmena, u range jsou to čísla z rozsahu, u listu jsou to jeho prvky atd.
"""

jmena = ["Michal", "Kamil", "Jarek", "Dominik", "Jirka", "Sultán"]

for jmeno in jmena:
    # proměnná jmeno postupně nabývá všech hodnot (jmen) ze seznamu jmena
    # v každé iteraci vypíšu pozdrav - nakonec budou všichni pozdraveni
    print("Ahoj, " + jmeno)


"""
Úloha 1:
Máte 2 seznamy - seznam lidí a seznam známek.
1. člověk v seznamu lidí dostal 1. známku ze seznamu známek.
2. člověk 2. známku atd.
Vaším úkolem je vytvořit program, který se opakovaně ptá na jméno a následně řekne, jakou má ten člověk známku,
případně že ho nezná.
např:
znamky = [4, 5, 1, 2]
jmena = ["Kamil", "Michal", "Jarek", "Anezka"]
"""

"""
Úloha 2 - Šibenice:
Úkolem je naprogramovat hru Šibenice.
V programu je slovo, které se uživatel snaží uhodnout. Na začátku vidí místo písmen ve slově
jen samé hvězdičky. Hráč začíná s 10 životy.
Každé kolo hráč buď: 1) tipne písmeno
                     2) tipne celou hádanku
V případě, že tipne celou hádanku - hra končí. V případě, že tipne jedno písmeno se odkryjí
všechny hvězdičky, na jejichž pozici se písmeno nachází. Pokud se písmeno ve slově nenachází vůbec, tak
hráč ztrácí život.
"""
#  CO SE MŮŽE HODIT:

# v Pythonu se nedá přímo změnit písmeno ve stringu, musí se to trochu obejít
# dá se totiž měnit položka v seznamu -> převedem si string na seznam, změníme co chceme a převedeme zpět
slovo = "Mich*l"
print(slovo)
slovo = list(slovo) # vytvoří ze stringu seznam
print(slovo)
slovo[4] = 'a' # změníme políčko v seznamu
slovo = "".join(slovo) # vezme prvky v seznamu a spojí je za sebe (a máme opět string)
print(slovo) # a mám, co jsem chtěl

# další věc je operátor in, ten nám řekne, jestli se něco vyskytuje ve stringu, listu, atd.
if "a" in "Michal":
    print("Slovo Michal obsahuje písmeno a.")
if "a" not in ["a","c","traktor"]:
    print("Seznam neobsahuje písmeno a.")
