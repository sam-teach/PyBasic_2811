# '''
# if выражение:
#     код выполняющийся если выражение вычислено как True
#     может быть много строк
# else:
#     код выполняющийся если выражение вычислено как False
# '''
#
# variable = int(input('Input number: '))
# if variable % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')
#
# if variable:
#     print('Yes')
# else:
#     print('No')
#
# if not variable % 2:
#     print('четное')
# else:
#     print('нечетное')
#
# if '3' in str(variable):
#     print('В єтом числе есть тройка')
#
# if 3 < variable < 19:
#     print(f'{variable} в диапазоне от 3 до 19')
#
# if variable % 5 == 0 and variable > 40:
#     print(f'{variable} больше 40 и кратно 5')
#
# if 10 < variable < 50 or\
#         -50 < variable < -10:
#     print(f'{variable} попадает в диапазон от |10| до |50|')
# else:
#     print('За пределами диапазона')

# '''
# Задача
# определить сумму покупки в зависимости от скидки
# до 500 грн - без скидки
# от 500 грн до 1000 грн - 5%
# от 1000 - 8%
# '''
# # Вариант 1
# price = float(input('Input price: '))
# if price < 500:
#     print(f'Your check is {price}')
# else:
#     if price < 1000:
#         print(f'Your check is {price * 0.95}')
#     else:
#         print(f'Your check is {price * 0.92}')
# print()
# # Вариант 2
# if price < 500:
#     print(f'Your check is {price}')
# if 500 < price < 1000:
#     print(f'Your check is {price * 0.95}')
# if price > 1000:
#     print(f'Your check is {price * 0.92}')
# print()
# # Вариант 3
# if price < 500:
#     print(f'Your check is {price}')
# elif price < 1000:
#     print(f'Your check is {price * 0.95}')
# else:
#     print(f'Your check is {price * 0.92}')
#
# print(
#     '''
#     Играть - нажмите 1
#     Сохранить - нажмите 2
#     Загрузить - нажмите 3
#     Опции - нажмите 4
#     Выход - нажмите 5
#     '''
# )
# user_choice = int(input('Сделайте ваш выбор: '))
# if user_choice == 1:
#     print('Play game')
# elif user_choice == 2:
#     print('Save pandas')
# elif user_choice == 3:
#     print('Load some data')
# elif user_choice == 4:
#     pass
# elif user_choice == 5:
#     print('Bye')
# elif user_choice == 333:
#     print('godmode')
# else:
#     print('Error choice')

my_string = 'London is the capital of Great Britain'
count_i = 0
for symbol in my_string:
    print(symbol, end=' ')
    if symbol == 'i':
        count_i += 1
print(f'\nIn this string {count_i} symbol\'s "i"')

'''
range(start,end,step)
default(0,x,1)
'''
print(range(10))
for i in range(10):
    print(i, end=' ')
print()
print(range(2, 10))
for i in range(2, 10):
    print(i, end=' ')
print()
print(range(2, 10, 2))
for i in range(2, 10, 2):
    print(i, end=' ')
print()
print(range(10, 2, -1))
for i in range(10, 2, -1):
    print(i, end=' ')
print()

start_range = int(input('Input start range: '))
end_range = int(input('Input end range: '))
# 1
for i in range(start_range, end_range + 1):
    if i % 2 == 0:
        print(i, end=' ')
print()
# 2
adj = 0
if start_range % 2 != 0:
    adj = 1
for i in range(start_range + adj, end_range + 1, 2):
    print(i, end=' ')
print()
# 3
for i in range(
        start_range + start_range % 2,  # в случае нечетного старта превратим в четный
        end_range + 1,  # конец диапазона
        2  # шаг последовательности
):
    print(i, end=' ')
print()
'''
Задача
найти в диапазоне первые пять чисел кратные пяти
'''
count_5 = 0
for i in range(start_range, end_range + 1):
    if i % 5 == 0:
        print(i, end=' ')
        count_5 += 1
        if count_5 == 5:
            break
else:  # 'Выполняется этот код только если не сработал break'
    print("чисел кратных пяти меньше пяти")


