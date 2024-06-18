class Demo:
    _objects = None

    def __new__(cls):
        if cls._objects is None:
            cls._objects = super().__new__(cls)
        return cls._objects

    def __init__(self):
        print(self)

    def display(self, data):
        print(self)
        return data


obj1 = Demo()
obj2 = Demo()
print(obj1.display("Object 1"))
print(obj2.display("Object 2"))
