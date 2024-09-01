import pygame, sys, random
class Score:
    def __init__(self):
        self.count = 0
        self.font = font
        self.text = self.font.render("Score: " + str(self.count), 1, (255,255,255))
    def score_up(self):
        self.count += 1
        self.text = self.font.render("Score: " + str(self.count), 1, (255,255,255))

    def Show_Score(self,x,y):
        Screen.blit(self.text, (x, y))
class player:
    def __init__(self):
        self.pos = pygame.math.Vector2(0,230)
        self.img = pygame.Surface((20,20))
        self.velo = pygame.math.Vector2(0,0)
    def draw(self):
        Screen.blit(self.img,self.pos)
        self.img.fill((255,255,0))
    def update(self):
        self.pos = self.pos + self.velo
class obstacle1:
    def __init__(self):
        self.pos = pygame.math.Vector2(random.randint(Xlen+50,Xlen+1000),230)
        self.img = pygame.Surface((20,20))
        self.img.fill((255,0,0))
        self.velo = pygame.math.Vector2(-5,0)
    def draw(self):
        Screen.blit(self.img,self.pos)
    def update(self):
        self.pos += self.velo
    def recreate(self):
        self.pos.x = random.randint(Xlen + 50, Xlen + 1000)
class obstacle2:
    def __init__(self):
        self.pos = pygame.math.Vector2(random.randint(Xlen+50,Xlen+1000),230)
        self.img = pygame.Surface((20,20))
        self.img.fill((0,255,0))
        self.velo = pygame.math.Vector2(-5,0)
    def draw(self):
        Screen.blit(self.img,self.pos)
    def update(self):
        self.pos += self.velo
    def recreate(self):
        self.pos.x = random.randint(Xlen + 50, Xlen + 1000)
class obstacle3:
    def __init__(self):
        self.pos = pygame.math.Vector2(random.randint(Xlen+50,Xlen+1000),230)
        self.img = pygame.Surface((20,20))
        self.img.fill((255,0,255))
        self.velo = pygame.math.Vector2(-5,0)
    def draw(self):
        Screen.blit(self.img,self.pos)
    def update(self):
        self.pos += self.velo
    def recreate(self):
        self.pos.x = random.randint(Xlen + 50, Xlen + 1000)
    


pygame.init()
font = pygame.font.Font("freesansbold.ttf",20)
Ylen = 350
Xlen = 450
Screen = pygame.display.set_mode((Xlen,Ylen))
Clock = pygame.time.Clock()
fps = 60
jump = 10
pygame.time.set_timer(pygame.USEREVENT,10)
P1 = player()
O1 = obstacle1()
O2 = obstacle2()
O3 = obstacle3()
SCORE = Score()
while True:
    Clock.tick(fps)
    Screen.fill((0,0,0))
    P1.draw()
    O1.draw()
    O2.draw()
    O3.draw()
    SCORE.Show_Score(185, 300)
    pygame.draw.rect(Screen,(255,255,255),(0,250,Xlen,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            O1.update()
            O2.update()
            O3.update()
            P1.update()
            if O1.pos.x < -30:
                O1.recreate()
                SCORE.score_up()
            if O2.pos.x < -30:
                O2.recreate()
                SCORE.score_up()
            if O3.pos.x < -30:
                O3.recreate()
                SCORE.score_up()
            if P1.pos.y > 210 and (0 <= O1.pos.x <= 20 or 0 <= O2.pos.x <= 20 or 0 <= O3.pos.x <= 20):
                O3.velo.x = 0
                O2.velo.x = 0
                O1.velo.x = 0
            if P1.pos.y > 230:
                P1.pos.y = 230
                P1.velo.y = 0
            else:
                P1.velo.y += jump/20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and P1.pos.y == 230:
                P1.velo.y -= jump
            if event.key == pygame.K_ESCAPE:
                O1 = obstacle1()
                O2 = obstacle1()
                O3 = obstacle3()
                SCORE.count = -1
                SCORE.score_up()
            
                
    pygame.display.flip()
        
