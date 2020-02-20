from pygame.locals import *
import pygame
import classes
import config

pygame.init()

crashed = False
bkgd = (198,149,63)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

heading = classes.Instrument(screen,100,100,0,config.headingMove)

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_ESCAPE]:
                crashed = True
    screen.fill(bkgd)
    heading.display()
    pygame.display.update()
    clock.tick(60)

pygame.quit()