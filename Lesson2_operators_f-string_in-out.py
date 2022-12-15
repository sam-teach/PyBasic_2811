# i = int()
# f = float()
# s = str()
# b = bool()
#
# i = 123
# s = '345'
# # new_string = s + i
# new_string = s + str(i)
# print(new_string)
#
# num_1 = 123
# num_2 = 2.24
# result = num_1 + num_2
# print(type(result), result)
# next_result=int(result)
# print(type(next_result), next_result)
#
# new_string = int(s) + i
# print(new_string)

# '''
# операторы
# арифметические
# +
# -
# *
# /
# %   - получение остатка от деления
# //  - деление нацело
# **  - возведение в степень
# =   - присвоение
#         (справа налево, т.е.
#         a = 5   пятерка записалась в a
#         b = 7   семерка записалась в b
#         a = b   семерка записалась в a)
# +=  - a = a + b эквивалентно a += b
# -=
# *=
# /=
# '''
#
# '''
# логические
# >
# <
# >=
# <=
# ==  - равно
# !=  - не равно
# and - и
#     1 and 1 -> 1
#     1 and 0 -> 0
#     0 and 1 -> 0
#     0 and 0 -> 0
#
# or  - или
#     1 or 1 -> 1
#     1 or 0 -> 1
#     0 or 1 -> 1
#     0 or 0 -> 0
#
# ^   - исключающее или (XOR)
#     1 ^ 1 -> 0
#     1 ^ 0 -> 1
#     0 ^ 1 -> 1
#     0 ^ 0 -> 0
#
# not - инверсия bool-значения
#
# '''
# print(7 > 5)
# print(not 7 > 5)
# print(7 > 5 and 7 > 12)
# print(7 > 5 or 7 > 12)
# print(7 > 5 ^ 7 > 12)
# print(7 != 5)
# # print(7 not 5)
# print(not 7 == 5)
# '''
# тождественности
# is      - идентичность операндов(участники операции)
# is not  - не идентичность операндов
# '''
# a = 123
# b = 123.0
# print(a == b)
# print(a is b)
#
# '''
# принадлежности
# in      - принадлежит
# not in  - наоборот
# '''
# some_string = 'sinchrophazotron'
# print('a' in some_string)
# print('a' not in some_string)
# some_another_string = 'Мама мыла раму'
# print('мыла' in some_another_string)

# name = 'Taras'
# age = 12
# # Меня зовут name и мне age лет
# print('Меня зовут ' + name + ' и мне ' + str(age) + ' лет')
# print('Меня зовут', name, 'и мне', age, 'лет')
# print(f'Меня зовут {name} и мне {age} лет') # <- f(форматированная)-строка

# data_from_user = input('Описание чего вы ожидаете от пользователя')
# print(type(data_from_user), data_from_user)
#
# int_from_user = int(input('Введи число: '))
# print(type(int_from_user), int_from_user)

# examples
'''
Программа для подсчета суммы двух чисел
'''
num1 = float(input('Введите число: '))
num2 = float(input('Еще одно: '))
print(f'{num1} + {num2} = {num1 + num2}')

radius = float(input('Введите радиус окружности: '))
print(f'Площадь окружности {3.14 * radius ** 2}')

number = int(input('Введите трехзначное число: '))
print(f'В этом числе '
      f'{number % 10} единиц, '
      f'{number // 10 % 10} десятков, '
      f'{number // 100} сотен')
