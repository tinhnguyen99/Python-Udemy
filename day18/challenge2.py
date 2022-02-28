# Tinh Nguyen <tinh.nguyentrung1999@gmail.com>

from turtle import Turtle, Screen

timmy = Turtle()
timmy_s = Screen()


for _ in range(6):
    timmy.forward(5)
    timmy.penup()
    current_pos = timmy.pos()
    timmy.setpos(current_pos[0] + 20, current_pos[1])
    timmy.pendown()




timmy_s.exitonclick()


