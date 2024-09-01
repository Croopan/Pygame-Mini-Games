import pygame, sys, math
from pygame.math import Vector2

class Score:
    def __init__(self):
        self.count = 0
        self.font = font
        self.text = self.font.render("Score: " + str(self.count), 1, (255,255,255),)
    def score_up(self):
        self.count += 1
        self.text = self.font.render("Score: " + str(self.count), 1, (255,255,255))

    def Show_Score(self,x,y):
        Screen.blit(self.text, (x, y))

class Paddles:
    def __init__(self):
        self.x = 10
        self.y = Ylen//2 - 100//2
        self.velocity = 0

    def Draw_paddles(self):
        Paddle_rect = pygame.Rect(self.x, self.y, 20, 100)
        pygame.draw.rect(Screen,(255,255,255),Paddle_rect)

    def Move_paddles(self):
        self.y += self.velocity

class Ball:
    def __init__(self):
        self.pos = Vector2(Xlen//2, Ylen//2)
        self.speed = 10
        self.velocity = Vector2(-self.speed,0)
    def DrawBall(self):
        Ball_Circle = (self.pos.x,self.pos.y)
        pygame.draw.circle(Screen,(255,255,255),Ball_Circle,15)
    def BounceWall(self):
        self.velocity.y *= -1
    def MoveBall(self):
        self.pos += self.velocity

class Main:
    def __init__(self):
        self.ball = Ball()
        self.Pad1 = Paddles()
        self.Pad2 = Paddles()
        self.Pad2.x = Xlen-30
        self.MaxBounce = 1
        self.Score1 = Score()
        self.Score2 = Score()
    def draw(self):
        self.ball.DrawBall()        
        self.Pad1.Draw_paddles()
        self.Pad2.Draw_paddles()
    def update(self):
        self.ball.MoveBall()
        self.Pad1.Move_paddles()
        self.Pad2.Move_paddles()
        self.Score1.Show_Score(30,20)
        self.Score2.Show_Score(Xlen-100,20)
    def check_collision(self):
        if self.Pad1.x + 35 >= self.ball.pos.x:
            return self.Pad1
        
        elif self.Pad2.x - 15 <= self.ball.pos.x:
            return self.Pad2
        else:
            return False
    def hit(self,y):
        if self.ball.pos.y <= self.Pad1.y+100 and self.ball.pos.y >= self.Pad1.y and y == self.Pad1:
            return self.Pad1
        if self.ball.pos.y <= self.Pad2.y+100 and self.ball.pos.y >= self.Pad2.y and y == self.Pad2:
            return self.Pad2
        return False
    def collision(self,x):
        if x == self.Pad1:
            RelativeHit = self.ball.pos.y - self.Pad1.y - 50
            NormalHit = RelativeHit/50
            Angle = NormalHit * self.MaxBounce
            self.ball.velocity = Vector2(abs((self.ball.speed*math.cos(Angle))), self.ball.speed*math.sin(Angle))
            self.Score1.score_up()
        if x == self.Pad2:
            RelativeHit = self.ball.pos.y - self.Pad2.y - 50
            NormalHit = RelativeHit/50
            Angle = NormalHit * self.MaxBounce
            self.ball.velocity = Vector2(-abs(self.ball.speed*math.cos(Angle)), self.ball.speed*math.sin(Angle))
            self.Score2.score_up()


pygame.init()
font = pygame.font.Font("freesansbold.ttf",20)
Ylen = 600
Xlen = 1000
Game = Main()
Screen = pygame.display.set_mode((Xlen,Ylen))
Clock = pygame.time.Clock()
Update = pygame.USEREVENT

while True:
    Screen.fill(pygame.Color("black"))
    Game.draw()
    Game.update()
    Clock.tick(60)
    if Game.ball.pos.y -15 <= 0 or Game.ball.pos.y + 15 >= Ylen:
        if Game.ball.pos.y +15 >= Ylen:
            Game.ball.pos.y = Ylen - 20
        else:
            Game.ball.pos.y = 20       
        Game.ball.BounceWall()
    if Game.Pad1.y <= 0 or Game.Pad1.y >= Ylen-100:
        if Game.Pad1.y <= 0:
            Game.Pad1.y = 0
        else:
            Game.Pad1.y = Ylen-100
        Game.Pad1.velocity = 0
    if Game.Pad2.y <= 0 or Game.Pad2.y >= Ylen-100:
        if Game.Pad2.y <= 0:
            Game.Pad2.y = 0
        else:
            Game.Pad2.y = Ylen-100
        Game.Pad2.velocity = 0
    if Game.check_collision():        
        if Game.hit(Game.check_collision()):
            Game.collision(Game.hit(Game.check_collision()))
        else:
            Game.ball.velocity = Vector2(0,0)
            if Game.check_collision() == Game.Pad1:
                Game.ball.pos.x = 45
            else:
                Game.ball.pos.x = Xlen-45

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Game.Pad2.y >= 0:
                Game.Pad2.velocity = -10
            if event.key == pygame.K_DOWN and Game.Pad2.y <= Ylen-100:
                Game.Pad2.velocity = 10
            if event.key == pygame.K_w and Game.Pad1.y >= 0:
                Game.Pad1.velocity = -10
            if event.key == pygame.K_s and Game.Pad1.y <= Ylen-100:
                Game.Pad1.velocity = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Game.Pad2.velocity = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                Game.Pad1.velocity = 0


    pygame.display.update()
        