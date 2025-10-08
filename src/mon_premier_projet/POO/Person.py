class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age cannot be negative")
        self.__age = age
