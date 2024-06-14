# Define a metaclass
class MyMetaClass(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        if 'DemoFunction' not in dct:
            def DemoFunction(self):
                return f"{name} class has no method named Demo ."
            dct['DemoFunction'] = DemoFunction
        return super().__new__(cls, name, bases, dct)


# Define a class using the metaclass With no method named DemoFunction
class MyClass(metaclass=MyMetaClass):
    def __init__(self):
        print("Constructor")


# Define a class using the metaclass With a method named DemoFunction
class AnotherClass(metaclass=MyMetaClass):
    def DemoFunction(self):
        return "AnotherClass has Demo Method."


# Object the class
instance = MyClass()
print(instance.DemoFunction())
another = AnotherClass()
print(another.DemoFunction())
