class Demo():
    __slots__ = ['a', 'b']

    def __init__(self, *args, **kwargs):
        self.a = 1
        self.b = 2


instance = Demo()
print(instance.__slots__)
print(instance.a)
print(instance.b)
try:
    print(instance.__dict__)
except Exception:
    print("Can't access the dictionary because we are using slots instead of dict.")
    try:
        instance.c = 5
        print(instance.c)
    except Exception:
        print("Can't add c or access it because c is not defined in slots.")
