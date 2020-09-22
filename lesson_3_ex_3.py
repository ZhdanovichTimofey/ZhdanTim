import turtle


def hor(n):
    if n == 1:
        turtle.pendown()
    turtle.forward(20)
    turtle.penup()


def ver(n):
    if n == 1:
        turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()


def dia(n):
    if n == 1:
        turtle.pendown()
    turtle.right(135)
    turtle.forward(29)
    turtle.left(135)
    turtle.penup()


def new(n):
    turtle.goto(30*n, 0)


inp = open('input.txt', 'r')  # считываем данные из файла
s = inp.readline()
inp.close()
s = s.rstrip()
N = [[0] * 9 for i in range(10)]  # список списков, в котором будут содержаться последовательности,задающие каждую цифру
for j in range(10):
    for i in range(9):
        N[j][i] = int(s[i + j * 9])  # Заполняем N данными из файла
turtle.penup()
j = 0
R = [1, 4, 1, 7, 0, 0]     # Список чисел, которые нужно написать
for i in R:
    hor(N[i][0])  # рисует горизонтальную черту, если она необходима в данной цифре
    turtle.goto(30*j, 0)  # переводит черепашку к началу нового элемента
    ver(N[i][1])  # аналогично вертикальную. Все 9 возможных элементов цифр пронумерованы(от 0 до 8)
    turtle.goto(30 * j + 20, 0)
    dia(N[i][2])  # Если данный элемент необходим в цифре, то в кортеже под номером элемента будет 1, иначе 0
    turtle.goto(30 * j + 20, 0)
    ver(N[i][3])
    turtle.goto(30*j, -20)
    hor(N[i][4])
    turtle.goto(30 * j, -20)
    ver(N[i][5])
    turtle.goto(30 * j + 20, -20)
    dia(N[i][6])
    turtle.goto(30 * j + 20, -20)
    ver(N[i][7])
    turtle.goto(30 * j, -40)
    hor(N[i][8])
    j += 1
    new(j)  # переходим к новой цифре
turtle.done()
