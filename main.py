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


class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.currentimg = PlayerRight1
        self.xoffset = self.currentimg.get_width()
        self.yoffset = self.currentimg.get_height()

    def update(self):
        self.xoffset = self.currentimg.get_width()
        self.yoffset = self.currentimg.get_height()
        print(keys)

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
