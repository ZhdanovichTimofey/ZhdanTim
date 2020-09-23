import turtle


def hor(n, l1):
    if n == 1:
        turtle.pendown()
    turtle.forward(l1)
    turtle.penup()


def ver(n, l1):
    if n == 1:
        turtle.pendown()
    turtle.right(90)
    turtle.forward(l1)
    turtle.left(90)
    turtle.penup()


def dia(n, l2):
    if n == 1:
        turtle.pendown()
    turtle.right(135)
    turtle.forward(l2)
    turtle.left(135)
    turtle.penup()


def new(n, ls):
    turtle.goto(ls * n, 0)


def number(i, j):
    hor(N[i][0], length_1)  # рисует горизонтальную черту, если она необходима в данной цифре
    turtle.goto(length_s * j, 0)  # переводит черепашку к началу нового элемента
    ver(N[i][1], length_1)  # аналогично вертикальную. Все 9 возможных элементов цифр пронумерованы(от 0 до 8)
    turtle.goto(length_s * j + length_1, 0)
    dia(N[i][2], length_2)  # Если данный элемент необходим в цифре, то в кортеже под номером элемента будет 1, иначе 0
    turtle.goto(length_s * j + length_1, 0)
    ver(N[i][3], length_1)
    turtle.goto(length_s * j, -length_1)
    hor(N[i][4], length_1)
    turtle.goto(length_s * j, -length_1)
    ver(N[i][5], length_1)
    turtle.goto(length_s * j + length_1, -length_1)
    dia(N[i][6], length_2)
    turtle.goto(length_s * j + length_1, -length_1)
    ver(N[i][7], length_1)
    turtle.goto(length_s * j, -2 * length_1)
    hor(N[i][8], length_1)
    j += 1
    new(j, length_s)  # переходим к новой цифре


N0 = (1, 1, 0, 1, 0, 1, 0, 1, 1)  # кортежи, задающие написание каждой цифры от 0 до 9
N1 = (0, 0, 1, 1, 0, 0, 0, 1, 0)
N2 = (1, 0, 0, 1, 0, 0, 1, 0, 1)
N3 = (1, 0, 1, 0, 1, 0, 1, 0, 0)
N4 = (0, 1, 0, 1, 1, 0, 0, 1, 0)
N5 = (1, 1, 0, 0, 1, 0, 0, 1, 1)
N6 = (0, 0, 1, 0, 1, 1, 0, 1, 1)
N7 = (1, 0, 1, 0, 0, 1, 0, 0, 0)
N8 = (1, 1, 0, 1, 1, 1, 0, 1, 1)
N9 = (1, 1, 0, 1, 1, 0, 1, 0, 0)
N = [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9]  # список всех цифр
turtle.penup()
k = 0  # номер позиции цифры
length_1 = 20  # длина горизонтального и вертикального элементов цифры индекса
length_2 = round(length_1 * 2**(1/2))  # длина диагонального элемента
length_s = 30  # ширина цифры в сумме с пробелом после неё
R = [1, 4, 1, 7, 0, 0]     # Список чисел, которые нужно написать
for i in R:
    k += 1
    number(i, k)  # рисуем цифру i
turtle.done()
