import pygame as py

b1 =py.Rect(0,0,600,10)
b2 =py.Rect(0,0,10,600)
b3 =py.Rect(0,590,600,10)
b4 =py.Rect(590,0,10,600)
bordercolor = (200,200,200)

def drawBorders(screen):
    py.draw.rect(screen,bordercolor,b1)
    py.draw.rect(screen,bordercolor,b2)
    py.draw.rect(screen,bordercolor,b3)
    py.draw.rect(screen,bordercolor,b4)
