person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

person["job"] = "Engineer"
print("After adding job:", person)

person["age"] = 32
print("After modifying age:", person)

del person["city"]
print("After deleting city:", person)

if "name" in person:
    print("Name is present")

print("Length of the dictionary:", len(person))

print("Iterating through keys:")
for key in person:
    print(key)

print("Iterating through values:")
for value in person.values():
    print(value)

print("Iterating through key-value pairs:")
for key, value in person.items():
    print(key, ":", value)

person.clear()
print("Cleared dictionary:", person)
