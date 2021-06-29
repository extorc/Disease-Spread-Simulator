import pygame as py
from math import sqrt
import random
from Classes.Person import Person
py.init()

healthy = (100,100,100)
infected = (255,0,0)
res =600
screen = py.display.set_mode((res,res))
clock = py.time.Clock()
fps_limit = 40
running = True
people = []
sample_size = 36
distance = (res-20) / int(sqrt(sample_size))
b1 =py.Rect(0,0,600,10)
b2 =py.Rect(0,0,10,600)
b3 =py.Rect(0,590,600,10)
b4 =py.Rect(590,0,10,600)
bordercolor = (200,200,200)

def drawBorders():
    py.draw.rect(screen,bordercolor,b1)
    py.draw.rect(screen,bordercolor,b2)
    py.draw.rect(screen,bordercolor,b3)
    py.draw.rect(screen,bordercolor,b4)

for y in range(int(sqrt(sample_size))):
    for x in range(int(sqrt(sample_size))):
        people.append(Person((y + 1) * distance,(x + 1) * distance,healthy,screen))

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
        if p.rect.colliderect(b1):
            print("top")
        elif p.rect.colliderect(b2):
            print("left")
        elif p.rect.colliderect(b3):
            print("bottom")
        elif p.rect.colliderect(b4):
            print("right")
        for o in people:
            if o.color == infected:
                if o.posx != p.posx and o.posy != p.posy:
                    if o.rect.colliderect(p.rect):
                        o.color = p.color = infected
                        p.draw()
                        o.draw()
    drawBorders()

    py.display.flip()

py.quit()
