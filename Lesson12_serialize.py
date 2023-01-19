"""
Сериализация
"""
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
print(type(user), user)
json_string = json.dumps(user)
print(type(json_string), json_string)
# loads - на основании строки в формате JSON генерирует python-данные
result_from_string = json.loads(json_string)
print(type(result_from_string), result_from_string)
# dump - на основании python-данных генерирует строку в формате JSON и записывает в файл
with open('files/test.json', 'w') as file:
    json.dump(user2, file)
# load - на основании строки в формате JSON прочитанной из файла генерирует python-данные
with open('files/test.json', 'r') as file:
    read_from_file = json.load(file)
print(type(read_from_file), read_from_file)

