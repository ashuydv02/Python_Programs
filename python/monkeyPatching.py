from moduleForSquare import Square
from unittest.mock import patch


def square(self, a):
    return a * a * a


# Square.square = square
# obj = Square()

# print(obj.square(5))

# Use Patch to temporarily replace the square method
with patch.object(Square, 'square', square):
    square_obj = Square()
    print(square_obj.square(5))


square_obj = Square()
print(square_obj.square(5))
