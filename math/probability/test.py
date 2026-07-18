#!/usr/bin/python3
"""Module about rectangle class and its methods and attributes"""


class Rectangle:
    """
    This creates the rectangle class.
    A closed figure of 4 sides, the opposite ones are of equal length.
    Aditionally, all angles are 90°.
    """
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """Class method that returns a square"""
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        Args:
            width:
            height:
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        getter method for height
        Args: self

        Returns: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height
        Args:
            self:
            value: integer >= 0 necessary for rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """
        getter method for width.
        Argument: self
        Returns: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width
        Args:
            self
            value: integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def area(self):
        """This returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        "This returns the rectangle perimeter"
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def print(self):
        """This method prints the rectangle with the character '#'"""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(0, self.__height):
            print(str(self.print_symbol) * self.__width)

    def __str__(self):
        """This method prints the rectangle with the character '#'"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(0, self.__height - 1):
            string += str(self.print_symbol)*self.__width+"\n"
        string += str(self.print_symbol)*self.__width
        return string

    def __repr__(self):
        """This method returns a represenation like "Rectangle(X, Y).
        With X and Y being width and height"""
        return "Rectangle(" + str(self.__width) + ", " \
               + str(self.__height) + ")"

    def __del__(self):
        """This method deletes the class and sends a good-bye"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del (self)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method returns the bigger of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
