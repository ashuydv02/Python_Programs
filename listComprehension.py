numbers = [1, 2, 3, 4, 5]

square_numbers = [num * num for num in numbers]
print(square_numbers)

# List comprehension with if else

even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# finding vowels from the word

word = input("Enter the word : ")
vowels = "aeiouAEIOU"
result = [char for char in word if char in vowels]

print(result)
