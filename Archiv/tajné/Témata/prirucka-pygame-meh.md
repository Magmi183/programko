# TATO STRÁNKA JE VE VÝSTAVBĚ
# PyGame tahák


## Přidání nového herního objektu

Pokud chcete do hry přidat nějaký objekt, je nutné se nejdříve zamyslet nad tím, jaké bude mít vlastnosti.
Každý herní objekt má obvykle minimálně tyto vlastnosti: pozici (kde se zrovna nachází) a tvar (jak ten objekt vypadá).
Tyto vlastnosti si potřebujeme někam uložit, prvním krokem tedy může být vytvoření patřičných proměnných.

Pokud bychom například chtěli založit herní objekt jídlo, začneme vytvořením proměnných pro pozici jídla. Hodnotu těchto proměnných pak budu používat, když to jídlo budu chtít zobrazit na obrazovce (abych věděl, kde na obrazovce ho mám zobrazit).
Pokud máme 2D hru, může to vypadat například takto:
```python
jidlo_pozice_x = 100
jidlo_pozice_y = 100
```

### Vykreslení herního objektu

#### Objekt jako geometrický útvar

Pokud chceme objekt vykreslit jako některý ze základních geometrických útvarů, použijeme k tomu patřičnou funkci z modulu ``pygame.draw``.
```python
# objekty budu kreslit do tohoto okna, 
okno = pygame.display.set_mode(velikost_okna)
# barva, kterou budu používat ke kreslení objektů (zelená)
barva = (0, 255, 0)

# KRUH # o # o # o # o # o # o #
# vykreslení kruhu se středem v bodě (x, y)
pygame.draw.circle(okno, barva, (x, y), polomer)

# OBDÉLNÍK/ČTVEREC # ▭ # ▭ # ▭ # ▭ # ▭ # ▭ #
# vykreslení obdélníku/čtverce
# udělám si obdélník, který budu vykreslovat - zadám levý horní roh obdélníku a jak je vysoký a široký
pozice_a_velikost = pygame.Rect(pozice_x_jidlo, pozice_y_jidlo, 60, 60)
# teď už jen stačí zavolat tuto funkci a dát jí okno, barvu a ten obdélník, co jsme si zadefinovali
pygame.draw.rect(okno, barva, pozice_a_velikost)

# ČÁRA # - # - # - # - # - # - #
# vykreslení čáry (úsečka)
cara_zacatek = (50, 50) # souřadnice začátku čáry
cara_konec = (100, 50) # souřadnice konce čáry
pygame.draw.line(okno, barva, cara_zacatek, cara_konec)

# ... a existují i další tvary, jejichž seznam lze najít zde https://www.pygame.org/docs/ref/draw.html

```

## Kolize herních objektů




### Dobré zdroje

Velmi hezký tutorial na PyGame je zde: https://www.itnetwork.cz/python/pygame/pygame-uvod--instalace.
Tutorial je česky a látku pokrývá opravdu detailně.

