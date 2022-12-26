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

'''
множество - неупорядоченный набор уникальных элементов
'''
my_set = set([1, 2, 3, 4, 5, 6])
print(my_set)
my_set.add(33)
print(my_set)
my_set = {'q', 'w', 'e', 'r', 't', 'y'}
print(my_set)
my_set.add(33)
print(my_set)
# my_string = '11 футболистов за 5 лет забили 231 гол в 102 матчах'
# my_set = set(my_string)
# print(my_set)
my_set.update('Odarka')
print(my_set)
# удаление
my_set.discard('r')
print(my_set)
my_set.discard('W')  # discard - исключает элемент, в случае его отсутствия во множестве нет ошибки
print(my_set)
my_set.remove(33)
print(my_set)
# my_set.remove(44)  # my_set.remove(44) KeyError: 44
# print(my_set)
