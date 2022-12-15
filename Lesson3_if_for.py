'''
if выражение:
    код выполняющийся если выражение вычислено как True
    может быть много строк
else:
    код выполняющийся если выражение вычислено как False
'''

variable = int(input('Input number: '))
if variable % 2 == 0:
    print('четное')
else:
    print('нечетное')

if variable:
    print('Yes')
else:
    print('No')

if not variable % 2:
    print('четное')
else:
    print('нечетное')

if '3' in str(variable):
    print('В єтом числе есть тройка')

if 3 < variable < 19:
    print(f'{variable} в диапазоне от 3 до 19')

if variable % 5 == 0 and variable > 40:
    print(f'{variable} больше 40 и кратно 5')

if 10 < variable < 50 or\
        -50 < variable < -10:
    print(f'{variable} попадает в диапазон от |10| до |50|')
else:
    print('За пределами диапазона')
