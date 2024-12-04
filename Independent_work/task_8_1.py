class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def circle_length(self):
        return 2 * 3.14 * self.__radius

    def circle_area(self):
        return 3.14 * self.__radius ** 2


class Square:

    def __init__(self, side):
        self.__side = side

    def square_perimeter(self):
        return 4 * self.__side

    def square_area(self):
        return self.__side ** 2


class CircleInSquare(Circle, Square):

    def __init__(self, side):
        Circle.__init__(self, side / 2)
        Square.__init__(self, side)

    def get_circle_in_square(self):
        return (f"Длина круга - {self.circle_length()}\n"
                f"Площадь круга - {self.circle_area()}\n"
                f"Периметр квадрата - {self.square_perimeter()}\n"
                f"Площадь квадрата - {self.square_area()}")


circle_in_square = CircleInSquare(10)
print(circle_in_square.get_circle_in_square())
