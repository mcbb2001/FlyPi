from pygame.locals import *
import pygame
import classes
import config

pygame.init()

crashed = False
bkgd = (198,149,63)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

heading = classes.Instrument(screen,1500,1000,10,config.headingStatic,config.headingMove)

attitude = classes.Horizon(screen,2500,1000,0,0,config.attitudeStatic,config.attitudeMove,config.attitudeBorder)

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_ESCAPE]:
                crashed = True
    screen.fill(bkgd)
    attitude.display()
    heading.display()
    pygame.display.update()
    clock.tick(60)

pygame.quit()