import pygame as py
from math import sqrt
import random
from Classes.Person import Person , infect_random_person
import matplotlib.pyplot as plt
from Classes.Borders import drawBorders , b1, b2, b3, b4
from Classes.Colors import *

class Sim:
    def __init__(self,resolution,fps,ss):
        py.init()
        self.res = resolution #screen res
        self.fps_limit = fps  #cycles speed
        self.sample_size = ss #number of people
        self.screen = py.display.set_mode((self.res,self.res))
        self.clock = py.time.Clock()
        self.running = True
        self.people = []
        self.distance = (self.res-100) / int(sqrt(self.sample_size)) #inital distance between people
        self.time = 0
        self.all_infected = False
        self.d_infected = 0
        self.prev_inf = 0
        self.inf = 0
        self.inf_plot = []

    def create_population(self):
        for y in range(int(sqrt(self.sample_size))):
            for x in range(int(sqrt(self.sample_size))):
                self.people.append(Person((y + 1) * self.distance,(x + 1) * self.distance,healthy,self.screen))
                #create population classes
        infect_random_person(self.sample_size,self.people,infected)

    def start_sim(self):
        while self.running:
            self.clock.tick(self.fps_limit)
            self.screen.fill(background)
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
            drawBorders(self.screen)
            for p in self.people:
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
                for o in self.people:
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
                        self.inf += 1

            if self.prev_inf == self.inf:
                self.d_infected += 1
            else:
                self.d_infected = 0
            if self.d_infected > 100:
                print("No More Infections")
                break

            self.prev_inf = self.inf
            self.time += 1
            print(self.d_infected,self.inf,self.time)
            self.inf_plot.append(self.inf)
            py.display.flip()
            self.inf = 0

    def end_plot(self):
        plt.plot(self.inf_plot)
        plt.show()
        py.quit()
