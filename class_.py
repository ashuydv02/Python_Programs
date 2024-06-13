# We can also create the class function outside the class.
def demo_function(self,x,y):
    return x+y

class demo:
    id = 0
    ls = []
    class_function = demo_function
    
    def __init__(self, name):
        self.employee_name = name
        print(self.employee_name)
        self.another_ls = []

    def set_ls(self, value):
        self.ls.append(value)

    def set_another_ls(self, value):
        self.another_ls.append(value)


object_ = demo("Ashish")
object_1 = demo("Anil")
object_.id = 10
object_1.id = 20
object_.set_ls("Anil")
object_1.set_ls("Ashish")
object_.set_another_ls("Anil")
object_1.set_another_ls("Ashish")
print(object_.ls)
print(object_1.ls)
print(object_.another_ls)
print(object_1.another_ls)
print(object_.id)
print(object_1.id)
print(object_1.class_function(4,5))
