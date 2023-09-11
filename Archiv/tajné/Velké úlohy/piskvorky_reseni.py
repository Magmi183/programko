# TO-DO: Tak piskvorky budou asi tezsi nez jsem si myslel, bude tezky udelat nejak hezky ohodnoceni, jestli nekdo uz

""" PREREKVIZITY:
2d pole, udelat, vytisknout
"""
import pprint


print("****** PIŠKVORKY ******")
print()

velikost_plochy = 9
plocha = [['-'] * velikost_plochy for _ in range(velikost_plochy)]
cisla = [str(x+1) for x in range(velikost_plochy)]

hrac = 1
vitez = 0
while vitez == 0:
    print("Na tahu je hráč " + str(hrac) + ".")

    print("  " + " ".join(cisla))
    cislo_radku = 1
    for radek in plocha:
        print(str(cislo_radku) + " " + " ".join(radek))
        cislo_radku += 1

    radek = sloupec = -1
    while radek < 0 or sloupec < 0 or radek>=velikost_plochy or sloupec>=velikost_plochy or plocha[radek][sloupec]!='-':
        print("Zadej řádek a sloupec:")
        radek, sloupec = input().split()
        radek = int(radek) - 1
        sloupec = int(sloupec) - 1

    if hrac == 1:
        plocha[radek][sloupec] = 'O'
    else:
        plocha[radek][sloupec] = 'X'

    if hrac == 1:
        hrac = 2
    else:
        hrac = 1


