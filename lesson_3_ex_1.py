import turtle
from random import *

R = 40  # максимально возможная длина шага
for i in range(100000):
    n = random()  # часть полного круга, на которую повернется черепашка
    r = random()  # часть максимально возможной длины шага, которую пройдет черепашка
    turtle.forward(R * r)
    turtle.right(n * 360)
turtle.done()
