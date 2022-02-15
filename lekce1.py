"""
Vytisknutí nějakého slova, třeba jména - použijeme příkaz print a do závorek napíšeme,
co chceme vytisknout, ale pozor, pokud je to obyčejný text tak musí být v uvozovkách! "" nebo ''
"""

print("Michal")
print("Jak se máš?")

# !! Vyzkoušejte si příkaz print.

# Můžeme tisknout více věcí najednou - oddělíme je tečkou, python je pak po pořadě vypíše

print("Ahoj, ", "jak se máš?")

# !! Zkuste vytisknout více věci pomocí oddělení čárkama.

# Jedna z možností, jak udělat nový řádek, je vytisknout prázdný řetězec - prostě nic. Příkaz print vždy automaticky udělá nový řádek.

print("")


# Další možnost jak udělat nový řádek, např. u dlouhého textu, je použití trojitých uvozovek

print("""Python je moderní programovací jazyk. Je univerzální – pohání weby i rakety.
Dobře se čte a dá se velice rychle naučit. Je skvělý pro výuku programování.
Česká komunita je aktivní. Najdeš v ní pomoc, kamarády i práci.""")
print("")
# Nebo je tu ještě jeden způsob, takový více "programátorský" - použijeme znak pro nový řádek! Zpětné lomeno + n. (\n)
# Tenhle příkaz udělá to stejné, jak ten nahoře:

print("Python je moderní programovací jazyk. Je univerzální – pohání weby i rakety.\nDobře se čte a dá se velice rychle naučit. Je skvělý pro výuku programování.\nČeská komunita je aktivní. Najdeš v ní pomoc, kamarády i práci.")

# !! Najděte si nějaký delší text a vytiskněte ho na více řádků alespoň dvěma způsoby.
# můžete použít asciiflow.com

print("""                                   x
                  x               xx             x
                  xx              x             x
                    x            x           x x
                      x
                                x           x
                        x      x          x
                          x             x
                           x  x        x
                          xxxxx      xx
                      xxxx  xxxxx xxxxxx x
                      xx    x             xx x
                   xxx                        xxxxxxx
                  x                                  xxx
    xxx          x     xxxxx                     xxxxx xxxx               xxxx
  xx  xx       x    xxxxxxxx                  xxxxxxx xx   xx          xxxx   xx
 x     xx    x      xxxxxxxx                  x xxxxxxxx      xx       x       xx
xx      x             xxxxxx                  xxxxxxxxx          x     x        x
x        x x                       xxx         xxx  xx             x   x        x
x        x                      xxx               xx                xx x        x
x       x                       xxxxxxx                              xxx        x
x      x                                                              xx        x
x      x                                                               x        x
x     xx         xxxxxx xxxx xxxxxxxxxxx   xx     xxxxxxxxxx           x        x
x     x          xxxxxxx      xx       xxxx  xxxxx    x     x          x        x
x     x            xxxx       xx        x       x     x     x          x       x
x     x            xxxx       xx        x       x     x     x          x       x
x   xx x             xxx      xx        x       x     x     x          xx      x
xx xx  x             xxx      xx       x        x     x     x         xxxx     x
 xxx    xx             xx     xx       x        xx    x     x         x  x     x
          xx            x     x        x         x    x     x         x   x    x
            xxx          x    x        x         x    x    xx        x    xxxxx
               xx        xxx  x x      x x       x    x  xx         xx
                 x         xx xx       xx        x      x          xx
                  x          xxx       x         x  xxxx          x
                    xx         xxxxxxx          xxxx             xx
                      x x             xxxxxxxxx                 xx
                         x xxx                                 x
                              xx xxx xxxxxxx x         xxxxxxxx
                                       x      xx xxxx x
                                      xx
                                      x
                                xxxxxxxxxxxxxxxx
                                     x
                                     x
                                    xxx
                                    x xx
                                  xx   xxx
                                  x      xxx
                                 x""")

# KOMENTÁŘE

# TOTO JE JEDNOŘÁDKOVÝ KOMENTÁŘ
print("Toto se vypíše")  # print("Toto už ne.")

"""
Víceřádkový komentář.
Víceřádkový komentář.
Víceřádkový komentář.
"""

# INPUT
# Tak jo, vytisknout něco, zobrazit to uživateli už umíme - teď bychom s ním chtěli interagovat, tedy - aby nám něco mohl říct i on.
# Třeba odpovědět na otázku. K tomu slouží příkaz input()
# Při použití příkazu input() se program ZASTAVÍ A ČEKÁ, až uživatel něco napíše.

# Obyčejný input - čekáme, až uživatel něco napíše, ale pak jdeme dál a nic s tím neděláme
input()

# Můžeme to třeba hned vytisknout - nejdříve se čeká na input, pak když uživatel něco zadá, tak se to vytiskne

print(input())

# Tím, že napíšeme text do závorek inputu (předáme mu parametr), se uživateli zobrazí text, např. otázka.

input("Kolik je ti let?")

# Výsledek si můžeme také uložit do proměnné - to budeme chtít většinou dělat. Jinak totiž hned zapomeneme, co nám uživatel řekl.

uzivateluv_vek = input("Kolik je ti let?")
print("Je ti ",uzivateluv_vek, " let.")
# Co když chceme dát uživateli možnost, aby svou odpověď mohl psát na nový řádek? Použiji znak pro nový řádek.

uzivateluv_vek = input("Kolik je ti let?\n")
print("Je ti ",uzivateluv_vek, " let.")


"""
Úloha 1 - Pozdrav:

Zeptej se uživatele na jméno a potom ho jménem pozdrav.


"""

jmeno = input("Jak se jmenuješ?\n")

print("Ahoj ", jmeno, ".")

"""
Úloha 2 - KVÍZ:
Zobrazte uživateli kvíz - otázku a třeba 4 možnosti odpovědí
Načtěte jeho odpověď do proměnné a vytiskněte ji. Nebo nepoužívejte proměnnou a odpověď rovnou vytiskněte.
Zatím není úkolem vyhodnotit správnost odpovědi.
"""

print("Jaká je nejvyšší hora světa?")
print("")
print("a) Smrk")
print("b) Sněžka")
print("c) Mariánský příkop")
print("d) Mt. Everest")

odpoved = input()
print(odpoved)

# alternativne:
print(input())