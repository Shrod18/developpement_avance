class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} fait un son.")

def mon_decorateur(func):
    def wrapper(*args, **kwargs):
        print("Avant l'appel de la fonction")
        func(*args, **kwargs)
        print("Après l'appel de la fonction")
    return wrapper


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    @mon_decorateur
    def speak(self):
        print(f"{self.name} aboie !")

class Cat(Animal):
    def speak(self):
        # print(f"{self.name} miaule !")
        super().speak()
        print("Meow !")

