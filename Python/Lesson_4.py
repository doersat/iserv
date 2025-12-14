# age = 0

# while age < 18:
#     print(f"Мне {age} лет. Я ребёнок!")
#     age += 1
# print("Уезжаю от родителей")

# 1 = 0
# while 1 < 5:
#     print("Привет")
#     1 += 1


#Задача №1
# a = 1
# b = "фывапол"
# while a < 11:
#     print(b)
#     a += 1

#Задача №2
# p = 20 #price
# aM = 110 #all money
# while aM >= p:
#     print("Вы купили товар")
#     aM -= p
#     print(f"У вас осталось: {aM}")
# print("Ну лох, деньги кончались")
    

#Задача 3
# print(" Игра -  отгадай число котрое я загадалa\n")
# rN = 5 #рандомное число
# iN = int(input("Угадай число которое я загадал (1-10): ")) #Вводимое число
# while rN != iN:
#     if iN < rN:
#         print("Ну близка")
#     else:
#         print("Ну далеко")
#     print("Это не верное число")
#     iN = int(input("Попробуй еще раз: ")) #Вводимое число
    

# print("Поздравляю ты отгадал")

# for i in range(0, 51):
#     print(i)

#Задача №4
summa = 0
a = int(input("Введите число: "))
for i in range(1, a +1):
    summa += 1
print(summa)