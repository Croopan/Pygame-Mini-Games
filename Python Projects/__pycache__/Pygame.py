import pygame
import sys,random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.pos = Vector2(random.randint(0,int(cell_number.x-1)),random.randint(0,int(cell_number.y-1)))
    def draw_fruit(self):
        fruit_rect = pygame.Rect(cell_size*self.pos.x, cell_size*self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen,(255,100,0),fruit_rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(7,5), Vector2(6,5), Vector2(5,5)]
        self.direction = Vector2(1,0)
        self.fruity = True
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(cell_size*int(block.x), cell_size*int(block.y), cell_size, cell_size)
            pygame.draw.rect(screen,(0,0,255),snake_rect)

    def move_snake(self):
        if self.fruity == True:
            self.body.pop()
        else:
            self.fruity = True
        self.body.insert(0, self.body[0] + self.direction)

class Main:
    def __init__(self) -> None:
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit = FRUIT()
            self.snake.fruity = False
        self.snake.move_snake()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def Game_over(self):
        pygame.quit()
        sys.exit()
    def draw_Score(self):
        Score = len(self.snake.body) - 3
        Score_surface = font.render(Score,True,"green")
        Score_rect = Score_surface.get_rect()

        
        

pygame.init()
cell_size = 40
font = pygame.font.Font(None,cell_size)
cell_number = Vector2(21,11)
screen = pygame.display.set_mode((cell_number.x*cell_size, cell_number.y*cell_size)) #sets screen
clock = pygame.time.Clock() 
Game = Main()


Screen_Update = pygame.USEREVENT
pygame.time.set_timer(Screen_Update,150)

while True:
    screen.fill(pygame.Color(0,200,100))
    Game.draw_elements()
    pygame.display.update() #updates display
    clock.tick(60)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #checks for quitting
            pygame.quit()
            sys.exit()
        if event.type == Screen_Update:
            Game.update()
            for x in range(1,len(Game.snake.body)):
                if Game.snake.body[0] == Game.snake.body[x]:
                    Game.Game_over()
                    break
            if Game.snake.body[0].x >= cell_number.x or Game.snake.body[0].x < 0 or Game.snake.body[0].y >= cell_number.y or Game.snake.body[0].y < 0:
                Game.Game_over()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Game.snake.direction != Vector2(0,1):
                Game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT and Game.snake.direction != Vector2(-1,0):
                Game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT and Game.snake.direction != Vector2(1,0):
                Game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_DOWN and Game.snake.direction != Vector2(0,-1):
                Game.snake.direction = Vector2(0,1)
