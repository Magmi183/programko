# Import modules
import pygame
import math
import random
pygame.init()

# Initialize constants
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

display_width = 800
display_height = 600

player_size = 10
fd_fric = 0.5
bd_fric = 0.1
player_max_speed = 20
player_max_rtspd = 10
bullet_speed = 15
saucer_speed = 5
small_saucer_accuracy = 10

# Make surface and display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Asteroids")
timer = pygame.time.Clock()


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

# Create function to draw texts
def drawText(msg, color, x, y, s, center=True):
    screen_text = pygame.font.SysFont("Calibri", s).render(msg, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (x, y)
    else:
        rect = (x, y)
    gameDisplay.blit(screen_text, rect)


# Create class bullet
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.life = 30

    def updateBullet(self):
        # Moving
        self.x += bullet_speed * math.cos(self.direction * math.pi / 180)
        self.y += bullet_speed * math.sin(self.direction * math.pi / 180)

        # Drawing
        pygame.draw.circle(gameDisplay, white, (int(self.x), int(self.y)), 3)

        # Wrapping
        if self.x > display_width:
            self.x = 0
        elif self.x < 0:
            self.x = display_width
        elif self.y > display_height:
            self.y = 0
        elif self.y < 0:
            self.y = display_height
        self.life -= 1




# Class player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hspeed = 0
        self.vspeed = 0
        self.dir = 0
        self.rtspd = 0
        self.thrust = False
        self.image = pygame.image.load("rocket.png")

    def updatePlayer(self):
        # Move player
        speed = math.sqrt(self.hspeed**2 + self.vspeed**2)
        if self.thrust:
            if speed + fd_fric < player_max_speed:
                self.hspeed += fd_fric * math.cos(self.dir * math.pi / 180)
                self.vspeed += fd_fric * math.sin(self.dir * math.pi / 180)
            else:
                self.hspeed = player_max_speed * math.cos(self.dir * math.pi / 180)
                self.vspeed = player_max_speed * math.sin(self.dir * math.pi / 180)
        else:
            if speed - bd_fric > 0:
                change_in_hspeed = (bd_fric * math.cos(self.vspeed / self.hspeed))
                change_in_vspeed = (bd_fric * math.sin(self.vspeed / self.hspeed))
                if self.hspeed != 0:
                    if change_in_hspeed / abs(change_in_hspeed) == self.hspeed / abs(self.hspeed):
                        self.hspeed -= change_in_hspeed
                    else:
                        self.hspeed += change_in_hspeed
                if self.vspeed != 0:
                    if change_in_vspeed / abs(change_in_vspeed) == self.vspeed / abs(self.vspeed):
                        self.vspeed -= change_in_vspeed
                    else:
                        self.vspeed += change_in_vspeed
            else:
                self.hspeed = 0
                self.vspeed = 0
        self.x += self.hspeed
        self.y += self.vspeed

        # Check for wrapping
        if self.x > display_width:
            self.x = 0
        elif self.x < 0:
            self.x = display_width
        elif self.y > display_height:
            self.y = 0
        elif self.y < 0:
            self.y = display_height

        # Rotate player
        self.dir += self.rtspd

    def drawPlayer(self):

        rotated_img, rect = rot_center(self.image, self.dir, self.x, self.y)
        gameDisplay.blit(rotated_img, rect)


    def killPlayer(self):
        # Reset the player
        self.x = display_width / 2
        self.y = display_height / 2
        self.thrust = False
        self.dir = -90
        self.hspeed = 0
        self.vspeed = 0


def gameLoop(startingState):
    # Init variables
    gameState = startingState
    player_state = "Alive"
    player_blink = 0
    player_dying_delay = 0
    player_invi_dur = 0
    hyperspace = 0
    bullet_capacity = 4
    bullets = []
    score = 0
    live = 2
    oneUp_multiplier = 1
    player = Player(display_width / 2, display_height / 2)


    # Main loop
    while gameState != "Exit":
        # Game menu
        while gameState == "Menu":
            gameDisplay.fill(black)
            drawText("ASTEROIDS", white, display_width / 2, display_height / 2, 100)
            drawText("Press any key to START", white, display_width / 2, display_height / 2 + 100, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameState = "Exit"
                if event.type == pygame.KEYDOWN:
                    gameState = "Playing"
            pygame.display.update()
            timer.tick(5)

        # User inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = "Exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.thrust = True
                if event.key == pygame.K_LEFT:
                    player.rtspd = -player_max_rtspd
                if event.key == pygame.K_RIGHT:
                    player.rtspd = player_max_rtspd
                if event.key == pygame.K_SPACE and player_dying_delay == 0 and len(bullets) < bullet_capacity:
                    bullets.append(Bullet(player.x, player.y, player.dir))
                if gameState == "Game Over":
                    if event.key == pygame.K_r:
                        gameState = "Exit"
                        gameLoop("Playing")
                if event.key == pygame.K_LSHIFT:
                    hyperspace = 30
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.thrust = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.rtspd = 0

        # Update player
        player.updatePlayer()

        # Checking player invincible time
        if player_invi_dur != 0:
            player_invi_dur -= 1
        elif hyperspace == 0:
            player_state = "Alive"

        # Reset display
        gameDisplay.fill(black)

        # Bullets
        for b in bullets:
            # Update bullets
            b.updateBullet()


        # Extra live
        if score > oneUp_multiplier * 10000:
            oneUp_multiplier += 1
            live += 1

        # Draw player
        if gameState != "Game Over":
            if player_state == "Died":
                if hyperspace == 0:
                    if player_dying_delay == 0:
                        if player_blink < 5:
                            if player_blink == 0:
                                player_blink = 10
                            else:
                                player.drawPlayer()
                        player_blink -= 1
                    else:
                        player_dying_delay -= 1
            else:
                player.drawPlayer()
        else:
            drawText("Game Over", white, display_width / 2, display_height / 2, 100)
            drawText("Press \"R\" to restart!", white, display_width / 2, display_height / 2 + 100, 50)
            live = -1

        # Draw score
        drawText(str(score), white, 60, 20, 40, False)

        # Update screen
        pygame.display.update()

        # Tick fps
        timer.tick(30)


# Start game
gameLoop("Menu")

# End game
pygame.quit()
quit()
