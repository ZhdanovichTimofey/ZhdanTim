import turtle
from random import randint

Vy0 = 10  # начальная скорость по OY
Vx = 1  # начальная скорость по OX
ay = -1  # ускорение по OY
dt = 1
Vy = Vy0
x, y = 0, 0
for t in range(1000):
    turtle.speed(round((Vx**2 + Vy**2)**1/2))  # скорость черепашки
    x = round(x + Vx*dt)
    y = round(y + Vy*dt)
    Vy = Vy + ay*dt  # скорость по OY
    if y <= 0:
        Vy = Vy0
    turtle.goto(x, y)
