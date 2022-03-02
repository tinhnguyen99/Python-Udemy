# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy_s = Screen()

timmy_s.colormode(255)
timmy.pensize(20)
angle = [0, 90, 180, 270]

for _ in range(100):
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    timmy.color((red, blue, green))
    timmy.forward(50)
    timmy.setheading(random.choice(angle))


timmy_s.exitonclick()
