# '''
# Генераторы списков
# '''
# from random import randint
#
# # randint(start, end) - функция генерирует случайное число из диапазона start - end
# # print(randint(-22, 9))
# '''
# li = [expression for item in iterable]
# expression - выражение
# item - элемент извлекаемый из последовательности
# iterable - последовательность
# '''
# li = [i ** 2 for i in range(10)]
# print(li)
# li = [randint(-100, 100) for i in range(20)]
# print(li)
# '''
# li = [expression for item in iterable if condition]
# expression - выражение
# item - элемент извлекаемый из последовательности
# iterable - последовательность
# condition - условная конструкция, добавление єлемент произойдет только если она вернет True
# '''
# my_string = '11 футболистов за 5 лет забили 231 гол в 102 матчах'
# li = [word for word in my_string.split() if word.isdigit()]
# print(li)
# li = [word for word in my_string.split() if word.isalpha()]
# print(li)
# li = [word for word in my_string if word.isdigit()]
# print(li)
# li = [word for word in my_string if word.isalpha()]
# print(li)

# '''
# Кортеж - тип данных, является НЕИЗМЕНЯЕМЫМ списком
# '''
# tu = tuple([1, 2, 3, 4, 5])
# tu2 = ('1', 2, 3.2, 'Taras')
# tu3 = tuple('apple')
# print(tu)
# print(tu2)
# print(tu3)
# tu4 = (1, 2, 3, ['a', 'b', 'c'])
# tu4[3][1] = 999
# print(tu4)
# # tu4[4]=798 #TypeError: 'tuple' object does not support item assignment
# li=list(tu)
# print(type(li),li)

# '''
# множество - неупорядоченный набор уникальных элементов
# '''
# my_set = set([1, 2, 3, 4, 5, 6])
# print(my_set)
# my_set.add(33)
# print(my_set)
# my_set = {'q', 'w', 'e', 'r', 't', 'y'}
# print(my_set)
# my_set.add(33)
# print(my_set)
# # my_string = '11 футболистов за 5 лет забили 231 гол в 102 матчах'
# # my_set = set(my_string)
# # print(my_set)
# my_set.update('Odarka')
# print(my_set)
# # удаление
# my_set.discard('r')
# print(my_set)
# my_set.discard('W')  # discard - исключает элемент, в случае его отсутствия во множестве нет ошибки
# print(my_set)
# my_set.remove(33)
# print(my_set)
# # my_set.remove(44)  # my_set.remove(44) KeyError: 44
# # print(my_set)

'''
practice
'''

# --- Дано число, посчитать количество нулей в нем
from random import randint

# num = randint(99, 999999)
# print(num)
# count_zero = 0
# for symbol in str(num):
#     if symbol == '0':
#         count_zero += 1
# print(count_zero)
# # python style
# print(str(num).count('0'))

# --- Дано целое число, определить количество нулей в конце числа. Например: 102034000 - 3 нуля
num = 102024000
print(num)
count_zero = 0

option1 = num
while option1 % 10 == 0:
    count_zero += 1
    option1 //= 10
print('option1', count_zero)

option2 = num
count_zero = 0
for sym in str(num)[::-1]:
    if sym == '0':
        count_zero += 1
    else:
        break
print('option2', count_zero)

option3 = num
count_zero = 0
for index in range(len(str(option3)) - 1, 0, -1):
    if str(option3)[index] == '0':
        count_zero += 1
    else:
        break
print('option3', count_zero)

option4 = num
# print('len(str(option4))', len(str(option4)))     # узнал количество цифр получив строку
# print('str(option4)[::-1]', str(option4)[::-1])   # переворот числа превращенного в строку
# print('int(str(option4)[::-1])', int(str(option4)[::-1]))     # превращение перевернутой строки в число (в этот момент если в начале строки были нули, то они исчезнут)
# print('len(str(int(str(option4)[::-1])))', len(str(int(str(option4)[::-1])))) # превращаю предыдущее действо опять в строку и узнаю ее длинну
count_zero = len(str(option4)) - len(str(int(str(option4)[::-1]))) # вычитание одного из другого...

print('option4', count_zero)
