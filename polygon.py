class Rectangle:
    # Rectangle object with width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # String representation
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Drawing a picture of asterisks based on the object's shape
    def get_picture(self):
        i = 0
        picture = ""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        while self.height > i:
            i += 1
            picture += self.width * "*" + "\n"
        return picture

    # Calculating how many times a shape can fit into the initial object
    def get_amount_inside(self, shape):
        area1 = self.get_area()
        area2 = shape.get_area()
        if area2 > area1:
            return 0
        elif area1 > area2:
            return int(area1/area2)
        elif area1 == area2:
            return 1


# Square subclass of Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
