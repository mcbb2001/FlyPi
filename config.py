from pygame.locals import *
import pygame

pygame.init()

headingMove = pygame.image.load('images/headingdial.png')
headingStatic = pygame.image.load('images/headingref.png')
headingMove = pygame.transform.scale(headingMove,(350,350))
headingStatic = pygame.transform.scale(headingStatic,(500,500))

attitudeMove = pygame.image.load('images/attitudebkgd.png')
attitudeStatic = pygame.image.load('images/attituderef.png')
attitudeBorder = pygame.image.load('images/attitudeborder.png')
attitudeMove = pygame.transform.scale(attitudeMove,(400,960))
attitudeStatic = pygame.transform.scale(attitudeStatic,(500,500))
attitudeBorder = pygame.transform.scale(attitudeBorder,(420,420))

