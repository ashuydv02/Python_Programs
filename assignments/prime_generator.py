# Create a generator that yields prime numbers
def prime_number(n):
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            yield i


for numbers in prime_number(47):
    print(numbers)
