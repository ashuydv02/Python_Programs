from enum import Enum, auto
 
class Friends(Enum):
    Ashish = 1
    Anil = 2
    Aswan = 3
    Abhishek = 4
    Ayush = 5

print(Friends.Ashish)
print(Friends.Ayush.name)
print(Friends.Aswan.value)
print(type(Friends.Anil))
print(repr(Friends.Aswan))
print(list(Friends))

print("Friend 1 : ", Friends(1).name)
print("The Number of Anil in enum class is ", Friends['Anil'].value)

print("List of Friends Stored in enum Class : ")
for friend in Friends:
    print(friend.value, "-", friend)

# We can use auto function to automatically assign integer values.
    
class Languages(Enum):
    Hindi = auto()
    English = auto()
    Marathi = auto()
    Punjabi = auto()
    Bhojpuri = auto()
    Kannad = auto()

for language in Languages:
    print(language, '-', language.value)
