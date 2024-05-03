#!/usr/bin/python3

class Square():
    """ This is a square class object """
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """Initialization of the class object"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ printing the width and height of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=10, height=17)
    print(s)
    print(s.area_of_my_square())
    print(s.perimit_of_my_square())