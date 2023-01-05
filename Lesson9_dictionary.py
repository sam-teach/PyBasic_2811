# '''
# словарь = {ключ : значение} - ключ является неизменным объектом
#
# '''
# my_dict = {'key': 'value'}
# print(my_dict, type(my_dict))
#
# address = {
#     'city': 'Kyiv',
#     'street': 'Lesya Kurbasa',
#     'house': 25,
#     'apartment': 33,
#     14: 'четырнадцать'
# }
# person = {
#     'name': 'Volodimir',
#     'age': 42,
#     'address': address,
# }
# print(person)
# print(person['name'])
# print(person['address']['street'])
# from random import randint
#
# cube_dict = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six'
# }
# value = randint(1, 100)
# print(value)
# result = cube_dict[(value % 6) + 1]
# print(f'Результат броска кубика {result}')

# a = 9
# di = {'key': a}
# print(di)
# a = 3
# print(di)
# di['key'] = 3
# print(di)
# my_dict = {('str1', 'str2', 'str3'): 123}
# my_dict = {123: ('str1', 'str2', 'str3')}

# my_dict = {'apple': {'eng': 'apple', 'som': 'tufax', 'de': 'apfel', 'fr': 'pomme'}}
# print(my_dict['apple']['eng'])
# print(my_dict['apple']['fr'])
# '''
# методы словарей
# '''
#
# address = {
#     'city': 'Kyiv',
#     'street': 'Lesya Kurbasa',
#     'house': 25,
#     'apartment': 33,
#     14: 'четырнадцать'
# }
# person = {
#     'name': 'Volodimir',
#     'age': 42,
#     'address': address,
# }
# print(person)
# print(person['name'])
# # print(person['job']) # KeyError: 'job'
# print(person.get('job'))  # позволяет получить значение по ключу, в случае отсутствия ключа вернет None, а не ошибку
# #  добавление одного элемента в словарь
# person['job'] = 'president'
# print(person['job'])
# print(person)
# print(person.keys())  # возвращает ключи словаря
# for key in person.keys():
#     print(key)
#
# print(person.values())  # возвращает значения словаря
# for value in person.values():
#     print(value)
#
# for i in person:  # при переборе словаря в цикле, перебираться будут ключи
#     print(i, end='-')
#
# print(person.items())
# for element in person.items():
#     print(element, end=' - ')
# print()
# print('-------------')
# # метод добавления нескольких элементов в словарь
# person.update({'legs': 2, 'hands': 2, 'head': 1})
# print(person)
# # удаление элемента
# del (person['age'])
# print(person)
# # del (person['age'])  # KeyError: 'age' <- попытка удаления несуществующего ключа
# print(person.pop('legs'))  # KeyError: 'age' <- попытка удаления несуществующего ключа
# print(person)
# # dictionary.pop( key, d) - удаляет элемент с ключом key и возвращает его значение,
# # если такого ключа нет вернет d,
# # если d не передавали в метод вызовет ошибку
# print(person.pop('legs', None))
# li = list(person)
# print(li)

'''
проверка на вхождение в словарь
'''
cube_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six'
}
print(2 in cube_dict)
print(2 in cube_dict.keys())
print('two' in cube_dict)
print('two' in cube_dict.values())
