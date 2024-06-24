def generator(n):
    value=0
    while value<n:
        yield value 
        value += 1

# print(generator(5))
# for i in generator(5):
#     print(generator(5))
#     print(i)

generator_obj = generator(5)
print(next(generator_obj))  # 0
print(next(generator_obj))  # 1
print(next(generator_obj))  # 2
print(next(generator_obj))  # 3
print(next(generator_obj))  # 4


# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
# for i in squares_generator:
#     print(i)
print(next(squares_generator))
print(next(squares_generator))
print(next(squares_generator))
