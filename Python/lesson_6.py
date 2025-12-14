import math
import random
import turtle

#Работа с библиотекой math


# part_1_1 = math.cos(math.pi/3) + math.log2(16)
# part_1_2 = sum([math.factorial(n) + 1 for n in range(0,4)])
# part_1 = part_1_1 * part_1_2
# print(part_1)

# part_2 = (math.sqrt(25) - abs(-5) ** math.sin(math.pi/2))  sqrt - квадратный корень   abs - модуль
# part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)

# resulte = part_1, part_2, part_3
# print(resulte)

# for i in range(5):
#     rand_num = random.randint(1, 101)
#     print(rand_num)

# for i in range(5):
#     rand1_num = random.uniform(1, 10)
#     print(rand1_num)

# sp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.choice(sp))
# life = 5
# rand_num = random.randint(1, 50)
# isWin = False
# print("Было загадано число от 1 до 50. Попробуй отгадать!")
# while life != 0:
#     num = int(input("Введите число: "))
#     if num == rand_num:
#         print("Вы победили!")
#         isWin = True
#         break
#     elif num < rand_num:
#         print("Загаданое число больше")
#         life -= 1
#     elif num > rand_num:
#         print("Загаданое число меньше")
#         life -= 1
# print("Ну и лох :>")


screen = turtle.Screen()
screen.setup(600, 900)
screen.bgcolor("lightblue")
screen.title("Весёлый смайлик изучаем Turtle")

t = turtle.Turtle()
t.speed(5)
t.width(3)

t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-40, 40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(40, 40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()


t.penup()
t.goto(-60, -20)
t.pendown()
t.color("black")
t.width(5)
t.setheading(-60)
t.circle(70, 120)

t.hideturtle()
screen.exitonclick()