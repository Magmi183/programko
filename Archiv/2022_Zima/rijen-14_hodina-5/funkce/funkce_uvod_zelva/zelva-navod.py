### PYTHON TURTLE
# Oficiální dokumentace: https://docs.python.org/3/library/turtle.html
# Tento návod obsahuje výčet a vysvětlení základních funkcí python turtle.
# Desítky dalších funkcí najdete v dokumentaci.

# Toto stačí napsat jen jednou na začátku programu. Tím říkáme, že chceme používat Python turtle (želvu).
from turtle import *

# POHYB ŽELVY:
# Pro pohyb želvy dopředu používáme příklad forward a jako parametr (hodnota v závorce, např. forward(10) ) uvedeme počet pixelů, o které se má želva pohnout.
forward(100) # Posuneme želvu dopředu o 100 pixelů.

# OTOČENÍ ŽELVY
# Pro otočení želvy používáme příkazy right a left a jako parametr zadáme úhel, o který se má želva danným směrem pootočit.
right(90) # otočím želvu o 90 stupňů doprava
forward(100) # jako důkaz, že se želva otočila, uděláme dalších 100 "kroků"

# KOLEČKO
# Můžeme udělat třeba i kolečko...
circle(50)

# BARVA, TLOUŠŤKA ...
# Pomocí funkce pen můžeme nastavit různé parametry pera jako je barva, tloušťka a mnoho dalšího (dokumentace!).
pen(pencolor="red", pensize=15) # parametrem 'pencolor' nastavíme barvu, 'pensize' zase tloušťku pera
forward(150)
circle(50)
width(20) # další způsob, jak nastavit tloušťku je pomocí funkce width()
color("blue") # barva se dá také nastavit jednodušším způsobem
forward(150)
circle(50)

# SMAZÁNÍ
# Funkcí clear můžeme smazat obrazovku (začít na novo, ale želva zůstane tam, kde je!)
clear()

# NÁVRAT NA ZAČÁTEK
# Pomocí home se želva začne vracet přímou čarou tam, kde začala
home()

# PSANÍ NA OBRAZOVKU
# Příkazem write můžeme vypsat na obrazovku nějaký text, pomocí parametrů si vybereme font, velikost, styl...
write("Nazdár", True, align="center", font=('Arial', 120, 'normal'))
# Všimněte si, že i při psaní textu se želva hýbe a zanechává za sebou čáru, což často nechceme.
# "ZVEDNUTÍ PERA"
# Příkazem penup "zvedneme pero", to znamená, že želva se sice bude pohybovat, ale nebude za sebou zanechávat čáru.
penup() # zvedneme čáru
home() # vrátíme želvu "domů"
clear() # vyčistíme obrazovku
# Opět něco vypíšeme, tentokrát bez čáry za želvou (máme zvedlé pero). Zkusíme kurzívu.
write("Ahoj", True, align="center", font=('Arial', 70, 'italic'))

# RYCHLOST ŽELVY
# Pokud kreslíme něco velkého, můžeme chtít želvu zrychlit.
speed(10) # funkcí speed nastavíme rychlost, kde 1 je nejpomalejší a 10 nejrychlejší

# TROJÚHELNÍK
# V programu samozřejmě můžu využít i for cykly nebo while cykly.
for i in range(3): # třikrát zopakuju (trojúhelník má tři strany)
    forward(150) # jdu dopředu
    left(120) # otočím se

# Zmenšující se kruhy
# Opakování se může hodit například pokud stavím sněhuláka.

kruhu = 50
velikost_kruhu = 3
while kruhu > 0: # dokud mi zbývají nějaké kruhy na nakreslení
    circle(kruhu*velikost_kruhu)
    kruhu-=1

# RANDOM ÚPRAVY
# Zkuste si upravit program a podívejte se, co to udělá.
# Co když se po nakreslení každého kruhu mírně otočím doleva?
speed(50)
kruhu = 50
velikost_kruhu = 3
while kruhu > 0: # dokud mi zbývají nějaké kruhy na nakreslení
    circle(kruhu*velikost_kruhu)
    kruhu-=1
    left(2)


# MNOHOÚHELNÍK

uhlu = 3
for i in range(6):
    width(uhlu)
    for j in range(uhlu):
        forward(50)
        left(360/uhlu)
    uhlu += 1

# INTERAKTIVNÍ ŽELVA
# V programu můžeme normálně používat input.
uhlu = int(input("Zadej kolikaúhelník chceš: \n"))
for j in range(uhlu):
    forward(50)
    left(360/uhlu)

# HVĚZDA

for i in range(50):
    forward(50)
    right(144)

# ÚKOLY:
# 1. Něco si vymyslete a udělejte to.
# 2. Nakreslete barák.
# 3. Nakreslete moderní umění pomocí cyklů.
# 4. Nakreslete hvězdu.



# Tohle je poslední příkaz v programu. Zajistí, že po vykonání všech příkazů okno nezmizí. Chceme se přece podívat na náš výtvor.
done()
