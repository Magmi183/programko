# PyGame tahák

Tento tahák nepředpokládá znalost objektového programování, proto jsou některé části ochuzené o hlubší vysvětlení.

## Přidání čtverce/obdélníku

Čtverec/obdélník je nejjednodušší předmět, který do pygame můžeme přidat. O složitější objekty se začněte zajímat až ve chvíli, kdy perfektně ovládáte vytváření, vykreslování a kolizi obdélníků.

**Příklad:** Chceme udělat herní objekt — _jídlo_ —, které bude mít tvar čtverce. Následující kroky vysvětlují postup.

### 1) Pozice, barva, velikost

Nejprve je potřeba si určit tyto **3 základní vlastnosti**.
Nejlépe **si udělat proměnné pro každou z nich.**
Ano, pozice se může měnit, a to klidně i velikost a barva, což není problém, ale potřebujeme si udělat proměnné, kde budeme uchovávat aktuální hodnoty.
Ty můžeme změnit např. po stisku šipek atd.

Barvu či velikost jde často sdílet pro více herních objektů. Např. uděláte si barvu `ZELENA`,
kterou budete používat pro objekt `trava`, `list` i `zaba`, bez nutnosti dělat 3 různé proměnné. 


Tyto proměnné jsou většinou založené **před herním cyklem.**
```python
# POČÁTEČNÍ pozice pro jídlo (v průběhu hry můžem změnit)
pozice_x_jidlo = 200
pozice_y_jidlo = 200

# zelená barva, můžeme použít i pro jiné objekty 
ZELENA = (0, 255, 0)

# Velikost (pokud máme čtverec, stačí jedna proměnná = délka jedné hrany)
velikost_jidlo = 30
```
### 2) Sestavení a vykreslení čtverce/obdélníku

Když máme vlastnosti našeho objektu, stačí jej už pouze vytvořit pomocí `pygame.Rect`, což je něco jako funkce,
která přijímá 4 parametry a vrátí obdélník (**Rect**angle). Parametry jsou:
1. Souřadnice X
2. Souřadnice Y
3. Velikost jedné hrany (A)
4. Velkost druhé hrany (B)


```python
# Vytvoření Rectu
jidlo = pygame.Rect(pozice_x_jidlo, pozice_y_jidlo, velikost_jidlo, velikost_jidlo)
```
Poté, co máme Rect, jej stačí pomocí funkce `pygame.draw.rect` vykreslit do našeho okna.
```python
# 3 parametry - okno, barva a ten Rect
pygame.draw.rect(okno, YELLOW, jidlo)
```

## Kolize dvou čtverců/obdélníků

Často chceme zjistit, jestli do sebe dva obdélníky nenarazily (kolize).
Představme si, že máme dva obdélníky, `postava` a `jidlo`:

```python
# Rect pro postavu
postava = pygame.Rect(pozice_x_postava, pozice_y_postava, velikost_postava, velikost_postava)
# Rect pro jidlo
jidlo = pygame.Rect(pozice_x_jidlo, pozice_y_jidlo, velikost_jidlo, velikost_jidlo)
```

Jestli nastala kolize zjistíme následovně pomocí `colliderect`:

```python
if postava.colliderect(jidlo):
    # kolize nastala
    # zde můžeme zvyšit skóre, vygenerovat novou pozici jídla atd.
```

Šlo by to udělat i obráceně, tedy `jidlo.colliderect(postava)`. Je to něco jako funkce,
která vrací `True`, nebo `False`, podle toho, jestli do sebe danné dva Recty narazily.