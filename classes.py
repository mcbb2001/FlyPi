from pygame.locals import *
import pygame

pygame.init()



class Instrument():
    def __init__(self,screen,x,y,direct,img):
        self.screen = screen
        self.x = x
        self.y = y
        self.dir = direct
        self.img = img

    def get_rimg(self):
        return pygame.transform.rotate(self.img,self.dir)

    def display(self):
        img = self.get_rimg()
        x = int(self.x-(img.get_width())/2)
        y = int(self.y-(img.get_height())/2)
        self.screen.blit(img,(x,y))