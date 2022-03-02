# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy_s = Screen()

timmy_s.colormode(255)
timmy.pensize(5)
timmy.speed(10.5)


def draw_circle(size_of_sides):
    heading = 0
    for _ in range(int(size_of_sides)):
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)
        timmy.setheading(heading)
        timmy.color((red, blue, green))
        timmy.circle(100)
        heading += 360/size_of_sides

draw_circle(50)


timmy_s.exitonclick()
