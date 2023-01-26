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


obj = Lamp()

obj.power = 100
obj.show_parameters()
obj2 = Lamp()
obj2.show_parameters()
