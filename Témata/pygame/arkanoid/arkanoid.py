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


    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.sirka, self.vyska)

    def stred(self):
        return self.x + self.sirka / 2


class Koule:

    velikost = 10

    def __init__(self, x, y, smer_x = 1, smer_y = 1):

        self.x = x
        self.y = y
        self.smer_x = smer_x
        self.smer_y = smer_y

    def vykresli(self, okno):
        rect = pygame.Rect(self.x, self.y, Koule.velikost, Koule.velikost)
        pygame.draw.rect(okno, RED, rect)

    def pohni(self):
        self.x += self.smer_x
        self.y += self.smer_y

    def get_rect(self):

        return pygame.Rect(self.x, self.y, Koule.velikost, Koule.velikost)

    def stred(self):
        return self.x + Koule.velikost / 2

class Cihla:

    def __init__(self,x, y, sirka = 50, vyska = 20, zivotu=2, barvy = (ORANGE, YELLOW)):
        self.zivotu = zivotu
        self.barvy = barvy

        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def vykresli(self, okno):
        rect = pygame.Rect(self.x, self.y, self.sirka, self.vyska)
        pygame.draw.rect(okno, self.barvy[-self.zivotu], rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.sirka, self.vyska)


platforma = Platforma()
koule = Koule(200, 200)

cihla_sirka = 60
cihla_vyska = 25
cihly = []
for i in range(int(SIRKA_OKNA/cihla_sirka) - 1):
    for j in range(5):
        cihly.append(Cihla(i * (cihla_sirka + 1), j * (cihla_vyska + 1), cihla_sirka, cihla_vyska))

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

    koule.pohni()
    koule.vykresli(okno)

    if koule.get_rect().colliderect(platforma.get_rect()):
        # Zjistíme, kde do sebe narazili, jestli je míček spis napravo nebo nalevo
        bod_kolize = koule.stred() - platforma.stred()

        # Spocitame novy směr X, hodnota bude mezi -1 a 1
        koule.smer_x = bod_kolize / (platforma.sirka / 2)

        # Smer Y otočíme a upravíme, aby míček urazil stejnou vzdalenost
        koule.smer_y = -(2 - abs(koule.smer_x))

    if koule.x < 0: koule.smer_x = -koule.smer_x
    if koule.x + Koule.velikost > SIRKA_OKNA: koule.smer_x = -koule.smer_x

    if koule.y < 0: koule.smer_y = -koule.smer_y

    nove_cihly = []
    kolize_zleva = kolize_zprava = kolize_zdola = kolize_zhora = False
    for cihla in cihly:
        kolize = koule.get_rect().colliderect(cihla.get_rect())

        if kolize:
            # Získání rohů cihly
            leva_strana_cihly = cihla.x
            prava_strana_cihly = cihla.x + cihla.sirka
            horni_strana_cihly = cihla.y
            dolni_strana_cihly = cihla.y + cihla.vyska

            # Detekce směru kolize
            kolize_zdola = koule.y - koule.smer_y >= dolni_strana_cihly
            kolize_zhora = koule.y + koule.velikost - koule.smer_y <= horni_strana_cihly
            kolize_zprava = koule.x + koule.velikost - koule.smer_x >= prava_strana_cihly
            kolize_zleva = koule.x - koule.smer_x <= leva_strana_cihly

        else:
            cihla.vykresli(okno)
            nove_cihly.append(cihla)

    if kolize_zleva or kolize_zprava:
        koule.smer_x = -koule.smer_x
    if kolize_zhora or kolize_zdola:
        koule.smer_y = -koule.smer_y

    cihly = nove_cihly


    pygame.display.flip()
    # nastavím, že jeden cyklus bude trvat 1/60 sekundy, tedy hra bude mít zhruba, nejvýš 60 FPS
    hodiny.tick(60)

pygame.quit() # ukončí pygame
