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
my_list = list()
my_list2 = []
my_list3 = [1, 2, 3, '1234556', 3.2, my_list]
my_list4 = list('123 asdf asdf asdf sdfvc sdef')
s = 'Vasa 123 132 5 sdfvc sdef'
my_list5 = s.split()
print('my_list -> ', my_list)
print('my_list2 -> ', my_list2)
print('my_list3 -> ', my_list3)
print('my_list4 -> ', my_list4)
print('my_list5 -> ', my_list5)

