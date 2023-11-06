class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

    


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print("My breed is {} and I can Woof".format(self.breed))


class Cat(Animal):
    def __init__(self, name, breed):
        self.name = name
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print("My breed is {} and I can Meow".format(self.breed))


if __name__ == "__main__":
    animal = Animal("Simba")
    cat = Cat("Pussy", "Bengal")
    dog = Dog("Razmus", "Portugese")

    animal.speak()
    cat.speak()
    dog.speak()
