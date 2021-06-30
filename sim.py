import pygame as py
from math import sqrt
import random
from Classes.Person import Person
import matplotlib.pyplot as plt
py.init()

healthy = (100,100,100)
infected = (255,0,0)
res =600
screen = py.display.set_mode((res,res))
clock = py.time.Clock()
fps_limit = 40
running = True
people = []
sample_size = 400
distance = (res-300) / int(sqrt(sample_size))
b1 =py.Rect(0,0,600,10)
b2 =py.Rect(0,0,10,600)
b3 =py.Rect(0,590,600,10)
b4 =py.Rect(590,0,10,600)
bordercolor = (200,200,200)
time = 0
inf_plot = []
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
status = []
all_infected = False
d_infected = 0
prev_inf = 0
inf = 0
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
            # print("top")
            p.movement_vector[1]  = p.movement_vector[1] * -1
        elif p.rect.colliderect(b2):
            # print("left")
            p.movement_vector[0]  = p.movement_vector[0] * -1
        elif p.rect.colliderect(b3):
            # print("bottom")
            p.movement_vector[1]  = p.movement_vector[1] * -1
        elif p.rect.colliderect(b4):
            # print("right")
            p.movement_vector[0]  = p.movement_vector[0] * -1
        for o in people:
            if o.color == infected:
                if o.posx != p.posx and o.posy != p.posy:
                    if o.rect.colliderect(p.rect):
                        if o.spreadProbability > 0:
                            o.color = p.color = infected
                            o.spreadProbability -= 1
                            p.draw()
                            o.draw()

    drawBorders()

    for p in people:
        if p.color == infected:
            p.infectionTime +=1
            if p.infectionTime >= 100:
                p.setColor(healthy)
            inf += 1

    # print(inf)
    if prev_inf == inf:
        d_infected += 1
    else:
        d_infected = 0
    if d_infected > 100:
        print("All Infected")
        break
    # print(d_infected)
    prev_inf = inf
    time += 1
    print(d_infected,inf,time)
    inf_plot.append(inf)
    py.display.flip()
    inf = 0
plt.plot(inf_plot)
plt.show()
py.quit()
