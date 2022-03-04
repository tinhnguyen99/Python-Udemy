# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image.jpg', 30)
colors_rgb = []

for color_temp in colors:
    r = color_temp.rgb.r
    g = color_temp.rgb.g
    b = color_temp.rgb.b

    colors_rgb.append((r, g, b))

timmy = Turtle()
timmy_s = Screen()
timmy_s.colormode(255)
timmy.hideturtle()

current_pos = ()

current_pos = timmy.position()
timmy.penup()
timmy.setposition(current_pos[0] - 100, current_pos[1] - 100)
for i in range(10):
    current_pos = timmy.position()
    for i in range(10):
        timmy.dot(20, random.choice(colors_rgb))
        timmy.forward(50)
    timmy.setposition(current_pos[0], current_pos[1] + 50)


timmy_s.exitonclick()
