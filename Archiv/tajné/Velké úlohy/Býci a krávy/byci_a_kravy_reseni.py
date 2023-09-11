import random
# TO-DO: Vyhodnoceni hry
cislo = 0
cislo_ok = False
while not cislo_ok:
    cislo = str(random.randrange(1000,10000))
    cislo_ok = True
    for i in range(10):
        if cislo.count(str(i)) > 1:
            cislo_ok = False
print(cislo)
pokusu = 8
print("Vítej ve známé hře Býci a Krávy. Myslím si číslo.")
while pokusu > 0:
    tip = input("Zadej svůj tip.\n")
    if len(tip) != len(cislo):
        tip = input("Zadej validní tip.\n")
    byci = 0
    kravy = 0
    for i in range(len(cislo)):
        if tip[i] == cislo[i]:
            byci += 1
        elif tip[i] in cislo:
            kravy += 1
    pokusu -= 1
    print(f"Býci: {byci}, krávy: {kravy}. Zbývá ti {pokusu} pokusů.")