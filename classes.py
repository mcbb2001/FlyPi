from pygame.locals import *
import pygame

pygame.init()

class Instrument():
    def __init__(self,x,y,direct,img):
        self.x = x
        self.y = y
        self.dir = direct
        self.img = img

    def get_rimg(self):
        return pygame.transform.rotate(self.img,self.dir)

    def