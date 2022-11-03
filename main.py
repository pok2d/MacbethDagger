import pygame
import os

# Initializes pygame and sets window to 800 x-axis and 600 y-axis.
pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Next few lines define name of window, the symbol of window, and defines the background and symbols.
pygame.display.set_caption("Macbeth Dagger Scene")


# icon = pygame.image.load('somethin.png')
# pygame.display.set_icon(icon)

PlayerRight1 = pygame.image.load('PlayerRight1.png')
PlayerRight2 = pygame.image.load('PlayerRight2.png')
PlayerRight3 = pygame.image.load('PlayerRight3.png')
PlayerLeft1 = pygame.image.load('PlayerLeft1.png')
PlayerLeft2 = pygame.image.load('PlayerLeft2.png')
PlayerLeft3 = pygame.image.load('PlayerLeft3.png')

prightanimationcycle = [PlayerRight1, PlayerRight2, PlayerRight1, PlayerRight3]

pleftanimationcycle = [PlayerLeft1, PlayerLeft2, PlayerLeft1, PlayerLeft3]
class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.currentimg = PlayerRight1
        self.xoffset = self.currentimg.get_width()
        self.yoffset = self.currentimg.get_height()
        self.animationframecounty = 0
        self.curanimationlist = prightanimationcycle
        self.animationstep = 0

    def update(self):
        self.xoffset = self.currentimg.get_width()
        self.yoffset = self.currentimg.get_height()
        if keys[pygame.K_d]:
            self.x += 0.5
            self.curanimationlist = prightanimationcycle
        elif keys[pygame.K_a]:
            self.x -= 0.5
            self.curanimationlist = pleftanimationcycle

        elif keys[pygame.K_w]:
            self.y -= 0.5
        elif keys[pygame.K_s]:
            self.y += 0.5
        else:
            self.animationframecounty -= 1
            self.animationstep = 0
        self.animationframecounty += 1

        if self.animationframecounty == 50:
            self.animationframecounty = 0
            if self.animationstep < 3:
                self.animationstep += 1
            else:
                self.animationstep = 0
            self.currentimg = self.curanimationlist[self.animationstep]





    def move(self):
        pass


Player1 = Player()

# Main running element
running = True

# Main game loop. If it ends, game stops.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keys pressed list
    keys = pygame.key.get_pressed()

    Player1.update()

    screen.fill((255, 255, 255))
    screen.blit(Player1.currentimg, (Player1.x, Player1.y))


    # Final thing in game loop is always the line to update the display.
    pygame.display.update()
