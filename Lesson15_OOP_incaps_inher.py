class User:
    # __ (два нижних подчеркивания) перед именем свойства делает его скрітім(private) за пределами класса
    __name = str()  # ''
    __age = int()  # 0
    a = 0

    def __init__(self, name: str, age: int):
        self.__name = name  # Vasiliy
        self.__age = age  # 0

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}'

    # методі позволяющие работать с приватніми свойствами назіваются акцессорами
    # меняющие приватніе свойства назіваются сеттерами (мутатор)
    # def set_age(self, age: int):
    #     if age >= 0:
    #         self.__age = age
    #
    # # возвращающие приватное свойство - геттерами
    # def get_age(self):
    #     return self.__age
    #
    # def get_name(self):
    #     return self.__name

    # Анотации атрибутов - позволяют получать доступ к приватнім свойствам через псевдоним,
    # при єтом обращение технически происходит через метод
    # для создания анотации используется декоратор @property

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age >= 0:
            self.__age = age

    @property
    def name(self):
        return self.__name


# obj = User('Vasiliy', 92)
# print(obj.name)
# obj.name='Anton'

class Person:
    """
    Класс описівающий человека
    """
    __firstname = str()
    __lastname = str()
    __age = int()
    __email = str()
    __phone = str()

    @property
    def firstname(self):
        return self.__firstname.capitalize()

    @property
    def lastname(self):
        return self.__lastname.capitalize()

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @email.setter
    def email(self, email: str):
        self.__email = email

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    def __set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0

    def __init__(self, name: str, surname: str, age: int):
        self.__firstname = name
        self.__lastname = surname
        self.__set_age(age)

    def __str__(self):
        info = f'Name: {self.firstname}\nSurname: {self.lastname}\nAge: {self.age}\n'
        if self.email != '':
            info = f'{info}e-mail: {self.email}\n'
        if self.phone != '':
            info = f'{info}phone: {self.phone}'
        return info


obj = Person('a', 'b', 12)
print(obj)
obj.phone = '0890329875023789'
print(obj)
class Family:

    def __init__(self):
        self.father = Person()
        self.mother = Person()
        self.childs = []