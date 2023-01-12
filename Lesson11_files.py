'''
obj = open(имя_файла, режим_открытия)
obj -> переменная хранящая набор инструментов для работы с файлом
имя_файла -> путь к файлу в ОС (может быть относительным или абсолютным)
        files/test.txt -> относительный (относительно данного файла)
        C:/Users/Admin/PycharmProjects/PyBasic_2811/files/test.txt -> абсолютный
режим_открытия -> указывает на способ взаимодействия с файлом
        r -> доступ для чтения, в случае отсутствия файла: ошибка открытия
        w -> доступ для записи, в случае отсутствия файла: создает файл, в случае отсутствия доступа:ошибка открытия
                в случае существования файла: удаляет данные из файла
        a -> доступ для ДОзаписи, в случае отсутствия файла: создает файл, в случае отсутствия доступа:ошибка открытия
                в случае существования файла: ставит курсор в конец файла
        b -> бинарный
        t -> текстовый
        + -> добавляет к любому режиму возможность записи
obj = open("files/test.txt", "wt")
obj = open("files/test.txt", "rt+")
'''
# obj = open("files/test.txt", "wt")
# obj.close()

# with -> менеджер контекста - позволяет автоматически закрывать файл
#  при выходе за пределы его(менеджера) области видимости
# with open("files/test.txt", "wt") as file:
#     делаем что-нибудь
# <- обасть видимости закрылась

# with open("files/test.txt", "wt") as file:
#     print(file.name)
#     print(file.mode)
#     print(file.closed)
#     print(file.encoding)

# запись в файл
# with open("files/test.txt", "wt") as file:
#     print(file.write('Hello World!'))

# li = ['123', 'qwe', '654']
# with open("files/test.txt", "at") as file:
#     # file.writelines(li)
#     file.writelines([i+'\n' for i in li])
# чтение из файла
# with open("files/test.txt", "rt") as file:
#     result = file.read()
#     print('read() -> ', result)
#
# with open("files/test.txt", "rt") as file:
#     result = file.read(5)
#     print('read(5) -> ', result)
#     print(file.read(6))
#
# with open("files/test.txt", "rt") as file:
#     result = file.readline()
#     print('readline() -> ', result)
#
# with open("files/test.txt", "rt") as file:
#     result = file.readlines()
#     print('readlines() -> ', result)

'''
примеры функций для обработки файлов
'''


def read_txt_files(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data


def write_txt_file(filename: str, data):
    with open(filename, 'wt') as file:
        file.write(str(data))


count = 0
text = read_txt_files('files/London.txt')
for word in text.split():
    if word == 'London':
        count += 1
print(f'London: {count}')
