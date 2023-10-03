class Point:
    color = 'white'
    def __init__(self, point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

    @property
    def point_a(self):
        return self.__point_a
    @point_a.setter
    def point_a(self, value):
        if value < 0:
            raise ValueError("Value can't be negative")
        self.__point_a = value

    @property
    def point_b(self):
        return self.__point_b
    @point_b.setter
    def point_b(self,value):
        if value < 0:
            raise ValueError("Value can't be negative")
        self.__point_b = value
    def __add__(self, other):
        return (self.__point_a + other.__point_a, self.__point_b + other.__point_b)


p1 = Point(1,2)
p2 = Point(1,2)
print(p1 + p2)