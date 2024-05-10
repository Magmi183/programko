import pygame
import random

pygame.init()

RECT_WIDTH = 10

def drawText(bg, msg, color, x, y, s, center=True):
    screen_text = pygame.font.SysFont("Calibri", s).render(msg, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (x, y)
    else:
        rect = (x, y)

    bg.window.blit(screen_text, rect)


class Background:
    def __init__(self, x_rects=50, y_rects=50, rect_width=RECT_WIDTH):
        self.width = x_rects * rect_width
        self.height = y_rects * rect_width
        self.colors = [(70, 255, 0), (170, 255, 0)]
        self.rect_width = rect_width
        self.x_rects = x_rects
        self.y_rects = y_rects
        self.window = pygame.display.set_mode((self.width, self.height))


    def draw(self):
        for y in range(0, self.y_rects):
            for x in range(0, self.x_rects):
                rect = pygame.Rect(x * self.rect_width, y * self.rect_width, self.rect_width,self.rect_width)
                pygame.draw.rect(self.window, self.colors[(y+x)%2], rect)



class Snake:
    def __init__(self, width=RECT_WIDTH):
        self.width = width
        self.parts = [(10 * width, 10 * width)]
        self.direction = "RIGHT"

    def draw(self, bg):

        for part in self.parts:
            part_rect = pygame.Rect(part[0], part[1], self.width, self.width)
            pygame.draw.rect(bg.window, (111, 111, 111), part_rect)

    def change_direction(self, new_direction):
        opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposites[self.direction]:
            self.direction = new_direction

    def move(self, grow = False):
        head_x, head_y = self.parts[0]
        if self.direction == "UP":
            head_y -= self.width
        elif self.direction == "DOWN":
            head_y += self.width
        elif self.direction == "LEFT":
            head_x -= self.width
        elif self.direction == "RIGHT":
            head_x += self.width

        new_head = (head_x, head_y)
        self.parts.insert(0, new_head)

        if not grow:
            self.parts.pop()

    def collide(self, food_rect):
        head_rect = pygame.Rect(self.parts[0][0], self.parts[0][1], self.width, self.width)
        return head_rect.colliderect(food_rect)

    def check_self_collision(self):
        head = self.parts[0]
        return head in self.parts[1:]

    def check_wall_collision(self, bg):
        head_x, head_y = self.parts[0]
        return not (0 <= head_x < bg.width and 0 <= head_y < bg.height)




pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def game():
    bg = Background()
    snake = Snake()
    fx = RECT_WIDTH * 20
    fy = RECT_WIDTH * 20
    dead = False

    run = True
    while run:

        while dead == True:
            bg.draw()
            drawText(bg, "SNAKE", (0,0,0), bg.width / 2, bg.height / 2, 30)
            drawText(bg, "Press any key to START", (0,0,0), bg.width / 2, bg.height / 2 + 100, 15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    game()
            pygame.display.update()
            clock.tick(5)


        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                    break
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                    break
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                    break
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                    break


        food_rect = pygame.Rect(fx, fy, RECT_WIDTH, RECT_WIDTH)


        grow = False
        if snake.collide(food_rect):
            grow = True
            fx = random.randint(0, 40) * RECT_WIDTH
            fy = random.randint(0, 40) * RECT_WIDTH

        if snake.check_self_collision() or snake.check_wall_collision(bg):
            dead = True

        bg.draw()
        pygame.draw.rect(bg.window, (66, 66, 255), food_rect)
        snake.draw(bg)
        snake.move(grow)

        pygame.display.update()
        clock.tick(10)

game()
pygame.quit()
