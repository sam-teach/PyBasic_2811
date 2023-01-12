num = 1234


def fun() -> None:
    '''
    Тестируем модули
    fun hello
    :return: None
    '''
    print('Hello!')


def print_module_name():
    print(f'Lesson 10 -> {__name__}')


if __name__ == '__main__':
    print('test all function')
    fun()
    print(num)
