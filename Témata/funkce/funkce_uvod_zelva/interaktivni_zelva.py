"""
Kromě klasického input() umožňuje želva reagovat na stisknutí kláves i lepším způsobem.

Funguje to tak, že nejdříve vytvoříme nějaké FUNKCE, které pak přiřadíme ke konkrétním tlačítkům.
Např. Uděláme funkci s názvem "DOPREDU" a přiřadáme ji ke klávese "W". To znamená, že když uživatel stiskne "W",
tak se danná funkce zavolá. Tímto způsobem můžeme vytvořit a zaregistrova libovolné množství funkcí.

Níže najdete ukázkový kód, rozdělený do základních částí + vysvětlení,
"""
# ---------------------------------------------------------------------------------------------------------------------
# ---> ČÁST 0: IMPORTY + NASTAVENÍ
#      Nic nového, klasické počáteční nastavení želvy.
from turtle import *

shape("turtle")
# ---------------------------------------------------------------------------------------------------------------------
# ---> ČÁST 1: FUNKCE
#      Zde vytvoříme funkce, které později registrujeme ke konkrétním tlačítkům.
def dopredu():
    forward(10)

def dozadu():
    backward(10)

def doleva():
    left(45)

def doprava():
    right(45)

def vycisti():
    clear()

def zmen_barvu():
    barvy = ['black', 'red', 'blue', 'green', 'yellow', 'purple']
    aktualni_barva = pencolor()
    pristi_barva_pozice = (barvy.index(aktualni_barva) + 1) % len(barvy)
    pencolor(barvy[pristi_barva_pozice])

# ---------------------------------------------------------------------------------------------------------------------
# ---> ČÁST 2: REGISTRACE FUNKCÍ
#      V této části přiřadíme vytvořené funkce ke tlačítkům.
#      To se dělá pomocí funkce "onkeypress", která má dva parametry:
#          1. parametr: název funkce, která se má provést
#             - POZOR: Výjimečně bez závorek! Funkci totiž NECHCEME POUŽÍT HNED, jen říkáme, jak se jmenuje.
#          2. parametr: klávesa, která funkci spustí

# Zaregistrujeme pohybové funkce pro konkrétní ŠIPKY na klávesnici
onkeypress(dopredu, 'Up')
onkeypress(dozadu, 'Down')
onkeypress(doleva, 'Left')
onkeypress(doprava, 'Right')

# Registrace funkce "vycisti" na klávesu "v"
onkeypress(vycisti, 'v')
# Registrace funkce "zmen_barvu" na klávesu "b"
onkeypress(zmen_barvu, 'b')

# ---------------------------------------------------------------------------------------------------------------------
# ---> ČÁST 3: Zapnutí programu
#      Tyto příkazy zajistí, že želva bude kontrolovat stisky kláves.
#      Navíc pomocí nekonečného cyklu zajistí, že program ihned neskončí.

listen()
mainloop()
