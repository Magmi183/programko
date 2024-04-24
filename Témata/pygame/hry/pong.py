""""
/*
 *  _____ _______         _                      _
 * |_   _|__   __|       | |                    | |
 *   | |    | |_ __   ___| |___      _____  _ __| | __  ___ ____
 *   | |    | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / / __|_  /
 *  _| |_   | | | | |  __/ |_ \ V  V / (_) | |  |   < | (__ / /
 * |_____|  |_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)___/___|
 *                   ___
 *                  |  _|___ ___ ___
 *                  |  _|  _| -_| -_|  LICENCE
 *                  |_| |_| |___|___|
 *
 * IT ZPRAVODAJSTVÍ  <>  PROGRAMOVÁNÍ  <>  HW A SW  <>  KOMUNITA
 *
 * Tento zdrojový kód pochází z IT sociální sítě WWW.ITNETWORK.CZ
 *
 * Můžete ho upravovat a používat jak chcete, musíte však zmínit
 * odkaz na http://www.itnetwork.cz
 */
"""

# TODO: Prepsat hru tak aby byla bez class a dalsich slozitejsich konstruktu

import pygame

from random import randrange, choice
from math import radians, cos, sin


def sign(num: int) -> int:
    """
    Zjisti znamenko cisla
    :param num: kontrolovane cislo
    :return: 1 pokud je cislo kladne, -1 pokud je zaporne, jinak 0
    """
    return 1 if num > 0 else -1 if num < 0 else 0


class Game:
    def __init__(self):
        # maximalni rychlost hry v FPS
        self.FPS = 30

        # inicializace hry
        pygame.init()
        self.running = True
        self.display: pygame.Surface = pygame.display.set_mode((1366, 768))
        pygame.display.set_caption("PyONG")
        self.screen = pygame.Surface((1920, 1080))
        self.round_tick = 0  # poradi stepu behem kola
        self.clock = pygame.time.Clock()

        # inicializace pisem
        font_name = choice([x for x in pygame.font.get_fonts() if 'mono' in x.lower()])
        self.font_score = pygame.font.SysFont(font_name, 30)
        self.font_info = pygame.font.SysFont(font_name, 50)

        # inicializace hernich objektu
        player_size = (50, 200)
        self.player_speed = 10
        self.player2_ai = False

        self.player1_orig = pygame.Rect((0, self.screen.get_height() // 2), player_size)
        self.player1 = self.player1_orig.copy()
        self.player1_score = 0

        self.player2_orig = pygame.Rect((self.screen.get_width() - player_size[0], self.screen.get_height() // 2),
                                        player_size)
        self.player2 = self.player2_orig.copy()
        self.player2_score = 0

        ball_size = (20, 20)
        self.ball_orig = pygame.Rect((self.screen.get_width() // 2, self.screen.get_height() // 2), ball_size)
        self.ball = self.ball_orig.copy()
        self.ball_direction = 0  # je nastaveno na zacatku kazdeho kola
        self.ball_speed_orig = 15
        self.ball_speed_max = self.ball_speed_orig * 4
        self.ball_speed = self.ball_speed_orig

        # vytvoreni okraju mapy
        self.top = pygame.Rect((0, -self.ball_speed_max), (self.screen.get_width(), self.ball_speed_max))
        self.bottom = pygame.Rect((0, self.screen.get_height()), (self.screen.get_width(), self.ball_speed_max))
        self.left = pygame.Rect((-self.ball_speed_max, 0), (self.ball_speed_max, self.screen.get_height()))
        self.right = pygame.Rect((self.screen.get_width(), 0), (self.ball_speed_max, self.screen.get_height()))

        # nynejsi pouzita logika uvnitr herniho cyklu
        self.logic: Optional[Callable] = None  # je nastaveno uvnitr .main()

    def set_ball_direction(self, val: int):
        if abs(val) >= 360:
            val %= 360
        if val < 0:
            val = 360 + val
        self.ball_direction = val

    def main(self):
        self.logic = self.logic_game_start

        while self.running:
            # UDALOSTI
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
                    self.running = False

            # KROK
            self.logic()

            # KRESLENI
            pygame.draw.rect(self.screen, (255, 255, 255), self.player1)
            pygame.draw.rect(self.screen, (255, 255, 255), self.player2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.ball)

            text = self.font_score.render(f"{self.player1_score} : {self.player2_score}", True, (255, 255, 255))
            self.screen.blit(text, ((self.screen.get_width() - text.get_width()) / 2, 0))

            # FINALIZACE A PREDANI DAT NA OBRAZOVKU
            pygame.transform.scale(self.screen, self.display.get_size(), self.display)
            pygame.display.update()
            self.clock.tick(self.FPS)
            self.screen.fill((0, 0, 0))

    def logic_game_body(self):
        # POHYBY HRACE
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s] and not self.player1.colliderect(self.bottom):
            self.player1.move_ip(0, self.player_speed)
        elif pressed[pygame.K_w] and not self.player1.colliderect(self.top):
            self.player1.move_ip(0, -self.player_speed)
        if not self.player2_ai:
            if pressed[pygame.K_DOWN] and not self.player2.colliderect(self.bottom):
                self.player2.move_ip(0, self.player_speed)
            elif pressed[pygame.K_UP] and not self.player2.colliderect(self.top):
                self.player2.move_ip(0, -self.player_speed)
        else:  # POHYBY POCITACE
            move_y = sign(self.ball.centery - self.player2.centery) * \
                     min(self.player_speed, abs(self.player2.centery - self.ball.centery))
            if (move_y > 0 and not self.player2.colliderect(self.bottom)) or \
                    (move_y < 0 and not self.player2.colliderect(self.top)):
                self.player2.move_ip(0, move_y)

        # POHYB MICE
        ball_direction_radians = radians(self.ball_direction)
        self.ball.move_ip(self.ball_speed * cos(ball_direction_radians), self.ball_speed * sin(ball_direction_radians))

        # ODRAZENI A KOLIZE MICE
        if self.ball.collidelist([self.top, self.bottom]) > -1:
            self.set_ball_direction(-self.ball_direction)
        elif self.ball.collidelist([self.player1, self.player2]) > -1:
            # mic narazil do hrace, odraz se
            self.set_ball_direction(180 - self.ball_direction)

        # mic opustil hraci plochu, pricti body
        if self.ball.colliderect(self.left):
            self.player2_score += 1
            self.logic = self.logic_round_start
        elif self.ball.colliderect(self.right):
            self.player1_score += 1
            self.logic = self.logic_round_start

        if self.round_tick > 0 and self.round_tick % (2 * self.FPS) == 0:
            # zrychli mic o 10 % kazde 2 sekundy
            self.ball_speed = min(1.1 * self.ball_speed, self.ball_speed_max)

        self.round_tick += 1

    def logic_round_start(self):
        self.player1 = self.player1_orig.copy()
        self.player2 = self.player2_orig.copy()
        self.ball = self.ball_orig.copy()
        self.ball_speed = self.ball_speed_orig
        self.round_tick = 0

        self.set_ball_direction(choice(
            (randrange(-75, -15), randrange(15, 75), randrange(195, 255))
        ))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.logic = self.logic_game_body

        text = self.font_info.render("Press SPACE to start", True, (255, 255, 255))
        self.screen.blit(text, ((self.screen.get_width() - text.get_width()) / 2,
                                (self.screen.get_height() * 0.75 - text.get_height()) / 2))

    def logic_game_start(self):
        text = self.font_info.render("Press C to play with computer or H to play against human", True, (255, 255, 255))
        self.screen.blit(text, ((self.screen.get_width() - text.get_width()) / 2,
                                (self.screen.get_height() * 0.75 - text.get_height()) / 2))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_h] or pressed[pygame.K_c]:
            self.player2_ai = bool(pressed[pygame.K_c])
            self.logic = self.logic_round_start


if __name__ == '__main__':
    Game().main()
