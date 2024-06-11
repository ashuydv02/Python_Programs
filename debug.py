# import pdb

# def add(a, b):
#     result = a + b
#     return result

# def subtract(a, b):
#     result = a - b
#     return result

# def main():
#     x = 5
#     y = 3
#     pdb.set_trace()  # Start the debugger here
#     addition = add(x, y)
#     subtraction = subtract(x, y)
#     print(f"Addition: {addition}, Subtraction: {subtraction}")

# if __name__ == "__main__":
#     main()

# import pdb

# try:
#     1 / 0
# except ZeroDivisionError:
#     pdb.post_mortem()

print('Hello WOrld!')
breakpoint()
a, b = 5, 10
a = a + b
print(a)