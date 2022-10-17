# name = input("Ваше имя?\n")
# age_str = input("Ваш возраст?\n")
# age = int(age_str)
#
# print(name, age)
#
# # Задание 1
# count_str = input("Сколько чашек кофе желаете приобрести?\n")
# count = int(count_str)
#
# bonus = int(count / 6)
#
# print(bonus)
#
# # Задание 2
# import math
#
# x1 = float(input("введите значение 'X' координаты первой точки \n"))
# y1 = float(input("введите значение 'Y' координаты первой точки \n"))
#
# x2 = float(input("введите значение 'X' координаты второй точки \n"))
# y2 = float(input("введите значение 'Y' координаты второй точки \n"))
#
# d = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)
#
# print("Расстояние между координатами: ", d)
#
# # Задание 3
# chicken = int(input("Введите количество кур\n")) * 2
# pig = int(input("Введите количество свиней\n")) * 4
# cow = int(input("Введите количество коров\n")) * 4
#
# summ = chicken + pig + cow
#
# print(summ)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Циклы ДЗ-1-2
# # Задание 1
# # Вариант 1
# num = int(input('Введите число, количество символов \'*\'\n'))
# start_number = 1
# while num != 0:
#     print(start_number * '*')
#     num -= 1
#     start_number += 1
#
# # Вариант 2
# num = int(input('Введите число, количество символов \'*\'\n'))
# for x in range (0, num):
#     print('*' * (x + 1))
#
# # Вариант 3
# for x in range(1, 8):
#     print(x * "*")
#
# # Задание 2
# # Вариант 1
# num = int(input('Введите число:\n')) + 1
# start_number = 0
# while num != 0:
#     if num % 2 == 0:
#         print(f'{start_number} is EVEN')
#     else:
#         print(f'{start_number} is ODD')
#     num -= 1
#     start_number += 1
# # Вариант 2
# num = int(input('Введите число:\n'))
# start_number = 0
# for x in range(num + 1):
#     if num % 2 == 0:
#         print(f'{start_number} is EVEN')
#     else:
#         print(f'{start_number} is ODD')
#     num -= 1
#     start_number += 1
#
# # Вариант 3
# num = int(input('Введите число:\n'))
# for x in range(num + 1):
#     if num % 2 == 0:
#         print(f'{x} is EVEN')
#     else:
#         print(f'{x} is ODD')
#     num -= 1
#     x += 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Циклы ДЗ-3 Division by 3 or 5
# # Вариант 1
# limit = int(input('Введите число:\n'))
# sum = 0
# for x in range(0, limit + 1):
#     if x % 3 == 0 or x % 5 == 0:
#         sum += x
#     else:
#         continue
# print(sum)
# # Вариант 2
# limit = int(input('Введите число:\n'))
# list_numbers = [x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0]
# total_sum = 0
# for y in list_numbers:
#     total_sum += y
# print(total_sum)
# # Вариант 3
# limit = int(input('Введите число:\n'))
# total_sum = sum([x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0])
# print(total_sum)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Циклы ДЗ-4 Joined List
# # Вариант 1
# joined_list = []
# first_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# second_lst = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
# for x in first_lst:
#     if x % 2 != 0:
#         joined_list.append(x)
#     else:
#         continue
# for x in second_lst:
#     if x % 2 == 0:
#         joined_list.append(x)
#     else:
#         continue
# print(joined_list)
# # # Вариант 2
# first_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# second_lst = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
# first_new_list = [x for x in first_lst if x % 2 != 0]
# second_new_list = [x for x in second_lst if x % 2 == 0]
# joined_list = first_new_list + second_new_list
# print(joined_list)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Циклы ДЗ-5 Joined List
# # Вариант 1
# weight_of_cards = {
#              2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
#              7: 0,  8: 0,  9: 0,
#              10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
#              }
# current_hand = [2, 3, 4, 10, 'Q', 5]
# cards_sum = 0
# for x in current_hand:
#     cards_sum += weight_of_cards[x]
# print(f'Weight of current cards is: {cards_sum}')
# # Вариант 2
# weight_of_cards = {
#              2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
#              7: 0,  8: 0,  9: 0,
#              10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
#              }
# current_hand = [2, 3, 4, 10, 'Q', 5]
# cards_sum = sum([weight_of_cards.get(x) for x in current_hand])
# print(f'Weight of current cards is: {cards_sum}')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Циклы ДЗ-6 - Определяем Flush
# table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
# hand_cards = ["J_D", "3_D"]
# all_cards = table_cards + hand_cards
#
# suit = [x[-1] for x in all_cards]
# if suit.count("S") >= 5:
#     print("Flush!")
# elif suit.count("H") >= 5:
#     print("Flush!")
# elif suit.count("D") >= 5:
#     print("Flush!")
# elif suit.count("C") >= 5:
#     print("Flush!")
# else:
#     print("No Flush!")
#
# # S - пики (spades)
# # H - червы (hearts)
# # D - буби (diamonds)
# # C - трефы (clubs)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Циклы ДЗ-7 - Палиндром
# # Вариант 1
# number = int(input("Введите число: "))
# len_of_number = len(str(number))
# while len_of_number > 1:
#     a = number // 10**(len_of_number - 1)  # первое число
#     b = number % 10  # последнее число
#     if a == b:
#         number = (number - a * 10**(len_of_number - 1)) // 10  # отрезаем первое и последнее числа
#         len_of_number -= 2
#         if len_of_number == 0 or len_of_number == 1:
#             print("Palindrome")
#     else:
#         print("No Palindrome")
#         break
# # Вариант 2
# number = int(input("Введите число: "))
# reversed_number = 0
# tmp_original = number
# while tmp_original > 0:
#     reversed_number = (reversed_number * 10) + tmp_original % 10
#     tmp_original = tmp_original // 10
# if number == reversed_number:
#     print("Palindrome")
# else:
#     print("No Palindrome")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задание - Угадай число.
# import random
# secret_number = random.randint(1, 50)
# your_number = int(input("Enter your number from 1 to 50: "))
# count = 5
# while count > 0:
#     if your_number == secret_number:
#         print("Congratulations! You are winner!")
#         break
#     elif your_number > secret_number:
#         print("Your number is more than computer number")
#         your_number = int(input("Enter your number from 1 to 50: "))
#         count -= 1
#         if your_number == secret_number:
#             print("Congratulations! You are winner!")
#         elif count == 0:
#             print(f"You are loser! My number was : {secret_number}")
#         else:
#             continue
#     elif your_number < secret_number:
#         print("Your number is less than computer number")
#         your_number = int(input("Enter your number from 1 to 50: "))
#         count -= 1
#         if your_number == secret_number:
#             print("Congratulations! You are winner!")
#         elif count == 0:
#             print(f"You are loser! My number was : {secret_number}")
#         else:
#             continue
#     else:
#         print("Mistake")
#         break
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задание - Игра - камни (R - rock), ножницы (S - scissors), бумага (P - paper).
# import random
# while exit != "no":
#     pc_choice = random.choice("RSP")
#     human_choice = input("Enter your choice - R - rock, or S - scissors, or P - paper: ").upper()
#     if human_choice == "R" or human_choice == "S" or human_choice == "P":
#         win_combinations =[("P", "S"), ("S", "R"), ("P", "S")]
#         if (pc_choice, human_choice) in win_combinations:
#             print(f"Congratulation! You are win! My choice was {pc_choice}")
#             temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#             if temp_exit == "yes":
#                 continue
#             elif temp_exit == "no":
#                 exit = temp_exit
#                 print("See you! Goodbye!")
#                 break
#             else:
#                 print("I don't understand you. Repeat please")
#                 temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#                 while temp_exit != "yes" or temp_exit != "no":
#                     if temp_exit == "yes":
#                         break
#                     elif temp_exit == "no":
#                         exit = temp_exit
#                         print("See you! Goodbye!")
#                         break
#                     else:
#                         print("I don't understand you. Repeat please")
#                         temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#         elif pc_choice == human_choice:
#             print("A draw! PC has the same element!")
#             temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#             if temp_exit == "yes":
#                 continue
#             elif temp_exit == "no":
#                 exit = temp_exit
#                 print("See you! Goodbye!")
#                 break
#             else:
#                 print("I don't understand you. Repeat please")
#                 temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#                 while temp_exit != "yes" or temp_exit != "no":
#                     if temp_exit == "yes":
#                         break
#                     elif temp_exit == "no":
#                         exit = temp_exit
#                         print("See you! Goodbye!")
#                         break
#                     else:
#                         print("I don't understand you. Repeat please")
#                         temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#         else:
#             print(f"You aren't win. My choice was {pc_choice}")
#             temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#             while temp_exit != "yes" or temp_exit != "no":
#                 if temp_exit == "yes":
#                     break
#                 elif temp_exit == "no":
#                     exit = temp_exit
#                     print("See you! Goodbye!")
#                     break
#                 else:
#                     print("I don't understand you. Repeat please")
#                     temp_exit = input(str("Do you want to try else? Yes or No? ")).lower()
#
#
#
#     else:
#         print("Mistake, try to enter your choice!")
#         continue
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Программа получения цифр трёхзначного числа
# num = 754
# a = num % 10  # получение последнего числа
# b = (num % 100) // 10  # получаем сначала два последних числа, затем первое из двух
# c = num // 100  # получаем первое число
# print(a)
# print(b)
# print(c)
# Алгоритм получения цифр из n-значного числа
# Последняя цифра - (num % pow(10, 1)) // pow(10, 0)
# Предпоследняя цифра - (num % pow(10, 2)) // pow(10, 1)
# Предпредпоследняя цифра - (num % pow(10, 3)) // pow(10, 2)
# ...
# Вторая цифра - (num % pow(10, n - 1)) // pow(10, n - 2)
# Первая цифра - (num % pow(10, n)) // pow(10, n - 1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задание -

# # Работа с функциями:
#
#
# def square(number):
#     return pow(number, 2)
#
#
# numbers = [1, 2, 3, 4, 5]
#
# result = map(square, numbers)
# for x in result:
#     print(x)
#
# print(list(map(square, numbers)))
#
#
# def is_adult(age):
#     return age >= 18
#
#
# ages = [13, 18, 19, 16, 30]
#
# print(list(filter(is_adult, ages)))
#
# # # Лямбда выражения, функции - анонимные функции:
#
# is_adult_2 = lambda age: age >= 18
#
# print(list(filter(is_adult_2, ages)))
#
#
# multiplier = lambda x, y: x*y
#
# print(multiplier(2, 3))

# # Декораторы:

# def hello():
#     print("Hello")
#
#
# hello()
#
#
# def say_something(func):
#     func()
#
#
# def hello_world():
#     print("Hello world!")
#
#
# say_something(hello_world)

# # Декоратор логирования начала и конца функции


# def log_decorator(func):
#     def wrap():
#         print(f"Calling func {func}")
#         func()
#         print(f"Func {func} finished its work")
#     return wrap
#
#
# # def hello():
# #     print('Hello man!')
#
#
# # wrapped_by_logger = log_decorator(hello)
# # print(wrapped_by_logger())
#
# @log_decorator
# def hello_2():
#     print("Hello!!!")
#
# hello_2()

# # Декоратор замера времени исполнения функции:
#
# from timeit import default_timer as timer
# import math
# import time
#
#
# def measure_time(func):
#     def inner(*args, **kwargs):  # *args, **kwargs - хитрый способ передать в функцию любые аргументы
#         start = timer()  # замер текущего времени
#         func(*args, **kwargs)
#         end = timer()  # замер текущего времени
#         print(f'Function {func.__name__} took {end - start} for execution')  # func.__name__ - передаем имя функции
#     return inner
#
#
# @measure_time
# def factorial(num):
#     time.sleep(3)  # замораживаем исполнение функции на 3 секунды
#     print(math.factorial(num))
#
#
# factorial(100)

# # Декоратор @wraps:

# from functools import wraps
#
#
# def log_decorator(func):
#     @wraps(func)  # используем чтоб при вызове help корректно отображалось наименование функции
#     def wrap(*args, **kwargs):
#         print(f"Calling func {func.__name__}")
#         func()
#         print(f"Func {func} finished its work")
#     return wrap
#
# @log_decorator
# def hello():
#     print('Hello man!')
#
#
# hello()
# help(hello)
# # ДЗ 9 - Кто выстрелил быстрее?
# '''
# Два участника p1 и p2 участвуют в дуэли.
# Напишите функцию whos_first, которая принимает две строки
# и возвращает имя игрока, который выстрелил первым.
# Если игроки выстрелили одновременно, то вернуть строку "tie".
# '''

# def whos_first(p1, p2):
#     first_player = p1.find("Bang!")
#     second_player = p2.find("Bang!")
#     if first_player < second_player:
#         return print(f"Win player1")
#     elif first_player > second_player:
#         return print(f"Win player2")
#     elif first_player == second_player:
#         return print("tie")
#     else:
#         return print("Mistake")
#
#
# whos_first("    Bang!" , "     Bang!")

# Current time

# from datetime import datetime
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
#
# print("Current time is: ", current_time)

# Работа с функциями:

# def greetings_f(name):
#     print(f"Hey {name}!")
#
#
# greetings_f("Roman")


# def greetings_s(name):
#     hey = f"Hey {name}!"
#     return hey
#
#
# greetings_s("Masha")


# def greetings_t(name = 'Vasya'):  # В случае если ни какой аргумент не передается, то будет выведен по default - 'Vasya'
#     print(f"Hey {name}!")
#
# greetings_t()  # Выводится default аргумент 'Vasya'
#
#
# names = ['Roman', 'Masha', 'Misha', 'Katya']
# for name in names:  # выводим в цикле каждый элемент списка names
#     greetings_t(name)


# def greetings_n(name, m_text):
#     print(f"Hey {name}, {m_text}!")
#
#
# greetings_n("Roman", "nice to meet you")  # перевая форма записи, не защищает от изменения последовательности ввода переменных
# greetings_n(name="Roman", m_text="nice to meet you")  # вторая форма записи, каждой переменной присваивается определенное значение


# def greetings_n(*name, m_text):  # * - для перечисления всех значений листа names
#     for name in names:
#         print(f"Hey {name}, {m_text}!")
#     print("The end of function!")
#
#
# names = ['Roman', 'Masha', 'Misha', 'Katya']
#
# greetings_n(names, m_text="nice to meet you")


# Ошибки и исключения:

# while True:
#
#     while True:
#         try:
#             x = int(input("Enter first number: "))
#         except ValueError:  # проверка x, является ли x числом
#             print("It's not a number!")
#             continue
#         break
#
#     while True:
#         try:
#             y = int(input("Enter second number: "))
#         except ValueError:  # проверка y, является ли y числом
#             print("It's not a number!")
#             continue
#         break
#
#     print("It's equal: ", x + y)
#
#     print("You want to exit (y/n): ")
#     q = input()
#
#     if q.lower() == 'y':
#         print("See you bye!")
#         break
#     elif q.lower() == 'n':
#         print("Nice!")
#         continue
#     else:
#         print("I don't understand you! Bye!")
#         break
#     continue

# Рекурсия (Чмсла Фибоначи, Ханойская башня, Перевод в двоичную систему исчислений):

# Число Фибоначи
# F(n) = F(n-2) + F(n-1)
# F(1) = 1; F(2) = 1
# 1 1 2 3 5 8 ...
# def F(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return F(n - 1) + F(n - 2)
# print (F(7))
#
# # ДЗ 10 - Ханойские башни

# def hanoi_tower(discs):
#     if discs >= 0:
#
#     else: break

# Перевод в двоичную систему исчислений