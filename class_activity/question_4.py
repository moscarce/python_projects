import math

# area = math.pi * 1.1 ** 2
# print(f'{area:.2f}')

class CircleArea:
    def area_of_circle(self,radius):
        if radius < 0:
            raise ValueError
        if type(radius) is not int:
            raise TypeError
        return math.pi * radius ** 2



