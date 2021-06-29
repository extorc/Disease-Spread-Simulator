import pygame as py
from math import sqrt
import random
py.init()

healthy = (100,100,100)
infected = (255,0,0)
res =600
screen = py.display.set_mode((res,res))
clock = py.time.Clock()
fps_limit = 40
def drawBorders():
    py.draw.rect(screen,(200,200,200),(0,0,600,10))
    py.draw.rect(screen,(200,200,200),(0,0,10,600))
    py.draw.rect(screen,(200,200,200),(0,590,600,10))
    py.draw.rect(screen,(200,200,200),(590,0,10,600))
class Person():
    def __init__(self, x, y, color):
        self.posx = x
        self.posy = y
        self.color = color
        self.movement_vector =( random.uniform(-1, 1),random.uniform(-1, 1))
        self.rect = py.Rect(self.posx,self.posy,10,10)
    def move(self,factorX , factorY):
        self.posx +=factorX
        self.posy +=factorY
        self.rect = py.Rect(self.posx,self.posy,10,10)
    def draw(self):
        py.draw.rect(screen,self.color,self.rect)
    def setColor(self, color):
        self.color = color
        self.draw()

running = True
people = []
sample_size = 100
distance = (res-20) / int(sqrt(sample_size))

for y in range(int(sqrt(sample_size))):
    for x in range(int(sqrt(sample_size))):
        people.append(Person((y + 1) * distance,(x + 1) * distance,healthy))

infected_person_x = random.randint(0,int(sqrt(sample_size)))
infected_person_y = random.randint(0,int(sqrt(sample_size)))

people[infected_person_x * infected_person_y - 1].setColor(infected)

while running:
    clock.tick(fps_limit)
    screen.fill((50,50,50))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    for p in people:
        p.move(p.movement_vector[0] * 2,p.movement_vector[1] * 2)
        p.draw()
        for o in people:
            if o.color == infected:
                if o.posx != p.posx and o.posy != p.posy:
                    if o.rect.colliderect(p.rect):
                        print("collided")
                        o.color = p.color = infected
                        p.draw()
                        o.draw()
    drawBorders()

    py.display.flip()

py.quit()
