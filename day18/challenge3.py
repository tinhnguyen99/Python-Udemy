# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

# draw with random color

from turtle import Turtle, Screen
import random

colorr = ("dark violet", "orange red", "lime green", "medium blue")

timmy = Turtle ()
timmy_s = Screen ()

sides = 3

# have a function to draw a shape when we know sides
def draw_shape(sides, the_turtle):
    for i in range(sides):
        the_turtle.forward(50)
        the_turtle.right(360/sides)

for _ in range(20):
    timmy.color(random.choice(colorr))
    draw_shape(sides, timmy)
    sides += 1






timmy_s.exitonclick()