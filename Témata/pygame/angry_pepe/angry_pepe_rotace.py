import pygame  # importuji pygame, abych mohl používat pygame funkce
import random
import time

pygame.init()  # inizializace pygame, musí být na začátku

# Zvolíme si velikost herního okna
sirka_okna = 1000
vyska_okna = 500
velikost_okna = (sirka_okna, vyska_okna)

# Vytvoříme okno s danou velikostí
okno = pygame.display.set_mode(velikost_okna)

# Zvolíme si popisek naší hry
pygame.display.set_caption("Minekrat rework")

# Stav této proměnné nám bude říkat, zda-li má hra stále pokračovat
hraje_se = True

# Tuto proměnnou později použiju pro nastavení FPS naší hry
hodiny = pygame.time.Clock()

# Načtu si obrázek hlavní postavy
nastvany_pepe_original = pygame.image.load('obrazky/angry_pepe.jpg')
# Zmenším ho (nastavím si vlastní velikost, protože ten obrázek je velký a zabral by celou obrazovku)
nastvany_pepe_original = pygame.transform.scale(nastvany_pepe_original, (75, 75))
nastvany_pepe = nastvany_pepe_original

strela_obrazek = pygame.image.load('obrazky/kanka.png')
rychlost_strely = 5

# tyto proměnné uchovávají pozici jídla na obrazovce (souřadnicový systém)
pozice_x_jidlo = 200
pozice_y_jidlo = 200
barva_jidla = (0, 128, 255)  # kód barvy v RGB

# podobně si udělám i pozici pro hlavní postavu této hry
pozice_x_pepe = 100
pozice_y_pepe = 100

# udělám si ještě nějaké další barvy, ať je pak můžu snáze používat
BLACK = (0, 0, 0)  # kód barvy v RGB
WHITE = (255, 255, 255)  # kód barvy v RGB
GREEN = (0, 255, 0)  # kód barvy v RGB
RED = (255, 0, 0)  # kód barvy v RGB

skore = 0

strely = []

# Funkce, která mi řekne, jestli jsou dva čtverce/obdélníky v kolizi (přes sebe)
def kolize(rect1, rect2):
    return rect1.colliderect(rect2)


# nastavím si font a velikost písma, kterou budu chtít používat
font = pygame.font.Font('freesansbold.ttf', 32)


# funkce, která v rohu obrazovky zobrazí text - aktuální skóre
def zobraz_skore():
    text = font.render("Skore: " + str(skore), True, GREEN)
    okno.blit(text, (0, 0))

def orotuj_pepeho(nahoru, dolu, doprava, doleva):
    if nahoru and doprava:
        return pygame.transform.rotate(nastvany_pepe_original, 45)
    elif nahoru and doleva:
        return pygame.transform.rotate(nastvany_pepe_original, 135)
    elif dolu and doprava:
        return pygame.transform.rotate(nastvany_pepe_original, -45)
    elif dolu and doleva:
        return pygame.transform.rotate(nastvany_pepe_original, -135)
    elif nahoru:
        return pygame.transform.rotate(nastvany_pepe_original, 90)
    elif doprava:
        return nastvany_pepe_original
    elif doleva:
        return pygame.transform.rotate(nastvany_pepe_original, 180)
    elif dolu:
        return pygame.transform.rotate(nastvany_pepe_original, -90)
    return nastvany_pepe_original

kouka_dolu = kouka_nahoru = kouka_doleva = False
kouka_doprava = True
posledni_strela = 0

def vystrel(posledni_strela):
    if time.time() - posledni_strela < 0.5:
        # nelze vystřelit více než 2x za sekundu (1x za 0.5 sekundy)
        return posledni_strela

    strela_x = pozice_x_pepe
    strela_y = pozice_y_pepe
    smer_x = 0
    if kouka_doprava:
        smer_x = 1
    elif kouka_doleva:
        smer_x = -1
    smer_y = 0
    if kouka_nahoru:
        smer_y = -1
    elif kouka_dolu:
        smer_y = 1
    strela = (strela_x, strela_y, smer_x, smer_y)
    strely.append(strela)
    return time.time()

def aktualizuj_strely(strely):
    aktualizovane_strely = []
    for strela in strely:
        if strela[0] > sirka_okna or strela[0] < 0 or strela[1]<0 or strela[1]>vyska_okna:
            pass
        else:
            strela_x = strela[0] + strela[2] * rychlost_strely
            strela_y = strela[1] + strela[3] * rychlost_strely
            strela = (strela_x, strela_y, strela[2], strela[3])
            aktualizovane_strely.append(strela)
    return aktualizovane_strely

    # tato funkce přijímá seznam pozic a pygame.Image, následně vykreslí danný obrázek
    # na každé z pozic v seznamu


def vykresli_obrazky(seznam_pozic, obrazek):
    for pozice in seznam_pozic:
        okno.blit(obrazek, pozice)


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
    nahoru = dolu = doprava = doleva = False
    # získám SLOVNÍK všech právě držených tlačítek
    # dvojice: tlačítko - bool (ve slovníku je pro každé tlačítko buď True = je stisklé, nebo False = není stisklé)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        # pokud je stisklá klávesa UP, zmenším Y pozici, aby se mi objekt přiblížil k hořejšku okna
        pozice_y_pepe -= 3
        nahoru = True
    if pressed[pygame.K_DOWN]:
        pozice_y_pepe += 3
        dolu = True
    if pressed[pygame.K_LEFT]:
        pozice_x_pepe -= 3
        doleva = True
    if pressed[pygame.K_RIGHT]:
        pozice_x_pepe += 3
        doprava = True
    if pressed[pygame.K_s]:
        posledni_strela = vystrel(posledni_strela)

    if pressed[pygame.K_q]:
        break

    #  vyplním obrazovku bílou barvou, aby tam nezůstali věci z předchozího cyklu
    okno.fill(WHITE)

    # toto je takový hezký tríček, jak zajistit, aby Pepe zůstal v takové rotaci, jako naposledy
    # prostě Pepeho rotujeme jenom tehdy, když uživatel právě tiskne nějakou šipku
    # jinak neděláme nic (a Pepe tedy zůstane takový, jako byl naposledy, když s ním uživatel hýbal)
    if True in [dolu, nahoru, doprava, doleva]:
        nastvany_pepe = orotuj_pepeho(nahoru, dolu, doprava, doleva)
        kouka_dolu, kouka_nahoru, kouka_doleva, kouka_doprava = dolu, nahoru, doleva, doprava

    strely = aktualizuj_strely(strely)
    vykresli_obrazky(strely, strela_obrazek)

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

    # zavolám funkci pro zobrazení skóre (jako poslední věc v cyklu)
    zobraz_skore()

    pygame.display.flip()
    # nastavím, že jeden cyklus bude trvat 1/60 sekundy, tedy hra bude mít zhruba, nejvýš 60 FPS
    hodiny.tick(60)

pygame.quit() # ukončí pygame
