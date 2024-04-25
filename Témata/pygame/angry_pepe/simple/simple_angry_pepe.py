import pygame
import random

# Část 1.: Příprava Pygame
# Zde nic moc měnit nemusíte, jedná se o obecné věci potřebné pro běh pygame.
#   - můžete si nastavit vlastní velikost okna či název vaší hry
pygame.init()
velikost_okna = (600, 400)
okno = pygame.display.set_mode(velikost_okna)
pygame.display.set_caption("Simple Angry Pepe")
hodiny = pygame.time.Clock()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Část 2.: Přípravda proměnných a ostatních věcí PŘED herním cyklem
# Zde přijdou věci, které už jsou ušity na míru vaší hře.
# Stále se však jedná o počáteční nastavení, tedy věci, které se vykonají pouze JEDNOU.
# Sem patří i vytvoření funkcí, které budete používat.
#   - můžete si nastavit vlastní velikost okna či název vaší hry


font = pygame.font.Font('freesansbold.ttf', 32)

# Funkce, která zobrazí skóre, v bodě (0,0) tedy vlevo nahoře.
def zobraz_velikost(skore):
    text = font.render("Velikost: " + str(skore), True, BLACK)
    okno.blit(text, (0, 0))

# Nastavení POČÁTEČNÍCH pozic našich herních objektů.
pozice_x_jidlo = 200
pozice_y_jidlo = 200
pozice_x_pepe = 100
pozice_y_pepe = 100

# Vytvoření barev, které budeme používáat (jsou v RGB formátu, jestli nevíš co to je, zjisti si to!)
YELLOW = (222, 188, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Velikosti herních objektů
velikost_pepe = 60
velikost_jidlo = 30

# Nastavíme počáteční skóre a podmínku herního cyklu.
skore = 0
hraje_se = True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Část 3.: Herní smyčka
#          Zde přijde ta část kódu, která se neustále opakuje a aktualizuje stav hry.
#          Např. Snímání stisků kláves, posouvání a vykreslování objektů atd.
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hraje_se = False

    # Získáme SLOVNÍK stisknutých kláves (klíč = klávesa, hodnota = True/False)
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        # pokud je zmáčklá klávesa ŠIPKA NAHORU, tak zmenšíme pozici Y
        # to znamená, že postava se posune blíže k souřadnici 0, tedy k hornímu okraji
        pozice_y_pepe -= 5
    if pressed[pygame.K_DOWN]:
        pozice_y_pepe += 5
    if pressed[pygame.K_LEFT]:
        pozice_x_pepe -= 5
    if pressed[pygame.K_RIGHT]:
        pozice_x_pepe += 5

    # CELÉ OKNO PŘEMALUJEME NA BÍLO (NA ZAČÁTKU KAŽDÉHO CYKLU)
    okno.fill(WHITE)


    # Vytvoříme a vykreslíme naše postavy (tvary)
    pepe = pygame.Rect(pozice_x_pepe, pozice_y_pepe, velikost_pepe, velikost_pepe)
    pygame.draw.rect(okno, GREEN, pepe)
    jidlo = pygame.Rect(pozice_x_jidlo, pozice_y_jidlo, velikost_jidlo, velikost_jidlo)
    pygame.draw.rect(okno, YELLOW, jidlo)


    # Zkontrolujeme, jestli nedošlo ke kolizi.
    if pepe.colliderect(jidlo):
        # pokud ano, přidáme skóre a vygenerujeme novou pozici pro jídlo
        velikost_pepe += 5
        pozice_x_jidlo = random.randrange(550)
        pozice_y_jidlo = random.randrange(350)

    # zavoláme naší funkci, která vykreslí velikost
    zobraz_velikost(velikost_pepe)

    pygame.display.update() # tento příkaz updatuje herní okno
    hodiny.tick(60) # nastaví MAXIMÁLNÍ FPS na 60 (tzn., cyklus se provede max. 60x za sekundu)

# po skončení while cyklu ukončíme pygame
pygame.quit()
