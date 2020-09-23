import turtle
from random import randint

time = 100000  # количество итераций
N = 5   # количество молекул газа
gas = [turtle.Turtle(shape='circle') for j in range(N)]  # газ
turtle.hideturtle()
k = 0
for unit in gas:  # повернем все молекулы на начальный угол
    unit.left(randint(0, 360))
for i in range(time):  # запустим симуляцию
    k = 0  # номер молекулы
    for unit in gas:
        unit.penup()
        unit.forward(10)
        if abs(unit.xcor()) > 100:
            unit.seth(180 - unit.heading())
        if abs(unit.ycor()) > 100:
            unit.seth(360 - unit.heading())
        k += 1
