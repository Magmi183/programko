# ZDROJ: https://www.edureka.co/blog/snake-game-with-pygame/
# (přeloženo do češtiny by: Michal Janeček)

import pygame
import time
import random

pygame.init()

bile = (255, 255, 255)
zluta = (255, 255, 102)
cerna = (0, 0, 0)
cervena = (213, 50, 80)
zelena = (0, 255, 0)
modra = (50, 153, 213)

okno_sirka = 600
okno_vyska = 400

okno = pygame.display.set_mode((okno_sirka, okno_vyska))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
FPS = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def zobraz_skore(score):
    value = score_font.render("Tvoje skóre je: " + str(score), True, zluta)
    okno.blit(value, [0, 0])


def zobraz_hada(snake_block, had_seznam):
    for kus_hada in had_seznam:
        pygame.draw.rect(okno, cerna, [kus_hada[0], kus_hada[1], snake_block, snake_block])


def zobraz_zpravu(zprava, barva):
    zprava_render = font_style.render(zprava, True, barva)
    okno.blit(zprava_render, [okno_sirka / 6, okno_vyska / 3])


def herni_smycka():
    hra_skoncila = False
    prohral = False

    hlava_pozice_x = okno_sirka / 2
    hlava_pozice_y = okno_vyska / 2

    aktualni_smer_x = 0
    aktualni_smer_y = 0

    had_seznam = []
    had_delka = 1

    jidlo_pozice_x = round(random.randrange(0, okno_sirka - snake_block) / 10.0) * 10.0
    jidlo_pozice_y = round(random.randrange(0, okno_vyska - snake_block) / 10.0) * 10.0

    while not hra_skoncila:

        while prohral == True:
            okno.fill(modra)
            zobraz_zpravu("Prohrál jsi! Zmáčkni klávesu C pro novou hru, nebo Q pro konec hry.", cervena)
            zobraz_skore(had_delka - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        hra_skoncila = True
                        prohral = False
                    if event.key == pygame.K_c:
                        herni_smycka()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hra_skoncila = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    aktualni_smer_x = -snake_block
                    aktualni_smer_y = 0
                elif event.key == pygame.K_RIGHT:
                    aktualni_smer_x = snake_block
                    aktualni_smer_y = 0
                elif event.key == pygame.K_UP:
                    aktualni_smer_y = -snake_block
                    aktualni_smer_x = 0
                elif event.key == pygame.K_DOWN:
                    aktualni_smer_y = snake_block
                    aktualni_smer_x = 0

        if hlava_pozice_x >= okno_sirka or hlava_pozice_x < 0 or hlava_pozice_y >= okno_vyska or hlava_pozice_y < 0:
            prohral = True
        hlava_pozice_x += aktualni_smer_x
        hlava_pozice_y += aktualni_smer_y
        okno.fill(modra)
        pygame.draw.rect(okno, zelena, [jidlo_pozice_x, jidlo_pozice_y, snake_block, snake_block])
        had_hlava = []
        had_hlava.append(hlava_pozice_x)
        had_hlava.append(hlava_pozice_y)
        had_seznam.append(had_hlava)
        if len(had_seznam) > had_delka:
            del had_seznam[0]

        for x in had_seznam[:-1]:
            if x == had_hlava:
                prohral = True

        zobraz_hada(snake_block, had_seznam)
        zobraz_skore(had_delka - 1)

        pygame.display.update()

        if hlava_pozice_x == jidlo_pozice_x and hlava_pozice_y == jidlo_pozice_y:
            jidlo_pozice_x = round(random.randrange(0, okno_sirka - snake_block) / 10.0) * 10.0
            jidlo_pozice_y = round(random.randrange(0, okno_vyska - snake_block) / 10.0) * 10.0
            had_delka += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


herni_smycka()