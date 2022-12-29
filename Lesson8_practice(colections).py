# '''
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого
#  первый элемент из my_list стоит на последнем месте.
#  Если my_list [1,2,3,4], то new_list [2,3,4,1]
# '''
# my_list = [1, 2, 3, 4]
# # new_list = my_list[1:].copy()
# # new_list.append(my_list[0])
# # ---------
# # new_list = my_list[1:] + my_list[0:1]
# # ------------
# # new_list = my_list[1:] + [my_list[0]]
# # -----------
# # new_list = my_list.copy()
# # new_list.append(new_list.pop(0))
# # -------
# new_list = []
# for index in range(1, len(my_list)):
#     new_list.append(my_list[index])
# new_list.append(my_list[0])
# print(new_list)
# '''
# Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя! (используйте метод pop)
# '''
# my_list = [1, 2, 3, 4]
# my_list.append(my_list.pop(0))
# print(my_list)
# '''
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34, но меньше чем 56".
# Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
# (используйте split и проверку isdigit)
# '''
# my_str = '43 больше чем 34, но меньше чем 56'
# result = sum(int(word) for word in my_str.split() if word.isdigit())
# print(result)
#
# result_str = ''
# for symbol in my_str:
#     if symbol.isdigit():
#         result_str += symbol
#     else:
#         result_str += ' '
# print(sum(int(number) for number in result_str.split()))

# '''
# 7. Дана строка my_str в которой символы МОГУТ повторяться
#  и два символа l_limit и r_limit, которые точно находятся в
# этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими
#  символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
# '''
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# sub_str = []
# # l_index = my_str.find(l_limit)
# # r_index = my_str.rfind(r_limit)
# # print(my_str[l_index + 1:r_index])
# # print(my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)])
# for index in range(len(my_str)):
#     if my_str[index] == l_limit:
#         l_index = index + 1
#         break
# for index in range(-1, len(my_str) * -1, -1):
#     if my_str[index] == r_limit:
#         r_index = index
#         break
# print(my_str[l_index:r_index])
# '''
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов
#  и поместите эти пары в список. Если строка
#  содержит нечетное количество символов, пропущенный второй
#  символ последней пары должен быть заменен
#  подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'],
#   'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)
# '''
# start_str = 'abcde'
# # my_str = start_str
# # if len(my_str) % 2 != 0:
# #     my_str += '_'
# # li = []
# # for i in range(0, len(my_str), 2):
# #     li.append(my_str[i:i + 2])
# # print(li)
# # --------
# li = [start_str[i:i + 2] for i in range(0, len(start_str), 2)]
# if len(li[-1]) < 2:
#     li[-1] += '_'
# print(li)

# '''
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
#  которые больше суммы двух своих соседей
#  (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
#   Крайние элементы списка никогда не учитываются,
#   поскольку у них недостаточно соседей. Для списка [2,4,1,5,3,9,0,7]
#    ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
# '''
# li = [2, 4, 1, 5, 3, 9, 0, 7]
# count = 0
# for i in range(1, len(li) - 1):
#     if li[i] > li[i - 1] + li[i + 1]:
#         count += 1
# print(count)
# result = sum(1 for i in range(1, len(li) - 1) if li[i] > li[i - 1] + li[i + 1])
# print(result)

# '''
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33] Создать новый список в который поместить только строки из my_list.
# '''
#
# li = [1, 2, 3, "11", "22", 33]
# print([i for i in li if type(i) == str])
# print([i for i in li if isinstance(i, str)])
# # ----
# new_li = []
# for element in li:
#     if isinstance(element, str):
#         new_li.append(element)
# print(new_li)

# '''
# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках ХОТЯ БЫ РАЗ.
# '''
# my_str1 = 'qawertwy'
# my_str2 = 'qazwsx'
# print({i for i in my_str1 if i in my_str2})
# result = set()
# for i in my_str1:
#     if i in my_str2:
#         result.add(i)
# print(result)

'''
13. Даны две строки. Создать список в который поместить те символы,
которые есть в обеих строках, но в каждой
 ТОЛЬКО ПО ОДНОМУ разу. Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
  т.к. эти символы есть в каждой строке по одному разу
'''
my_str1 = 'aaaasdf1'
my_str2 = 'asdfff2'
# li = [i for i in my_str1 if i in my_str2]
# li2 = [i for i in li if my_str1.count(i) == 1 and my_str2.count(i) == 1]
# print(li2)
# -----
li1 = [symbol for symbol in my_str1 if my_str1.count(symbol) == 1]
li2 = [symbol for symbol in my_str2 if my_str2.count(symbol) == 1]
print(li1)
print(li2)
result = list(set(li1) & set(li2))  # & - intersection - пересечение множеств
print(result)
