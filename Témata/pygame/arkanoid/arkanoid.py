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

BLACK = (0, 0, 0)  # kód barvy v RGB
WHITE = (255, 255, 255)  # kód barvy v RGB
GREEN = (0, 255, 0)  # kód barvy v RGB
RED = (255, 0, 0)  # kód barvy v RGB

# nastavím si font a velikost písma, kterou budu chtít používat
font = pygame.font.Font('freesansbold.ttf', 32)


class Platforma:

    def __init__(self, sirka=100, vyska=20, color = BLACK):
        self.sirka = sirka
        self.vyska = vyska
        self.color = color
        self.x = SIRKA_OKNA/2 - sirka/2
        self.y = VYSKA_OKNA - vyska


    def vykresli(self, okno):
        rect = pygame.Rect(self.x, self.y, self.sirka, self.vyska)
        pygame.draw.rect(okno, self.color, rect)



platforma = Platforma()

# HERNÍ SMYČKA
while hraje_se:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # uživatel zavřel okno, ukončíme hru
            hraje_se = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        platforma.x -= 1
    if pressed[pygame.K_RIGHT]:
        platforma.x += 1

    #  vyplním obrazovku bílou barvou, aby tam nezůstali věci z předchozího cyklu
    okno.fill(WHITE)

    platforma.vykresli(okno)


    pygame.display.flip()
    # nastavím, že jeden cyklus bude trvat 1/60 sekundy, tedy hra bude mít zhruba, nejvýš 60 FPS
    hodiny.tick(60)

pygame.quit() # ukončí pygame
