import pickle

data = {'name': 'ashish', 'age': 22}
byte_data = pickle.dumps(data)
print(byte_data)
print(pickle.loads(byte_data))

with open('pickling.txt', 'wb') as file:
    pickle.dump(data, file)

with open('pickling.txt', 'rb') as file:
    file_data = pickle.load(file)

print(file_data)
