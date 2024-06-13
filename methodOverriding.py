class Animal:
    def eat(self):
        print('I can eat.')

class Dog(Animal):
    name = ''

    def eat(self):
        super().eat()
        print(f"{Dog.name} like to eat bones.")

dog = Dog()
Dog.name = "BullDog"
dog.eat()
