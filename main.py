import pygame
import os

# Initializes pygame and sets window to 800 x-axis and 600 y-axis.
pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Next few lines define name of window, the symbol of window, and defines the background and symbols.
pygame.display.set_caption("Macbeth Dagger Scene")
FPS = 60
fpsClock = pygame.time.Clock()

# icon = pygame.image.load('somethin.png')
# pygame.display.set_icon(icon)

PlayerRight1 = pygame.image.load('PlayerPngs/PlayerRight1.png')
PlayerRight2 = pygame.image.load('PlayerPngs/PlayerRight2.png')
PlayerRight3 = pygame.image.load('PlayerPngs/PlayerRight3.png')
PlayerLeft1 = pygame.image.load('PlayerPngs/PlayerLeft1.png')
PlayerLeft2 = pygame.image.load('PlayerPngs/PlayerLeft2.png')
PlayerLeft3 = pygame.image.load('PlayerPngs/PlayerLeft3.png')
PlayerBack1 = pygame.image.load('PlayerPngs/PlayerBack1.png')
PlayerBack2 = pygame.image.load('PlayerPngs/PlayerBack2.png')
PlayerBack3 = pygame.image.load('PlayerPngs/PlayerBack3.png')
PlayerFront1 = pygame.image.load('PlayerPngs/PlayerFront1.png')
PlayerFront2 = pygame.image.load('PlayerPngs/PlayerFront2.png')
PlayerFront3 = pygame.image.load('PlayerPngs/PlayerFront3.png')
DaggerUp = pygame.image.load('DaggerPngs/DaggerUp.png')
DaggerUpBloody = pygame.image.load('DaggerPngs/DaggerUpBloody.png')
DaggerDown = pygame.image.load('DaggerPngs/DaggerDown.png')
DaggerDownBloody = pygame.image.load('DaggerPngs/DaggerDownBloody.png')
DaggerRight = pygame.image.load('DaggerPngs/DaggerRight.png')
DaggerRightBloody = pygame.image.load('DaggerPngs/DaggerRightBloody.png')
Guilt1 = pygame.image.load('GuiltPngs/Guilt1.png')
Guilt2 = pygame.image.load('GuiltPngs/Guilt2.png')
AmbitionPoint = pygame.image.load('AmbitionPngs/AmbitionPoint.png')
Screenblockblack = pygame.image.load('ScreenblockerPngs/Screenblockblack.png')
Background1Part1 = pygame.image.load('BackgroundPngs/Background1Part1.png').convert()
Background1Part2 = pygame.image.load('BackgroundPngs/Background1Part2.png').convert()
Background1Part3 = pygame.image.load('BackgroundPngs/Background1Part3.png').convert()
Background1Part4 = pygame.image.load('BackgroundPngs/Background1Part4.png').convert()
Background2Part1 = pygame.image.load('BackgroundPngs/Background1Part4.png').convert()
Background2Part2 = pygame.image.load('BackgroundPngs/Background2Part2.png').convert()
Background2Part3 = pygame.image.load('BackgroundPngs/Background2Part3.png').convert()
Background2Part4 = pygame.image.load('BackgroundPngs/Background2Part4.png').convert()
Background3Part1 = pygame.image.load('BackgroundPngs/Background3Part1.png').convert()
Background3Part2 = pygame.image.load('BackgroundPngs/Background3Part2.png').convert()
Background3Part3 = pygame.image.load('BackgroundPngs/Background3Part3.png').convert()
Background3Part4 = pygame.image.load('BackgroundPngs/Background3Part4.png').convert()
Background4Part1 = pygame.image.load('BackgroundPngs/Background4Part1.png').convert()
Background4Part2 = pygame.image.load('BackgroundPngs/Background4Part2.png').convert()
Background4Part3 = pygame.image.load('BackgroundPngs/Background4Part3.png').convert()
Background4Part4 = pygame.image.load('BackgroundPngs/Background4Part4.png').convert()
Background5Part1 = pygame.image.load('BackgroundPngs/Background5Part1.png').convert()
Background5Part2 = pygame.image.load('BackgroundPngs/Background5Part2.png').convert()
Background5Part3 = pygame.image.load('BackgroundPngs/Background1Part4.png').convert()
Background5Part4 = pygame.image.load('BackgroundPngs/Background5Part4.png').convert()
Background6Part1 = pygame.image.load('BackgroundPngs/Background6Part1.png').convert()
Background6Part2 = pygame.image.load('BackgroundPngs/Background1Part4.png').convert()
Background6Part3 = pygame.image.load('BackgroundPngs/Background6Part3.png').convert()
Background6Part4 = pygame.image.load('BackgroundPngs/Background6Part4.png').convert()

prightanimationcycle = [PlayerRight1, PlayerRight2, PlayerRight1, PlayerRight3]

pleftanimationcycle = [PlayerLeft1, PlayerLeft2, PlayerLeft1, PlayerLeft3]

pbackanimationcycle = [PlayerBack1, PlayerBack2, PlayerBack1, PlayerBack3]

pfrontanimationcycle = [PlayerFront1, PlayerFront2, PlayerFront1, PlayerFront3]

screenblockervalue = False


class Enemy:
    curimg = Guilt1
    animationstep = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemyrect = self.curimg.get_rect()

    def update(self):
        self.enemyrect = self.curimg.get_rect()
        self.enemyrect.topleft = (self.x, self.y)
        screen.blit(Enemy.curimg, (self.x, self.y))


class Setting:

    def __init__(self, im1, im2, im3, im4, loc1, loc2, loc3, loc4, x1, y1, x2, y2, x3, y3, xstart, ystart, dagx, dagy, dagimg):
        self.image1 = im1
        self.image2 = im2
        self.image3 = im3
        self.image4 = im4
        self.loc1 = loc1
        self.loc2 = loc2
        self.loc3 = loc3
        self.loc4 = loc4
        self.enemy1 = Enemy(x1, y1)
        self.enemy2 = Enemy(x2, y2)
        self.enemy3 = Enemy(x3, y3)
        self.enemylist = [self.enemy1, self.enemy2, self.enemy3]
        self.quotevalue = 0
        self.xstart = xstart
        self.ystart = ystart
        self.daggerx = dagx
        self.daggery = dagy
        self.dagimg = dagimg

    def load(self):
        global screenblockervalue
        if self.quotevalue == 0:
            screen.blit(self.image1, (0, 0))
            screen.blit(self.image2, (600, 0))
            screen.blit(self.image3, (0, 400))
            screen.blit(self.image4, (600, 400))
            screen.blit(self.dagimg, (self.daggerx, self.daggery))
        if self.quotevalue > 0:
            self.quotevalue -= 1
        self.enemy1.update()
        self.enemy2.update()
        self.enemy3.update()
        Enemy.animationstep += 1
        if Enemy.animationstep == 61:
            Enemy.animationstep /= 61
            Enemy.curimg = Guilt2
        if Enemy.animationstep > 30:
            Enemy.curimg = Guilt1


class Player:

    def __init__(self):
        self.x = 600
        self.y = 600
        self.currentimg = PlayerRight1
        self.xoffset = self.currentimg.get_width()
        self.yoffset = self.currentimg.get_height()
        self.animationframecounty = 0
        self.curanimationlist = prightanimationcycle
        self.animationstep = 0
        self.xsave = self.x
        self.ysave = self.y
        self.health = 5
        self.ambitionxstep = 10

    def update(self):
        self.xsave = self.x
        self.ysave = self.y
        self.xoffset = self.currentimg.get_width()
        self.yoffset = self.currentimg.get_height()
        if activesetting.quotevalue == 0:
            if keys[pygame.K_d]:
                self.x += 5
                self.curanimationlist = prightanimationcycle
            elif keys[pygame.K_a]:
                self.x -= 5
                self.curanimationlist = pleftanimationcycle
            elif keys[pygame.K_w]:
                self.y -= 5
                self.curanimationlist = pbackanimationcycle
            elif keys[pygame.K_s]:
                self.y += 5
                self.curanimationlist = pfrontanimationcycle
            else:
                self.animationframecounty -= 1
                self.currentimg = self.curanimationlist[0]
            self.animationframecounty += 1

        if self.animationframecounty == 5:
            self.animationframecounty = 0
            if self.animationstep < 3:
                self.animationstep += 1
            else:
                self.animationstep = 0
            self.currentimg = self.curanimationlist[self.animationstep]

        if 0 < self.x < 1200 - self.xoffset and 45 < self.y < 800 - self.yoffset:
            pass
        else:
            self.x = self.xsave
            self.y = self.ysave
            self.checktransition()

        self.playerrect = self.currentimg.get_rect()
        self.playerrect.topleft = (self.x, self.y)

        for item in activesetting.enemylist:
            if self.playerrect.colliderect(item.enemyrect):
                self.health -= 1
                item.x = -500
        if activesetting == Setting6:
            if self.playerrect.colliderect(dagrect):
                activesetting.quotevalue = -20

        # Loads image
        screen.blit(self.currentimg, (self.x, self.y))
        self.loadhealth()

    def checktransition(self):
        if 500 < self.x < 700 - self.xoffset:
            if self.y < 400:
                self.switchscene(activesetting.loc1)
            else:
                self.switchscene(activesetting.loc3)
        elif 300 < self.y < 500 - self.yoffset:
            if self.x > 600:
                self.switchscene(activesetting.loc2)
            else:
                self.switchscene(activesetting.loc4)

    def switchscene(self, loc):
        global activesetting
        if loc == "ENTRY":
            activesetting = settings[settings.index(activesetting) - 1]
            self.decidepostrans()
        elif loc == "EXIT":
            activesetting = settings[settings.index(activesetting) + 1]
            activesetting.quotevalue = 420
            self.decidepostrans()

    def decidepostrans(self):
        self.x = activesetting.xstart
        self.y = activesetting.ystart

    def loadhealth(self):
        if self.health == 0:
            activesetting.quotevalue = -10
        for i in range(self.health):
            screen.blit(AmbitionPoint, (self.ambitionxstep, 10))
            self.ambitionxstep += 50
        self.ambitionxstep = 10


def screenblocker():
    if activesetting.quotevalue != 0:
        screen.blit(Screenblockblack, (0, 0))
        screen.blit(Screenblockblack, (600, 0))
        screen.blit(Screenblockblack, (0, 400))
        screen.blit(Screenblockblack, (600, 400))
        if activesetting.quotevalue == -10:
            screen.blit(pygame.font.Font('freesansbold.ttf', 64).render('GAME OVER', True, (255, 255, 255)), (400, 350))
            screen.blit(pygame.font.Font('freesansbold.ttf', 48).render('IF CHANCE WILL HAVE ME KING, WHY,', True, (255,
                                                                        255, 255)), (100, 550))
            screen.blit(pygame.font.Font('freesansbold.ttf', 48).render('CHANCE MAY CROWN ME WITHOUT MY STIR', True,
                                                                        (255, 255, 255)), (100, 650))
        elif activesetting.quotevalue == -20:
            screen.blit(pygame.font.Font('freesansbold.ttf', 64).render('I GO, AND IT IS DONE', True, (130, 0, 7)), (290, 350))
            screen.blit(pygame.font.Font('freesansbold.ttf', 48).render('YOU WIN!', True, (130, 0, 7)), (480, 550))
            screen.blit(PlayerFront1, (550, 120))
            screen.blit(DaggerUpBloody, (575, 700))
        else:
            screen.blit(pygame.font.Font('freesansbold.ttf', 48).render(texts[settings.index(activesetting)][0], True,
                                                                        (255, 255, 255)), (100, 250))
            screen.blit(pygame.font.Font('freesansbold.ttf', 48).render(texts[settings.index(activesetting)][1], True,
                                                                        (255, 255, 255)), (100, 350))
            screen.blit(pygame.font.Font('freesansbold.ttf', 48).render(texts[settings.index(activesetting)][2], True,
                                                                        (255, 255, 255)), (100, 450))


Player1 = Player()

Setting1 = Setting(Background1Part1, Background1Part2, Background1Part3, Background1Part4, "EXIT", "N", "N", "N", 475,
                   400, 575, 400, 675, 400, 600, 400, 590, 100, DaggerUp)
Setting2 = Setting(Background2Part1, Background2Part2, Background2Part3, Background2Part4, "N", "EXIT", "ENTRY", "N",
                   257, 577, 831, 571, 783, 276, 600, 600, 1080, 390, DaggerRight)
Setting3 = Setting(Background3Part1, Background3Part2, Background3Part3, Background3Part4, "N", "N", "EXIT", "ENTRY",
                   567, 441, 453, 541, 306, 655, 50, 325, 590, 722, DaggerDown)
Setting4 = Setting(Background4Part1, Background4Part2, Background4Part3, Background4Part4, "ENTRY", "N", "EXIT", "N",
                   575, 376, 355, 376, 795, 375, 567, 120, 590, 715, DaggerDownBloody)
Setting5 = Setting(Background5Part1, Background5Part2, Background5Part3, Background5Part4, "ENTRY", "EXIT", "N", "N",
                   376, 304, 575, 572, 914, 195, 567, 120, 1100, 400, DaggerRightBloody)
Setting6 = Setting(Background6Part1, Background6Part2, Background6Part3, Background6Part4, "N", "N", "N", "ENTRY",
                   244, 192, 548, 631, 786, 206, 50, 325, 1150, 480, DaggerUpBloody)

activesetting = Setting1

settings = [Setting1, Setting2, Setting3, Setting4, Setting5, Setting6]

texts = [["IS THIS A DAGGER WHICH I SEE BEFORE ME,", "THE HANDLE TOWARDS MY HAND?", "COME, LET ME CLUTCH THEE!"],
         ["THOU MARSHALL'ST ME THE", "WAY THAT I WAS GOING,", " AND SUCH AN INSTRUMENT I WAS TO USE."],
         ["MINE EYES ARE MADE THE", "FOOLS O' TH' OTHER SENSES,", "OR ELSE WORTH ALL THE REST."],
         ["I SEE THEE STILL, AND ON THY BLADE", "AND DUDGEON GOUTS OF BLOOD,", "WHICH WAS NOT SO BEFORE."],
         ["HEAR NOT MY STEPS, WHICH WAY THEY", "WALK FOR FEAR THY VERY STONES", "PRATE OF MY WHEREABOUT."],
         ["WHILE I THREAT, HE LIVES", "WORDS TO THE HEAT OF DEEDS", " TOO COLD BREATH GIVES."]]

activesetting.quotevalue = 420

dagrect = DaggerUpBloody.get_rect()
dagrect.topleft = (1150, 480)

# Main running element
running = True

# Main game loop. If it ends, game stops.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseposition = pygame.mouse.get_pos()
            print(mouseposition[0])
            print(mouseposition[1])
    # Keys pressed list
    keys = pygame.key.get_pressed()
    activesetting.load()
    Player1.update()
    screenblocker()
    # Updates displayer and makes sure FPS is stable.
    pygame.display.update()
    fpsClock.tick(FPS)
