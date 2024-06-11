fruits = ("apple", "banana", "cherry", "apple")

print(fruits)

print("First element:", fruits[0])
print("Last element:", fruits[-1])

print("Count of 'apple':", fruits.count("apple"))

print("Index of 'banana':", fruits.index("banana"))

print("Iterating through the tuple:")
for fruit in fruits:
    print(fruit)

coordinates = (3, 5)
x, y = coordinates
print("x coordinate:", x)
print("y coordinate:", y)
