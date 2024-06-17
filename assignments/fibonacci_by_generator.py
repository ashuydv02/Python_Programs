# Write a generator function to generate Fibonacci numbers
def fabonacci_series(n):
    x = 0
    y = 1
    while n > x:
        yield x
        x, y = y, x + y


for fabonacci in fabonacci_series(50):
    print(fabonacci)
