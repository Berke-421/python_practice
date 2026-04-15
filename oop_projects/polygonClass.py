import random
import math
from fractional_and_nonfractional_floats import AutonumberFloat

class Polygon:
    __pi = math.pi
    __auto = AutonumberFloat()

    def __init__(self, edge, side_length):
        try:
            self.edge = edge
            if self.edge <= 2: raise ValueError
        except ValueError:
            print("")
            self.edge = float(random.randint(3, 8))

        try:
            self.sideLength = side_length
            if self.sideLength <= 0: raise ValueError
        except ValueError:
            print("")
            self.sideLength = self.__auto.maybe_float_one_third(1, 20)

    def area(self):
        a = (self.edge * self.sideLength**2) / (4 * math.tan(math.pi/self.edge))
        return a

    def perimeter(self):
        p = self.edge * self.sideLength
        return p

    def angle(self):
        a = (self.edge - 2) * 180
        return a