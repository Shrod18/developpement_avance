class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} fait un son.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} aboie !")

class Cat(Animal):
    def speak(self):
        # print(f"{self.name} miaule !")
        super().speak()
        print("Meow !")

