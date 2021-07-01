import pygame as py
from math import sqrt
import random
from Classes.Person import Person , infect_random_person
import matplotlib.pyplot as plt
from Classes.Borders import drawBorders , b1, b2, b3, b4
from Classes.Colors import *

py.init()

res =600
screen = py.display.set_mode((res,res))
clock = py.time.Clock()
fps_limit = 40
running = True
people = []
sample_size = 225
distance = (res-100) / int(sqrt(sample_size))
time = 0
all_infected = False
d_infected = 0
prev_inf = 0
inf = 0
inf_plot = []

for y in range(int(sqrt(sample_size))):
    for x in range(int(sqrt(sample_size))):
        people.append(Person((y + 1) * distance,(x + 1) * distance,healthy,screen))

infect_random_person(sample_size,people,infected)

while running:
    clock.tick(fps_limit)
    screen.fill(background)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    drawBorders(screen)
    for p in people:
        p.move(p.movement_vector[0] * 2,p.movement_vector[1] * 2)
        p.draw()
        if p.rect.colliderect(b1):
            p.movement_vector[1]  = p.movement_vector[1] * -1
        elif p.rect.colliderect(b2):
            p.movement_vector[0]  = p.movement_vector[0] * -1
        elif p.rect.colliderect(b3):
            p.movement_vector[1]  = p.movement_vector[1] * -1
        elif p.rect.colliderect(b4):
            p.movement_vector[0]  = p.movement_vector[0] * -1
        for o in people:
            if o.color == infected:
                if p.color == healthy:
                    if o.rect.colliderect(p.rect):
                        o.color = p.color = infected
                        p.draw()
                        o.draw()

        if p.color == infected:
            p.infectionTime -= 1
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
        print("No More Infections")
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
