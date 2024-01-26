# Example file showing a basic pygame "game loop"
from time import sleep
import pygame
from entry import createEntry

BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 800
BLOCKSIZE = 20

def drawGrid():
    for x in range(0, WIDTH, BLOCKSIZE):
        for y in range(0, HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, "white", rect, 1)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
drawGrid()

running = True
coordinates = createEntry(WIDTH / BLOCKSIZE, HEIGHT / BLOCKSIZE)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)
    drawGrid()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()