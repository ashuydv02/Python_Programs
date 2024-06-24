numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)

numbers.append(6)
print("After appending 6:", numbers)

numbers.insert(2, 7)
print("After inserting 7 at index 2:", numbers)

print("Element at index 3:", numbers[3])

numbers[1] = 8
print("After modifying element at index 1 to 8:", numbers)

numbers.remove(4)
print("After removing element 4:", numbers)

del numbers[0]
print("After deleting element at index 0:", numbers)

if 7 in numbers:
    print("7 is in the list")

print("Length of the list:", len(numbers))

print("Iterating through the list:")
for num in numbers:
    print(num)

fruits = ["apple", "banana", "cherry"]

combined_list = numbers + fruits
print("Combined list:", combined_list)

numbers.sort()
print("Sorted numbers:", numbers)

numbers.reverse()
print("Reversed numbers:", numbers)

numbers.clear()
print("Cleared list:", numbers)

