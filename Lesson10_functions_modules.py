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

'''
аргументы функций по умолчанию
'''


def test_fun(arg1='Default_arg1', arg2='Default_arg2') -> None:
    print(arg1, arg2)


test_fun(1, 2)
test_fun(1)
test_fun()

'''
именованные аргументы
'''
test_fun(arg2=123)


