class Animal:
    def __init__(self, animal):
        self.animal = animal

    def speak(self):
        print(f"{self.animal} fait un son.")

class Dog(Animal):
    def speak(self):
        print(f"{self.animal} aboie !")

class Cat(Animal):
    def speak(self):
        print(f"{self.animal} miaule !")