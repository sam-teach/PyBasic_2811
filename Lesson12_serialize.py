"""
Сериализация
"""
from random import randint

user = {
    'firstname': 'Taras',
    'lastname': 'Shevchenko',
    'age': 208,
    'email': 'kobzar_1814@gmail.ua',
}
user2 = {
    'name': 'Taras',
    'surname': 'Bulba',
    'age': 188,
    'e-mail': 'taras_childfree@kobzar.ua'
}
# JSON -JavaScript Object Notation  ТЕКСТОВЫЙ формат обмена данными, основанный на JavaScript.
import json
# dumps - на основании python-данных генерирует строку в формате JSON
# print(type(user), user)
# json_string = json.dumps(user)
# print(type(json_string), json_string)
# # loads - на основании строки в формате JSON генерирует python-данные
# result_from_string = json.loads(json_string)
# print(type(result_from_string), result_from_string)
# # dump - на основании python-данных генерирует строку в формате JSON и записывает в файл
# with open('files/test.json', 'w') as file:
#     json.dump(user2, file)
# # load - на основании строки в формате JSON прочитанной из файла генерирует python-данные
# with open('files/test.json', 'r') as file:
#     read_from_file = json.load(file)
# print(type(read_from_file), read_from_file)

# CSV - Comma-Separated Values текстовый формат, предназначенный для представления табличных данных
import csv


# with open('files/Книга2.csv', 'rt') as file:
#     reader = csv.reader(file, delimiter=';')
#     print(list(reader))

# with open('files/test.csv', 'wt') as file:
#     writer = csv.DictWriter(file, fieldnames=user.keys(), delimiter=';')
#     writer.writeheader()
#     writer.writerow(user)

# with open('files/test.csv', 'rt') as file:
#     reader = csv.DictReader(file, delimiter=';')
#
#     for row in reader:
#         print(row)

def read_from_csv(filename: str) -> list:
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data


def write_to_csv(filename: str, data: list):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in data:
            writer.writerow(row)


def add_grade_to_stud_list(subj: str):
    student_list = read_from_csv('files/Книга2.csv')
    student_list[0].append(subj)
    for stud_number in range(1, len(student_list)):
        student_list[stud_number].append(randint(1, 13))
    write_to_csv('files/Книга2.csv', student_list)


add_grade_to_stud_list('Физкультура')
