'''
while выражение:
    тело цикла
'''
# password = '123'
# pass_in = input('Input password: ')
# while pass_in != password:
#     print('Wrong password!')
#     pass_in = input('Try again: ')
# else:
#     print('Welcome')

# count_try = 3
# pass_in = input('Input password: ')
# while pass_in != password:
#     count_try -= 1
#     if count_try == 0:
#         print('NO WELCOME')
#         break
#     print('Wrong password!')
#     pass_in = input('Try again: ')
# else:
#     print('Welcome')

# бесконечный for
# for  _ in iter(int,1):
#   pass

# for i in range(count_try):
#     pass_in = input('Input password: ')
#     if pass_in == password:
#         print('Welcome')
#         break
#     else:
#         print('Try again')
# else:
#     print('NO WELCOME')

# получить сумму всех цифр числа
# num = int(input('Input number: '))
# result = 0
# while num > 0:
#     result += num % 10  # result = result + num % 10
#     num //= 10  # num = num // 10
# print(result)

# цикл в цикле
# sym_in_string = 5
# count_of_strings = 4
# for h in range(count_of_strings):
#     for w in range(sym_in_string):
#         print('*', end=' ')
#     print()

# columns = 5
# strings = 5
# for s in range(strings):
#     for c in range(columns):
#         print('*', end=' ')
#     print()

# columns = 5
# strings = 5
# for s in range(strings):
#     for c in range(s + 1):
#         print('*', end=' ')
#     print()
'''
строка - НЕИЗМЕНЯЕМЫЙ тип данных, представляет собой последовательность символов
является итерируемым объектом
'''
# my_string = 'string'
# my_string2 = str('another string')
# my_string3 = '''multiline
# string'''
# print('len(my_string)', len(my_string))  # len() - функция возвращающая длину итерируемого объекта
# print('my_string[0]', my_string[0])  # обращение к символу по индексу
# print('my_string[-1]', my_string[-1])  # отрицательные индексы обращаются с конца
# '''срезы'''
# # string[старт:стоп:шаг] default[0:len(string):1]
# print('string[старт:стоп:шаг] default[0:len(string):1]')
# print('my_string[0:len(my_string):1]', my_string[0:len(my_string):1])
# print('my_string[2:]', my_string[2:])
# print('my_string[:4]', my_string[:4])
# print('my_string[1:4]', my_string[1:4])
# print('my_string[4:1:-1]', my_string[4:1:-1])
# print('my_string[::-1]', my_string[::-1])
# # переворот числа
# number = 123456
# #        преобразование        преобразование  переворот
# result =    int                 (str(number)    [::-1])
# print(result)

my_string = 'some new string'
print('my_string ->', my_string)

print('my_string.split() ->', my_string.split())
print('my_string.split(sep="s") ->', my_string.split(sep="s"))
print('my_string.upper() ->', my_string.upper())
print('my_string ->', my_string)

symbol = '.'
print('symbol.isdigit() ->', symbol.isdigit())  # число
print('symbol.isalpha() ->', symbol.isalpha())  # буква
print('symbol.isalnum ->', symbol.isalnum())  # число или буква

text = 'London is the capital of Great Britain'
print(text)
print('text.find("a")', text.find("a"))
print('text.find("ap")', text.find("ap"))
print('text.find("al")', text.find("al"))

print("text.replace('London', 'Kyiv')", text.replace('London', 'Kyiv'))
print(text)
print("text.replace('Great Britain', '***')", text.replace('Great Britain', '***'))

# родитель f-строк
print('{}, {}, {}')
print('{}, {}, {}'.format(12, 'Stone', 'table'))
print('{1}, {2}, {0}'.format(12, 'Stone', 'table'))
print('{c}, {a}, {b}'.format(a=12, b='Stone', c='table'))
