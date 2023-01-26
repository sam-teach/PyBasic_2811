"""
OOP
"""


# класс - пользовательский тип данних
class Lamp:
    """
    documentation
    """
    # переменние в классе називаются: атрибути/поля/свойства
    on = bool()
    power = int()
    temperature = int()
    lamp_socket = str()

    # конструктор обїектов
    def __init__(self, power: int, temperature: int, lamp_socket: str, on: bool = False):
        self.on = on
        self.power = power
        self.temperature = temperature
        self.lamp_socket = lamp_socket
        print('Lamp constructor!!')

    def set_parameters(self, power: int, temperature: int, lamp_socket: str, on: bool = False):
        self.on = on
        self.power = power
        self.temperature = temperature
        self.lamp_socket = lamp_socket
        print('Lamp constructor!!')

    # функции в классе називаются: методи
    # self - указатель содержащий адрес обїекта являющегося инициатором визова данного метода
    def show_parameters(self):
        # обращение к свойтсвам обїекта происходит через указатель self
        print(f''
              f'On: {self.on}\n'
              f'Power: {self.power}\n'
              f'Temperature: {self.temperature}\n'
              f'Socket: {self.lamp_socket}'
              f'')

    def __str__(self):
        return f'On: {self.on}\nPower: {self.power}\nTemperature: {self.temperature}\nSocket: {self.lamp_socket}'

    def __int__(self):
        return self.power

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.power
        elif isinstance(other, str):
            return other == self.lamp_socket
        else:
            return 0

obj = Lamp(100, 5600, 'e27', True)
# obj.show_parameters()
print(obj)
# print(obj.__str__())
print(int(obj))
if obj == 100:
    print('yes 100 watt')
else:
    print('No')

if obj == 'e27':
    print('e27')
else:
    print('not e27')
#
# obj.power = 100
# obj.show_parameters()

# obj2 = Lamp()
# obj2.show_parameters()
# #  добавление динмаического свойства обїекту
# obj.my_new_data = 'Tigidim'
# print(obj.my_new_data)
# # print(obj2.my_new_data)  # динамическое свойство не передается в другие обїекти и не попадает в класс
# print(obj.__dir__()) # список свойств и методов обїекта
# print(obj.__doc__) # документация
# print(obj.__dict__) # словарь определенних(в которие что-то записали) свойств обїекта
# print(Lamp.__dict__)# словарь определенних(в которие что-то записали) свойств класса
# print(obj.__class__)# возвращает имя класса на основании которого построен обїект
