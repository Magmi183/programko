import pygame  # importuji pygame, abych mohl používat pygame funkce
import random

pygame.init()  # inizializace pygame, musí být na začátku

SIRKA_OKNA = 600
VYSKA_OKNA = 400
velikost_okna = (SIRKA_OKNA, VYSKA_OKNA)

# Vytvoříme okno s danou velikostí
okno = pygame.display.set_mode(velikost_okna)

# Zvolíme si popisek naší hry
pygame.display.set_caption("Prográmko: Arkanoid")

# Stav této proměnné nám bude říkat, zda-li má hra stále pokračovat
hraje_se = True

# Tuto proměnnou později použiju pro nastavení FPS naší hry
hodiny = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)
BROWN = (165, 42, 42)
NAVY = (0, 0, 128)


# nastavím si font a velikost písma, kterou budu chtít používat
font = pygame.font.Font('freesansbold.ttf', 32)

platforma_sirka = 100
platforma_vyska = 20
platforma_barva = BLACK
platforma_x = SIRKA_OKNA/2 - platforma_sirka/2
platforma_y = VYSKA_OKNA - platforma_vyska


koule_velikost = 10
koule_x = 200
koule_y = 200
koule_smer_x = 1
koule_smer_y = 1

cihla_sirka = 30
cihla_vyska = 10

cihly = []
for i in range(int(SIRKA_OKNA/30) - 1):
    for j in range(5):
        cihly.append([i * (cihla_sirka + 1), j * (cihla_vyska + 1)])

# HERNÍ SMYČKA
while hraje_se:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # uživatel zavřel okno, ukončíme hru
            hraje_se = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        platforma_x -= 1
    if pressed[pygame.K_RIGHT]:
        platforma_x += 1

    #  vyplním obrazovku bílou barvou, aby tam nezůstali věci z předchozího cyklu
    okno.fill(WHITE)

    platforma = pygame.Rect(platforma_x, platforma_y, platforma_sirka, platforma_vyska)
    pygame.draw.rect(okno, platforma_barva, platforma)

    koule_y += koule_smer_y
    koule_x += koule_smer_x

    koule = pygame.Rect(koule_x, koule_y, koule_velikost, koule_velikost)
    pygame.draw.rect(okno, BLUE, koule)

    if koule.colliderect(platforma):
        # Zjistíme kde je střed koule a platformy
        stred_koule = koule_x + koule_velikost / 2
        stred_platforma = platforma_x + platforma_sirka / 2

        # Zjistíme, kde do sebe narazili, jestli je míček spis napravo nebo nalevo
        bod_kolize = stred_koule - stred_platforma

        # Spocitame novy směr X, hodnota bude mezi -1 a 1
        koule_smer_x = bod_kolize / (platforma_sirka / 2)

        # Smer Y otočíme a upravíme, aby míček urazil stejnou vzdalenost
        koule_smer_y = -(2 - abs(koule_smer_x))

    if koule_x < 0: koule_smer_x = -koule_smer_x
    if koule_x + koule_velikost > SIRKA_OKNA: koule_smer_x = -koule_smer_x

    if koule_y < 0: koule_smer_y = -koule_smer_y

    nove_cihly = []
    for cihla in cihly:
        cihla_rect = pygame.Rect(cihla[0], cihla[1], cihla_sirka, cihla_vyska)
        if cihla_rect.colliderect(koule):
            koule_smer_y = -koule_smer_y
        else:
            pygame.draw.rect(okno, RED, cihla_rect)
            nove_cihly.append(cihla)
    cihly = nove_cihly

    pygame.display.update()  # tento příkaz updatuje herní okno, měl by vždy být na konci cyklu
    hodiny.tick(60)  # nastaví MAXIMÁLNÍ FPS na 60 (tzn., cyklus se provede max. 60x za sekundu)

pygame.quit() # ukončí pygame
