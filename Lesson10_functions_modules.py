'''
функции
def имя_функции(аргумент(ы)):
    """строка документации"""
    тело функции(операторы)(код)
'''


def function_name():
    """some strings with describe function"""
    pass


function_name()
print(function_name.__doc__)


def print_hello_message():
    """
    printing hello message
    :return:
    """
    print('Hello!')


def print_named_hello_message(name):
    """
    printing named hello message
    :param name:
    :return:
    """
    print(f'Hell {name}!')


def calc(num1, op, num2):
    """
    comments
    :param num1:
    :param op:
    :param num2:
    :return:
    """
    return eval(f'{num1}{op}{num2}')


result = calc(2, '+', 5)
print(result)
