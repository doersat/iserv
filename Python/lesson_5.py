# proizNum = 1 #Произведение чисел
# userInput = 1 #Вводимое число юзером
# while userInput != 0:
#     proizNum *= userInput
#     print("Введите 0 чтобы остановить программу")
#     userInput = int(input("Или введите число: "))
# print("Произведение ваших чисел равно", proizNum)

# for i in range (1, 101):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i, end = " ")

# st = "Мы используем индексы в этом примере"
# print(st [-1])
# print(st[-7: -1])
# print(st[:-13])
# print(st[-13:])
# print(st[::-1])


# st = "Кто владеет информацией, тот владеет миром!" 

# len_st = len(st)
# new_st1 = st.title()
# new_st3 = st.replace("информацией", "python")
# new_st4 = st.upper()
# count_o = st.count("о")
# print(st)
# print(len_st)
# print(new_st1)
# print(new_st3)
# print(new_st4)
# print(count_o)

# st = input()
# a = int(input())
# b = int(input())
# print(st[a:b])

# a = input()
# print(a[:: -1])
# if a == a[::-1]:
#     print("Слово палиндром")

a = input()
new_a = a.replace(",", " ")
new_a2 = a.replace(".", " ")
new_a3 = a.replace("!", " ")
new_a4 = a.replace("?", " ")
new_a5 = a.replace("...", " ")
new_a6 = a.replace(";", " ")
new_a7 = a.replace(":", " ")
print(new_a)
print(new_a2)
print(new_a3)
print(new_a4)
print(new_a5)
print(new_a6)
print(new_a7) 