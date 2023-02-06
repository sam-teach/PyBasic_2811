"""
OOP наследование
Позволяет создавать новій класс на основе существующего
Супер класс/базовій класс/родительский класс
Подкласс/производній класс/дочерний класс
"""


class Person:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'Name: {self.__name}'


class Employee(Person):
    def __init__(self, name: str, position: str):
        self.__position = position
        super().__init__(name)

    @property
    def position(self):
        return self.__position

    def work(self):
        print(f'{self.name} делает работу')

    def __str__(self):
        return super().__str__() + f' Position: {self.position}'


# obj = Employee('Taras', 'Директор')
# print(obj.position)
# print(obj)
# obj.work()

class Employee_with_salary(Employee):
    def __init__(self, name: str, position: str, salary: int):
        self.salary = salary
        super().__init__(name, position)

    def __str__(self):
        return super().__str__() + f' Salary: {self.salary}'


# obj = Employee_with_salary('Taras', 'dev', 1000000)
# print(Employee_with_salary.__mro__)
