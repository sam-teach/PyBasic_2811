'''
1)У вас есть строка my_string = '0123456789'.
Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
Генерирование через range или другие "фишки" я засчитывать не буду ))
'''

my_string = '0123456789'
for desyatki in my_string:
    for edinitsi in my_string:
        result = int(desyatki + edinitsi)
        print(result, end=' : ')
