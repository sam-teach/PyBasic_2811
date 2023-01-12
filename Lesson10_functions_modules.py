# '''
# функции
# def имя_функции(аргумент(ы)):
#     """строка документации"""
#     тело функции(операторы)(код)
# '''
#
#
# def function_name():
#     """some strings with describe function"""
#     pass
#
#
# function_name()
# print(function_name.__doc__)
#
#
# def print_hello_message() -> None:
#     """
#     printing hello message
#     :return:
#     """
#     print('Hello!')
#
#
# def print_named_hello_message(name: str) -> None:
#     """
#     printing named hello message
#     :param name:
#     :return:
#     """
#     print(f'Hell {name}!')
#
#
# def calc(num1, op: str, num2) -> float:
#     """
#     comments
#     :param num1: int
#     :param op:
#     :param num2:
#     :return: result
#     """
#
#     return eval(f'{num1}{op}{num2}')
#
#
# result = calc(2, 2, 5)
# print(result)
#
#
# # calc()
#
# def test_fun(b):
#     print('in fun', b)
#     b *= 2
#     print('in fun', b)
#
#
# a = 3
# test_fun(a)
# print('out fun', a)

# '''
# аргументы функций по умолчанию
# '''
#
#
# def test_fun(arg1='Default_arg1', arg2='Default_arg2') -> None:
#     print(arg1, arg2)
#
#
# test_fun(1, 2)
# test_fun(1)
# test_fun()
#
# '''
# именованные аргументы
# '''
# test_fun(arg2=123)

# '''
# переменное количество аргументов
# '''
#
#
# def print_names(*names, format=None):
#     if format == 'cap':
#         result = [i.capitalize() for i in names]
#     elif format == 'low':
#         result = [i.lower() for i in names]
#     else:
#         result=[i for i in names]
#     print(result, '<-', type(result))
#
#
# print_names('vasa', 'peTya', 'KaTyA')

'''
модули
'''
# # подключение модуля
# import Lesson10_example_module
#
# # при использовании необходимо указать имя модуля
# Lesson10_example_module.fun()
# print(Lesson10_example_module.num)
# # просмотр содержимого модуля
# print(dir(Lesson10_example_module))

# # произвольное имя модуля
# import Lesson10_example_module as Le10
#
# Le10.fun()

# # подключение отдельного элемента из модуля
# from Lesson10_example_module import num, fun
#
# print(num)
# fun()

# подключение всех элементов из модуля
# from Lesson10_example_module import *
#
# print(num)
# fun()
import Lesson10_example_module as L10
print(__name__)
# L10.print_module_name()