import pygame

pygame.init()
velikost_okna = (600, 400)
okno = pygame.display.set_mode(velikost_okna)
pygame.display.set_caption("NÁZEV HRY")
hodiny = pygame.time.Clock()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

hraje_se = True
WHITE = (255, 255, 255)

while hraje_se:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hraje_se = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        # zmáčknutá šipka nahoru
        pass
    if pressed[pygame.K_DOWN]:
        # zmáčknutá šipka dolu
        pass

    okno.fill(WHITE)

    # Sem budete psát kód hry ...
    # ...

    # ...
    pygame.display.update()
    hodiny.tick(60)

pygame.quit()
