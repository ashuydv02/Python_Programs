def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError as e:
        print(f"Error: {e}")
    else:
        print(f"The result of {x} divided by {y} is: {result}")
    finally:
        print("End of divide function\n")

divide(10, 0)

divide(10, '2')

divide(10, 2)

# Example of custom exception in Python

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'CustomError: {self.message}'

def validate_age(age):
    if age < 0 or age > 120:
        raise CustomError("Age must be between 0 and 120")

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print(f"Your age is: {age}")
except ValueError:
    print("Error: Please enter a valid integer for age")
except CustomError as ce:
    print(ce)
