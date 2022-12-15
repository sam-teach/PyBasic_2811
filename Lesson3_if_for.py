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

'''
Задача
определить сумму покупки в зависимости от скидки
до 500 грн - без скидки
от 500 грн до 1000 грн - 5%
от 1000 - 8%
'''
# Вариант 1
price = float(input('Input price: '))
if price < 500:
    print(f'Your check is {price}')
else:
    if price < 1000:
        print(f'Your check is {price * 0.95}')
    else:
        print(f'Your check is {price * 0.92}')
print()
# Вариант 2
if price < 500:
    print(f'Your check is {price}')
if 500 < price < 1000:
    print(f'Your check is {price * 0.95}')
if price > 1000:
    print(f'Your check is {price * 0.92}')
print()
# Вариант 3
if price < 500:
    print(f'Your check is {price}')
elif price < 1000:
    print(f'Your check is {price * 0.95}')
else:
    print(f'Your check is {price * 0.92}')

print(
    '''
    Играть - нажмите 1
    Сохранить - нажмите 2
    Загрузить - нажмите 3
    Опции - нажмите 4
    Выход - нажмите 5
    '''
)
user_choice = int(input('Сделайте ваш выбор: '))
if user_choice == 1:
    print('Play game')
elif user_choice == 2:
    print('Save pandas')
elif user_choice == 3:
    print('Load some data')
elif user_choice == 4:
    pass
elif user_choice == 5:
    print('Bye')
elif user_choice == 333:
    print('godmode')
else:
    print('Error choice')
