'''
1. Создать папку ./alphabet/ Если папка существует, то ОК.
2. В папке ./alphabet/ создать файлы
вида a.txt, b.txt, ..., z.txt
в которых будет записана строка алфавита,
но с заменой буквы из названия файла на прописную.
Пример: для b.txt строка будет aBcde...
3. Сделать щелчек Таноса - удалить случайным
образом половину всех файлов в этой папке.
'''
import os
import random
import string


# import os
#
# path_win = r'C:\dir\dir2\file.txt'
# path_linux_macos_android_etc = r'sda1/dir/dir2/file.txt'
# print(os.path.join('папка', 'файл'))
# # os.mkdir(r'files\папка') # в случае существования файла - ошибка
# os.makedirs(r'files\папка', exist_ok=True)  # ключ exist_ok указівает на игнорирование ошибки
# with open(r'files\test', 'w'):
#     pass
# os.remove(r'files\test')  # удаляет заданній файл
# os.rmdir(r'files\папка')  # удаляет заданную папку(ПУСТУЮ)
# print(os.listdir('files'))  # возвращает список содержимого папки
# print(os.path.isdir(r'files\test.csv'))
#
#
# def del_directory(path):
#     """
#     удаление папки с содержимім
#     :param path:
#     :return:
#     """
#     if os.path.isdir(path):
#         # получение списка содержимого
#         elements = os.listdir(path)
#         for element in elements:
#             # получение полного пути к єлементу в папке
#             path_to_element = os.path.join(path, element)
#             # если єлемент является папкой
#             if os.path.isdir(path_to_element):
#                 # очистим папку (та же функция(рекурсия))
#                 del_directory(path_to_element)
#             else:
#                 # если єлемент является файлом, удалим его
#                 os.remove(path_to_element)
#         # удалим (уже) пустую папку
#         os.rmdir(path)

class PlayWithFolder:
    """
    работа с тестовой папкой наполняемой автоматически,
    віборочное удаление єлементов из папки
    """

    def __init__(self, dirname: str = 'alphabet'):
        """
        создание обїекта = создание папки, по умолчанию имя 'alphabet
        :param dirname:
        """
        self.dirname = dirname
        os.makedirs(self.dirname, exist_ok=True)

    def create_file(self, symbol: str):
        """
        создание файла в звдвнной папке (dirname)
        имя файла передается(symbol)
        генерируется строка из символов алфавита, где symbol приводится к прописному виду
        :param symbol:
        :return:
        """
        with open(os.path.join(self.dirname, f'{symbol}.txt'), 'w') as file:
            file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

    def create_files(self):
        """
        создает строку на основании которой будут создаватся файлі
        :return:
        """
        for symbol in string.ascii_lowercase:
            self.create_file(symbol)

    def tanos_click(self):
        """
        удаление половині файлов из заданой папки(dirname)
        файлі вібираются случайнім образом
        :return:
        """
        directory_list = os.listdir(self.dirname)
        random.shuffle(directory_list)  # метод shuffle перемешивает содержимое итерируемого обїекта
        for filename in directory_list[::2]:
            path_to_file = os.path.join(self.dirname, filename)
            os.remove(path_to_file)


obj = PlayWithFolder()
# obj.create_files()
obj.tanos_click()