import pygame as py
from math import sqrt
import random
from Classes.Person import Person
import matplotlib.pyplot as plt
from Classes.Borders import drawBorders , b1, b2, b3, b4
py.init()

healthy = (100,100,100)
infected = (255,0,0)
res =600
screen = py.display.set_mode((res,res))
clock = py.time.Clock()
fps_limit = 40
running = True
people = []
sample_size = 225
distance = (res-100) / int(sqrt(sample_size))
time = 0

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
inf_plot = []
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
                if p.color == healthy:
                    if o.rect.colliderect(p.rect):
                        o.color = p.color = infected
                        p.draw()
                        o.draw()


    drawBorders(screen)
    for p in people:
        if p.color == infected:
            p.infectionTime -= 1
            # print(p.infectionTime)
            if p.infectionTime <= 0:
                p.color = healthy
                p.infectionTime = random.randint(50,150)
            else:
                inf += 1

    if prev_inf == inf:
        d_infected += 1
    else:
        d_infected = 0
    if d_infected > 100:
        print("All Infected")
        break

    prev_inf = inf
    time += 1
    print(d_infected,inf,time)
    inf_plot.append(inf)
    py.display.flip()
    inf = 0

plt.plot(inf_plot)
plt.show()
py.quit()
