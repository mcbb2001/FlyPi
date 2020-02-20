from pygame.locals import *
import pygame

pygame.init()

headingMove = pygame.image.load('images/headingdial.png')
headingStatic = pygame.image.load('images/headingref.png')
headingMove = pygame.transform.scale(headingMove,(100,100))

