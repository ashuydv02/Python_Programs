# Simple Context Manager Class Flow
class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def show(self):
        print("Running...")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

# with ContextManager() as manager:
#     print('with statement block')
#     manager.show()


# Opening File with the help of Context Manager class
class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


print("Files Data : ")
with FileManager('tempFile.txt', 'a') as managerObject:
    managerObject.write('\n\t Junior SoftWare Engineer')
    print('End Of File...')
print(managerObject.closed)
