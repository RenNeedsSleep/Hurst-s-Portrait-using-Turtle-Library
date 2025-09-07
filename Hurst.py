from idlelib.colorizer import color_config

'''Below is a method i used to extract colours from an already uploaded
 Hurst potrait to make the colour selection more authentic.'''
#import colorgram

#colors = colorgram.extract('hurst.jpeg',30)
#for i in range(len(colors)):
#    new_color = colors[i]
#    rgb = new_color.rgb
#    r = rgb.r
#    g = rgb.g
#    b = rgb.b
#    tuple = (r,g,b)
#    colour_list.append(tuple)
#
#print(colour_list)

from turtle import Screen
import turtle as t
import random

galelio = t.Turtle()
screen = Screen()

t.colormode(255)
galelio.speed("fastest")

colour_list = [(230, 233, 239), (239, 231, 235), (228, 235, 231), (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]

galelio.pu()
galelio.setpos(-200,-200)
galelio.pd()

y = -200

for j in range(10):
    for i in range(10):
            galelio.color(random.choice(colour_list))
            galelio.dot(20)
            galelio.pu()
            galelio.forward(50)
            galelio.pd()
    galelio.pu()
    galelio.setpos(-200,y)
    galelio.left(90)
    galelio.forward(50)
    galelio.right(90)
    y += 50


screen.exitonclick()