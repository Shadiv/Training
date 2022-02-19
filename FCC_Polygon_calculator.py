class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(1/2)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            picture += self.width*'*'+'\n'
        return picture

    def get_amount_inside(self, shape):
        if shape.width > self.width or shape.height > self.height:
            return 0
        else:
            s = shape.width*shape.height
            return self.get_area() // s

class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width, height=width)
        self.width = width
        self.height = self.width

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.width = width
        self.height = width

a = Rectangle(4,5)
b = Square(4)
print(a.get_area())
a.set_width(6)
print(a.get_area())
a.set_height(8)
print(a.get_picture())
print(b.width)
print(b.height)
b.set_width(4)
b.set_height(6)
b.set_side(5)
print(b.get_area())
print(b.get_picture())
