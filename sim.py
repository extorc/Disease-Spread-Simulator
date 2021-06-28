import pygame as py
from math import sqrt
import random
py.init()

healthy = (100,100,100)
infected = (255,0,0)
res = 600
screen = py.display.set_mode((res,res))
clock = py.time.Clock()
fps_limit = 60

class Person():
    def __init__(self, x, y, color):
        self.posx = x
        self.posy = y
        self.color = color
    def move(self,factorX , factorY):
        self.posx +=factorX
        self.posy +=factorY
    def draw(self):
        py.draw.circle(screen, self.color,(self.posx,self.posy),res/85)
    def setColor(self, color):
        self.color = color
        self.draw()

running = True
people = []
sample_size = 1000
distance = (res-20) / int(sqrt(sample_size))

for y in range(int(sqrt(sample_size))):
    for x in range(int(sqrt(sample_size))):
        people.append(Person((y + 1) * distance,(x + 1) * distance,healthy))

infected_person_x = random.randint(0,int(sqrt(sample_size)))
infected_person_y = random.randint(0,int(sqrt(sample_size)))

people[infected_person_x * infected_person_y].setColor(infected)

while running:
    clock.tick(fps_limit)
    screen.fill((50,50,50))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    for p in people:
        p.draw()
    py.display.flip()

py.quit()
