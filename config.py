from pygame.locals import *
import pygame

pygame.init()

headingMove = pygame.image.load('images/headingdial.png')
headingStatic = pygame.image.load('images/headingref.png')
headingMove = pygame.transform.scale(headingMove,(400,400))
headingStatic = pygame.transform.scale(headingStatic,(400,400))

attitudeMove = pygame.image.load('images/attitudebkgd.png')
attitudeStatic = pygame.image.load('images/attituderef.png')
attitudeBorder = pygame.image.load('images/attitudeborder.png')
attitudeMove = pygame.transform.scale(attitudeMove,(400,960))
attitudeStatic = pygame.transform.scale(attitudeStatic,(400,400))
attitudeBorder = pygame.transform.scale(attitudeBorder,(400,4000))

