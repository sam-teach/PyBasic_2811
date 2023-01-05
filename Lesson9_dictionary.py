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

my_dict = {'apple': {'eng': 'apple', 'som': 'tufax', 'de': 'apfel', 'fr': 'pomme'}}
print(my_dict['apple']['eng'])
print(my_dict['apple']['fr'])
