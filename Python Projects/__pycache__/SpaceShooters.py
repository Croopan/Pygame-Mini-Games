import pygame,sys,random,os
def load_images(path):
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('image1.png'))
        self.images.append(load_image('image2.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class explosion:
    def __init__(self,x,y):
        self.i = 0
        self.img= []
        self.pos = pygame.math.Vector2(x,y)
        self.img.append(pygame.image.load("frame_apngframe01.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe02.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe03.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe06.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe11.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe14.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe15.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe16.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe17.png").convert_alpha())
        self.img.append(pygame.image.load("frame_apngframe19.png").convert_alpha())
    def update(self):
        if self.i >= len(self.img):
            return False
        else:
            Screen.blit(self.img[int(self.i)],(self.pos))
            self.i += 1
class Score:
    def __init__(self):
        self.count = 0
        self.font = font
        self.text = self.font.render("Score: " + str(self.count), 1, (255,255,255))
    def score_up(self):
        self.count += random.randint(50,200)
        self.text = self.font.render("Score: " + str(self.count), 1, (255,255,255))

    def Show_Score(self,x,y):
        Screen.blit(self.text, (x, y))

class bullet:
    def __init__(self,Name):
        self.pos = pygame.math.Vector2(Name.pos.x + 5,Name.pos.y)
        self.img = Name.bullets_img
        self.velo = pygame.math.Vector2(0,-5)
        self.HB = pygame.mask.from_surface(self.img)
    def update(self):
        self.pos += self.velo
        Screen.blit(self.img,self.pos)
class player:
    def __init__(self):
        self.pos = pygame.math.Vector2(215,320)
        self.img = img4
        self.velo = pygame.math.Vector2(0,0)
        self.mask = pygame.mask.from_surface(self.img)
        self.health = 100
        self.bullets_img = img5 
        self.bullets = []
        self.score = Score()
    def draw(self):
        Screen.blit(self.img,self.pos)
    def update(self):
        if self.health < 100:
            pygame.draw.rect(Screen, (255,0,0), (self.pos.x - 5, self.pos.y - 10, 40, 5))
            pygame.draw.rect(Screen, (0,255,0), (self.pos.x - 5, self.pos.y - 10, 40*(self.health/100), 5))
        self.pos = self.pos + self.velo
        if self.pos.x >= Xlen-30:
            self.pos.x = Xlen-30
            self.velo.x = 0
        if self.pos.x <= 0:
            self.pos.x = 0
            self.velo.x = 0
        for x in self.bullets:
            x.update()
    def shoot(self):
        self.bullets.append(bullet(self))
        if self.bullets and self.bullets[0].pos.y < 0:
            self.bullets.pop(0)
    def hit(self):
        self.health -= 25


class enemies():
    def __init__(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.velo = pygame.math.Vector2(-2,0)
        self.img = imgs[random.randint(0,2)]
        self.bullets_img = img6
        self.HB = pygame.mask.from_surface(self.img)
        self.bullets = []
    def redirect(self):
        self.velo.x *= -1
    def draw(self):
        
        Screen.blit(self.img,(self.pos))
        self.pos += self.velo
        if self.bullets:
            for x in self.bullets:
                x.velo.y = 5
                x.update()
                if x.pos.y > 350:
                    self.bullets.pop(0)
    def leveldown(self):
        self.pos.y += 40
    def shoot(self):
        self.bullets.append(bullet(self))
pygame.init()
font = pygame.font.Font("freesansbold.ttf", 10)
font2 = pygame.font.Font("freesansbold.ttf", 30)
text_surface = font2.render('Play Again', False, (255, 255, 255))
text_surface2 = font2.render('Play Again', False, (255, 0, 0))

Ylen = 350
Xlen = 450
Screen = pygame.display.set_mode((Xlen,Ylen))
Clock = pygame.time.Clock()
Reload = pygame.time.Clock()
# Import Graphics for Enemies
img1 = pygame.image.load("Pink.png").convert_alpha()
img1 = pygame.transform.scale(img1,(20,20))
img2 = pygame.image.load("Blue.png").convert_alpha()
img2 = pygame.transform.scale(img2,(20,20))
img3 = pygame.image.load("Yellow.png").convert_alpha()
img3 = pygame.transform.scale(img3,(20,20))
img4 = pygame.image.load("Ship.jpg").convert_alpha()
img4 = pygame.transform.scale(img4,(30,30))
img5 = pygame.image.load("Laser.jpeg").convert_alpha()
img5 = pygame.transform.scale(img5,(10,20))
img6 = pygame.image.load("RedLaser.jpg").convert_alpha()
img6 = pygame.transform.scale(img6,(10,10))
img7 = pygame.image.load("SmallHitExplosion.jpeg").convert_alpha()
img7 = pygame.transform.scale(img7,(10,10))
Game_over = pygame.image.load("GameOver.jpeg").convert_alpha()
Game_over = pygame.transform.scale(Game_over,(400,300))

exp1 = pygame.image.load("frame_apngframe01.png")
exp1 = pygame.transform.scale(exp1, (20,20))
exp2 = pygame.image.load("frame_apngframe01.png")
exp2 = pygame.transform.scale(exp1, (20,20))
exp3 = pygame.image.load("frame_apngframe01.png")
exp3 = pygame.transform.scale(exp1, (20,20))
exp4 = pygame.image.load("frame_apngframe01.png")
exp4 = pygame.transform.scale(exp1, (20,20))
exp5 = pygame.image.load("frame_apngframe01.png")
exp5 = pygame.transform.scale(exp1, (20,20))
exp6 = pygame.image.load("frame_apngframe01.png")
exp6 = pygame.transform.scale(exp1, (20,20))
exp7 = pygame.image.load("frame_apngframe01.png")
exp7 = pygame.transform.scale(exp1, (20,20))

exps = [exp1,exp2,exp3,exp4,exp5,exp6,exp7]
        
            
imgs = [img1,img2,img3]


fps = 60
Ship = player()
Custom = pygame.USEREVENT + 1
Another = pygame.USEREVENT + 2
pygame.time.set_timer(Custom,10000)
pygame.time.set_timer(Another,500)

shot = False
start = None
Cooldown = 0
bad = []
Xi = 90
Yi = 20
game = False
val = False
xpos = 0
ypos = 0
red_button = pygame.Surface((100, 50))
explosions = []

while True:

    Screen.fill(pygame.Color("black"))
    Clock.tick(60)
    
    if not game:
        Screen.blit(Game_over,(20,0))
        Screen.blit(text_surface,(150,250))
        Ship.score.Show_Score(200,200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 200 < pos[0] < 275 and 250 < pos[1] < 300:
                    text_surface = font2.render('Play Again', False, (255, 0, 0))

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 200 < pos[0] < 275 and 250 < pos[1] < 300:
                    game = True
                    Ship = player()
                    bad.clear()
    else:
        for f in explosions:
            if not f.update():
                explosions.remove(f)
        Ship.update()
        Ship.draw()
        Ship.score.Show_Score(0,340)
        if Ship.health == 0:
            for x in bad:
                x.velo = pygame.Vector2(0,0)
                Cooldown = pygame.time.get_ticks()
                i = 0
                game = False
        if val:
            Screen.blit(img7,(xpos,ypos))
            if pygame.time.get_ticks() - Cooldown > 100:
                val = False
            

        if len(bad) == 0:
            j = 0
            while j < 6:
                i = 0
                while i < 3:
                    bad.append(enemies(Xi + j*50,Yi + i*40))
                    i += 1
                j += 1
        else:
            if bad[0].pos.x <= 0 or bad[-1].pos.x >= 430:
                for x in bad:
                    x.redirect()
                    x.draw()
            else:
                for x in bad:
                    x.draw()
                    if x.bullets and x.bullets[0].HB.overlap(Ship.mask,(Ship.pos.x - x.bullets[0].pos.x, Ship.pos.y - x.bullets[0].pos.y)) and pygame.time.get_ticks()-Cooldown > 200:
                        #Here you would have the health shit
                        p = x.bullets.pop(0)
                        Ship.hit()
                        Cooldown = pygame.time.get_ticks()
                        val = True
                        xpos = p.pos.x
                        ypos = p.pos.y
        if shot and pygame.time.get_ticks() - start > 300:
            start = pygame.time.get_ticks()
            Ship.shoot()

        #Collisions
        for x in Ship.bullets:
            for y in bad:
                if x.HB.overlap(y.HB,(x.pos.x - y.pos.x, x.pos.y - y.pos.y)):
                    Ship.bullets.remove(x)
                    Ship.score.score_up()
                    explosions.append(explosion(x.pos.x,x.pos.y))
                    bad.remove(y)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == Custom and game:
                for x in bad:
                    x.leveldown()
            if event.type == Another and game:
                bad[random.randint(0,len(bad)-1)].shoot()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and Ship.pos.x >= 0:
                    Ship.velo.x = -5 
                if event.key == pygame.K_RIGHT and Ship.pos.x <= Xlen-30:
                    Ship.velo.x = 5
                if event.key == pygame.K_SPACE:
                    shot = True
                    Ship.shoot()
                    start = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Ship.velo.x = 0
                if event.key == pygame.K_RIGHT:
                    Ship.velo.x = 0
                if event.key == pygame.K_SPACE:
                    shot = False
            

    pygame.display.flip()
