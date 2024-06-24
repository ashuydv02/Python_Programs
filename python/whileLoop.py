# Example 1: Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Example 2: Using a condition with a while loop
number = 1
while number <= 10:
    print(number)
    number += 2

# Example 3: Infinite loop with break statement
number = 1
while True:
    print(number)
    number += 1
    if number > 10:
        break

# Example 4: Nested while loops
outer = 1
while outer <= 3:
    inner = 1
    while inner <= 3:
        print(outer, inner)
        inner += 1
    outer += 1

# Example 5: While loop with else clause
number = 1
while number <= 5:
    print(number)
    number += 1
else:
    print("End of loop")

