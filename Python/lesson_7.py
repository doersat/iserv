import random
import math
import string

#Функции


#def - определить, в -> () пишутся параметры
#Чаще всего функции называют глаголами 
#Вернуть это return
#Вывести это print


# def sum_squares_nums(lst):            
#     new_lst = []
#     for i in lst:
#         new_lst.append(i ** 2)
#     result = sum(new_lst)
#     return result


# lst1 = [23, 57, 13, 67, 75]
# result1 = sum_squares_nums(lst1)
# print(result1)

# lst2 = [14, 49, 6, 64]
# result2 = sum_squares_nums(lst1)
# print(result2)

# lst3 = [8, 90, 55, 83, 1, 22]
# result3 = sum_squares_nums(lst1)
# print(result3)


#функия с параманетрами
# def exam_result(russian, math, informatics):
#     total = russian + math + informatics

#     if 0 <= total and total <= 120:
#         print('Плохо')
#     elif 121 <= total and total <= 210:
#         print('Хорошо')
#     elif 211 <= total and total <= 300:
#         print('Отлично')
#     else:
#         print('Введены некорректные данные!')
# exam_result = [67, 77, 80]




#Задача №1 создание пароля
# def password_generaniot(lenPas, iSnums, isUpAlpha):
#     symbols = string.ascii_lowercase
#     password = ""
#     if isUpAlpha:
#         symbols += string.ascii_uppercase
#     if iSnums:
#         symbols += '1234567890'
#     for _ in range(lenPas):
#         password += random.choice(symbols)
#     return password


# print("---Программа для генерации пароля---")
# lenPas = int(input("Введите длину пароля: "))
# isNums  = input("Нужны ли цифры в пароле Y/n: ")
# isUpAlpha  = input("Нужны ли в большие буквы в пароле? Y/n: ")

# if isNums.lower() == "y":
#     isNums = True
# else:
#     isNums = False
# if isUpAlpha.lower() == "y":
#     isUpAlpha = True
# else:
#     isNums = False
# password = password_generaniot(lenPas, isNums, isUpAlpha)
# print(password)


#Задание №1.1
# def IsEven(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# num = int(input("Введите ваше число: "))
# if(IsEven(num)):
#     print("Число чётное")
# else:
#     print("Число не четное")

# #Задания 1.2
# def CountGlassSymbols(text):
#     glassSymbol = "аеёиоуыэюя"
#     count = 0
#     for i in text:
#         if glassSymbol.find(1) != -1:
#             count += 1
#     return count
# string = "Всем привет я крутая строка!"
# print(f"В строке \"{string}\" {CountGlassSymbols(string)} гласных букв")


#Задание 1.3
# def SumOfDigits(number):
#     strNum = str(number)
#     sumDigits = 0
#     for i in strNum:
#         sumDigits += int(i)
#     return sumDigits
# print(f"Сумма цифр в числе 1234 равна {SumOfDigits(1234)}")
