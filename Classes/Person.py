import pygame as py
import random
class Person():
    def __init__(self, x, y, color,screen):
        self.posx = x
        self.posy = y
        self.screen = screen
        self.color = color
        self.movement_vector =( random.uniform(-1, 1),random.uniform(-1, 1))
        self.rect = py.Rect(self.posx,self.posy,10,10)
    def move(self,factorX , factorY):
        self.posx +=factorX
        self.posy +=factorY
        self.rect = py.Rect(self.posx,self.posy,10,10)
    def draw(self):
        py.draw.rect(self.screen,self.color,self.rect)
    def setColor(self, color):
        self.color = color
        self.draw()
