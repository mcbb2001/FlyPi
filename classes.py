from pygame.locals import *
import pygame

pygame.init()



class Instrument():
    def __init__(self,screen,x,y,direct,statimg,movimg):
        self.screen = screen
        self.x = x
        self.y = y
        self.dir = direct
        self.statimg = statimg
        self.movimg = movimg
        self.width = self.get_rimg().get_width()
        self.height = self.get_rimg().get_height()

    def get_rimg(self):
        return pygame.transform.rotate(self.movimg,self.dir)

    def display(self):
        img = self.get_rimg()
        x = int(self.x-(img.get_width())/2)
        y = int(self.y-(img.get_height())/2)
        pygame.draw.rect(self.screen,(33,28,10),(x-50,y-50,self.width+100,self.height+100))
        self.screen.blit(img,(x,y))
        self.screen.blit(self.statimg,(self.x-self.statimg.get_width()/2,self.y-self.statimg.get_height()/2))

class Horizon(Instrument):
    def __init__(self,screen,x,y,direct,yaw,statimg,movimg,bordimg):
        self.border = bordimg
        self.yaw = yaw
        super(Horizon,self).__init__(screen,x,y,direct,statimg,movimg)

    def display(self):
        super(Horizon,self).display()
        self.screen.blit(self.border,(self.x-self.border.get_width()/2,self.y-self.border.get_height()/2))