class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, width, height):
        if width == height:
            super().__init__(width, height)
        else:
            print("Not a square as width and height should be the same")

# return the area of rectangle
rec = Rectangle(2, 3)
print(rec.get_area())

# return the area of square
sq = Square(5, 5)
print(sq.get_area())

sq = Square(5, 6)
print(sq.get_area())
