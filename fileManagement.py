print("Accessing the files data : ")

# Opening File with context manager 'with'
# Opening file in read mode.
with open('tempFile.txt', 'r') as file:
    print(file.read())

# Normal method to open file.
# Opening file in write mode.
pointer = open('tempFile.txt', 'w')
pointer.write('Ashish Yadav is a junior software engineer\n')
pointer.close()

# opening file in append mode
with open('tempFile.txt', 'a') as file:
    file.write('Ashish is from district Sehore.')

# Opening file in both read and write mode by just adding + with modes.
with open('tempFile.txt', 'r+') as file:
    file.seek(0)
    for line in file.readlines():
        print(line, end='')
    else:
        print()
    file.seek(0)
    data = ['My Name is Ashish Yadav\n',
            'I am from Nasrullaganj\n', 'I am a Software Engineer']
    for line in data:
        file.write(line)
