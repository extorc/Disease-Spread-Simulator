import pygame as py
import random
from math import sqrt

class Person():
    def __init__(self, x, y, color,screen):
        self.posx = x
        self.size = 6
        self.posy = y
        self.screen = screen
        self.color = color
        self.movement_vector =[random.uniform(-1, 1),random.uniform(-1, 1) ]
        self.rect = py.Rect(self.posx,self.posy,self.size,self.size)
        self.infectedLast = False
        self.infectionTime =random.randint(100,200)
    def move(self,factorX , factorY):
        self.posx +=factorX
        self.posy +=factorY
        self.rect = py.Rect(self.posx,self.posy,self.size,self.size)
    def draw(self):
        py.draw.rect(self.screen,self.color,self.rect)
    def setColor(self, color):
        self.color = color
        self.draw()

def infect_random_person(sample_size,people,color):
    infected_person_x = random.randint(0,int(sqrt(sample_size)))
    infected_person_y = random.randint(0,int(sqrt(sample_size)))
    people[infected_person_x * infected_person_y - 1].setColor(color)
