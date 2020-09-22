import turtle
from random import randint

time = 100000  # количество итераций
N = 5   # количество молекул газа
Vgas = [randint(-10, 10) for i in range(N)]  # задание скоростей молекул
Agas = [randint(0, 360) for f in range(N)]  # задание напралений движения молекул
gas = [turtle.Turtle(shape='circle') for j in range(N)]  # газ
k = 0
for unit in gas:  # повернем все молекулы на начальный угол
    unit.right(Agas[k])
    k += 1
for i in range(time):  # запустим симуляцию
    k = 0  # номер молекулы
    for unit in gas:
        unit.penup()
        unit.forward(Vgas[k])
        x, y = unit.position()
        if y >= 100:  # верхняя граница
            unit.right(2 * Agas[k])
            Agas[k] = 360 - Agas[k]
        if x >= 100:  # правая
            unit.left(180 - 2 * Agas[k])
            Agas[k] = 180 - Agas[k]
        if y <= -100:  # нижняя
            unit.left(2 * Agas[k])
            Agas[k] = 360 - Agas[k]
        if x <= -100:  # левая
            unit.right(180 - 2 * Agas[k])
            Agas[k] = 180 - Agas[k]
        k += 1
