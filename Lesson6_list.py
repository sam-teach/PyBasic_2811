'''
Пример поиска решения ДЗ
Проверить, является ли число простым(делится без остатка только на 1 и себя)
'''

# # зададим случайное число
# num = 119
# # переберем числа от 2 до самого числа(исключая его)
# for i in range(2, num):
#     # если число делится без остатка, то оно не простое
#     if num % i == 0:
#         print('не простое')
#         # прервем выполнение цикла
#         break
# # если цикл завершился без прерываний, значит число простое
# else:
#     print('число простое')

'''
Списки - тип данных позволяющий хранить под одним именем
 множество разнообразных объектов, является итерируемым элементом
'''
# создание списка
# my_list = list()
# my_list2 = []
# my_list3 = [1, 2, 3, '1234556', 3.2, my_list]
# my_list4 = list('123 asdf asdf asdf sdfvc sdef')
# s = 'Vasa 123 132 5 sdfvc sdef'
# my_list5 = s.split()
# print('my_list -> ', my_list)
# print('my_list2 -> ', my_list2)
# print('my_list3 -> ', my_list3)
# print('my_list4 -> ', my_list4)
# print('my_list5 -> ', my_list5)

# обращение к элементам
#     0  1  2  3  4  5 0    1    2      6
li = [1, 2, 3, 4, 5, ['a', 'b', 'c'], 'Anatoliy']
print('li', li)
print('li[2]', li[2])
print('li[5]', li[5])
print('li[5][1]', li[5][1])  # обращение к элементу списка в списке
# пример списка в списке - матрица
matrix = [
    [1, 2, 3, 4, 5],
    [2, 4, 1, 5, 6],
    [1, 1, 0, 3, 5],
]
print('li[2:5]', li[2:5])  # срез
print('li[-2]', li[-2])  # отрицательный индекс
# перебор списка по индексу
print('''for index in range(len(li)):
    print(li[index], end=' ')''')
for index in range(len(li)):
    print(li[index], end=' ')
print()
# перебор списка по элементно
print('''for element in li:
     print(element, end=' ')''')
for element in li:
    print(element, end=' ')
print()
