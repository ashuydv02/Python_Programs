class Animal:
    name = ''

    def eat(self):
        print('I can eat.')

class Dog(Animal):
    def eat(self):
        super().eat()
        print(f"{self.name} like to eat bones.")

dog = Dog()
dog.name = "BullDog"
dog.eat()
