import pygame  # importuji pygame, abych mohl používat pygame funkce
import random

pygame.init()  # inizializace pygame, musí být na začátku

# Zvolíme si velikost herního okna
sirka_okna = 1000
vyska_okna = 500
velikost_okna = (sirka_okna, vyska_okna)

# Vytvoříme okno s danou velikostí
okno = pygame.display.set_mode(velikost_okna)

# Zvolíme si popisek naší hry
pygame.display.set_caption("Angry Pepe")

# Stav této proměnné nám bude říkat, zda-li má hra stále pokračovat
hraje_se = True

# Tuto proměnnou později použiju pro nastavení FPS naší hry
hodiny = pygame.time.Clock()

# Načtu si obrázek hlavní postavy
nastvany_pepe = pygame.image.load('obrazky/angry_pepe.jpg')
# Zmenším ho (nastavím si vlastní velikost, protože ten obrázek je velký a zabral by celou obrazovku)
nastvany_pepe = pygame.transform.scale(nastvany_pepe, (75, 75))

# tyto proměnné uchovávají pozici jídla na obrazovce (souřadnicový systém)
pozice_x_jidlo = 200
pozice_y_jidlo = 200
barva_jidla = (0, 128, 255)  # kód barvy v RGB

# podobně si udělám i pozici pro hlavní postavu této hry
pozice_x_pepe = 100
pozice_y_pepe = 100

cihlova_zed = pygame.image.load('obrazky/cihlova_zed.jpg')
zed_rozmer = 50
cihlova_zed = pygame.transform.scale(cihlova_zed, (zed_rozmer, zed_rozmer))

# Tato funkce vygeneruje pozice zdí tak, aby byly po obvodu celé obrazovky.
# Pokud rozměr není dělitelný rozměrem zdi, tak zbyde na krajích trocha prostoru.
def vygeneruj_zdi(sirka_okna, vyska_okna, zed_rozmer):

    # prázdný seznam, do kterého budu postupně vkládat vygenerované pozice
    zdi = []
    # spočítám si, kolik zdí se mi do okna vejde na šířku
    zdi_na_sirku = int(sirka_okna/zed_rozmer)
    # spočítám si, kolik zdí se mi do okna vejde na výšku
    zdi_na_vysku = int(vyska_okna/zed_rozmer)

    # ve for cyklu budu generovat nejdříve zdi nahoře a dole (horizontálně)
    for i in range(zdi_na_sirku):
        # spočítám pozici zdi nahoře (y = 0, x se postupně zvětšuje)
        pozice = (i * zed_rozmer, 0)
        zdi.append(pozice)

        # spočítám pozici zdi dole (y = začátek poslední zdi, x se postupně zvětšuje)
        pozice = (i * zed_rozmer, (zdi_na_vysku -1) * zed_rozmer)
        zdi.append(pozice)

    # obdobně jako při generování horizontálních pozic si spočítám vertikální pozice
    # akorát mám range od 1 do zdi_na_vysku - 1, jelikož první a poslední zeď už mám vygenerovanou,
    # jelikož se jedná o zdi v rozích, které jsou již zahrnuty do "horizontálních" zdí
    for i in range(1, zdi_na_vysku - 1):
        pozice = (0, i * zed_rozmer)
        zdi.append(pozice)

        pozice = ((zdi_na_sirku-1) * zed_rozmer, i * zed_rozmer )
        zdi.append(pozice)

    # vrátím seznam zdí
    return zdi

# pomocí mé funkce si vytvořím seznam zdí
zdi_pozice = vygeneruj_zdi(sirka_okna, vyska_okna, zed_rozmer)

# tato funkce přijímá seznam pozic a pygame.Image, následně vykreslí danný obrázek
# na každé z pozic v seznamu
def vykresli_obrazky(seznam_pozic, obrazek):
    for pozice in seznam_pozic:
        okno.blit(obrazek, pozice)


# udělám si ještě nějaké další barvy, ať je pak můžu snáze používat
BLACK = (0, 0, 0)  # kód barvy v RGB
WHITE = (255, 255, 255)  # kód barvy v RGB
GREEN = (0, 255, 0)  # kód barvy v RGB
RED = (255, 0, 0)  # kód barvy v RGB

skore = 0

# Funkce, která mi řekne, jestli jsou dva čtverce/obdélníky v kolizi (přes sebe)
def kolize(rect1, rect2):
    return rect1.colliderect(rect2)

"""
Tato funkce přijímá rect (objektu, který mě zajímá, jestli do něčeho nenarazil),
seznam pozic (souřadnic) a velikost objektů na danných pozicích - MUSÍ být čtverce.
(TODO: Zmenit, udelat defaultni parametr.).
Následně funkce zkontroluje, zdali rect koliduje s kterýmkoliv objektem ze seznamu.
Vráti True pokud ano, jinak False.
"""
def kolize_s_pozici_ze_seznamu(rect1, seznam_pozic, velikost_objektu):
    for pozice in seznam_pozic:
        rect_objektu = pygame.Rect(pozice[0], pozice[1], velikost_objektu, velikost_objektu)
        if rect1.colliderect(rect_objektu):
            return True
    return False


# nastavím si font a velikost písma, kterou budu chtít používat
font = pygame.font.Font('freesansbold.ttf', 32)


# funkce, která v rohu obrazovky zobrazí text - aktuální skóre
def zobraz_skore():
    text = font.render("Skore: " + str(skore), True, GREEN)
    okno.blit(text, (0, 0))

def zkus_pohyb(x, y, pozice_x_pepe, pozice_y_pepe):
    pepe_rect = nastvany_pepe.get_rect(topleft=(pozice_x_pepe+x, pozice_y_pepe+y))

    if kolize_s_pozici_ze_seznamu(pepe_rect, zdi_pozice, zed_rozmer):
        # kdyby se pepe pohnul o směr (x, y), tak by byl v kolizi s nějakou zdí
        # funkci ukončíme, žádný pohyb se nekoná - z funkce vrátím původní pozici Pepeho (před pohybem)
        return pozice_x_pepe, pozice_y_pepe

    # pohyb nezpůsobí žádnou kolizi, proto jej můžu udělat
    pozice_y_pepe += y
    pozice_x_pepe += x

    # z funkce vrátím aktualizované pozice
    return pozice_x_pepe, pozice_y_pepe


""" 
HERNÍ SMYČKA! Dokud se hraje, tak poběží tento cyklus.
Typicky by tento cyklus měl obsluhovat alespoň tyto základní věci:
    1) Načte vstup od uživatele (stiski kláves, pohyb myší atd.)
    2) Vyhodnotí vstup od uživatele, implementuje herní logiku. Např. když se dva objekty srazí, něco se stane.
       Když uživatel splní level, tak se dostane do dalšího levelu. Když mu dojdou životy, zobrazí skóre atd.
    3) Vykreslí tyto změny na obrazovku.

    ... a takto pořád dokola!
"""
while hraje_se:
    # Na začátku herní smyčky projedu ve for cyklu všechny události, které se stali (stisk tlačítka, zavření okna...)
    # Tímto způsobem ale zachytím jen změnu, např. když uživatel zmáčkl tlačítko, ale když ho bude držet, tak už to nepoznám,
    # poznám pak až zase změnu, že tlačítko držet přestane.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # uživatel zavřel okno, ukončíme hru
            hraje_se = False

    # získám SLOVNÍK všech právě držených tlačítek
    # dvojice: tlačítko - bool (ve slovníku je pro každé tlačítko buď True = je stisklé, nebo False = není stisklé)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        # pokud je stisklá klávesa UP, zmenším Y pozici, aby se mi objekt přiblížil k hořejšku okna
        pozice_x_pepe, pozice_y_pepe = zkus_pohyb(0, -3, pozice_x_pepe, pozice_y_pepe)
    if pressed[pygame.K_DOWN]:
        pozice_x_pepe, pozice_y_pepe = zkus_pohyb(0, 3, pozice_x_pepe, pozice_y_pepe)
    if pressed[pygame.K_LEFT]:
        pozice_x_pepe, pozice_y_pepe = zkus_pohyb(-3, 0, pozice_x_pepe, pozice_y_pepe)
    if pressed[pygame.K_RIGHT]:
        pozice_x_pepe, pozice_y_pepe = zkus_pohyb(3, 0, pozice_x_pepe, pozice_y_pepe)
    if pressed[pygame.K_q]:
        break

    #  vyplním obrazovku bílou barvou, aby tam nezůstali věci z předchozího cyklu
    okno.fill(WHITE)

    # vykreslím zdi, jako jednu z prvních akcí
    vykresli_obrazky(zdi_pozice, cihlova_zed)

    # udělám si čtverec, který bude představovat jídlo - zadám pozici a velikost
    jidlo = pygame.Rect(pozice_x_jidlo, pozice_y_jidlo, 60, 60)

    # takto vykreslím jídlo = draw.rect - nakreslí nějaký čtverec, obdélník
    # zadáme okno, barvu a ten čtverec, který chceme vytvořit
    pygame.draw.rect(okno, barva_jidla, jidlo)

    # vykreslení obrázku - nastvany_pepe na pozici (pozice_x_pepe, pozice_y_pepe)
    okno.blit(nastvany_pepe, (pozice_x_pepe, pozice_y_pepe))

    # zjistím si, jaký "výřez" obrazovky zabírá pepe, abych pomocí toho mohl zjistit kolize
    pepe_rect = nastvany_pepe.get_rect(topleft=(pozice_x_pepe, pozice_y_pepe))

    # pokud je pepe v kolizi s jídlem, znamená to, že ho sní - tedy zvýším skóre a vygeneruji novou pozici jídla
    if kolize(jidlo, pepe_rect):
        skore += 1
        pozice_x_jidlo = random.randrange(550)
        pozice_y_jidlo = random.randrange(350)

    """
    # Kontrola, jestli náhdou pepe nenarazil do nějaké zdi
    if kolize_s_pozici_ze_seznamu(pepe_rect, zdi_pozice, zed_rozmer):
        # pokud narazil, udělím penalizaci a resetuji jeho pozici
        skore -= 1000
        pozice_x_pepe = int(sirka_okna/2)
        pozice_y_pepe = int(vyska_okna/2)
    """

    # zavolám funkci pro zobrazení skóre (jako poslední věc v cyklu)
    zobraz_skore()

    pygame.display.update()  # tento příkaz updatuje herní okno, měl by vždy být na konci cyklu
    hodiny.tick(60)  # nastaví MAXIMÁLNÍ FPS na 60 (tzn., cyklus se provede max. 60x za sekundu)

pygame.quit() # ukončí pygame
