import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    @property
    def diameter(self):
        return 2 * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Can only add a Circle to another Circle")

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        else:
            raise TypeError("Can only compare a Circle to another Circle")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError("Can only compare a Circle to another Circle")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Can only compare a Circle to another Circle")

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        else:
            raise TypeError("Can only compare a Circle to another Circle")

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        else:
            raise TypeError("Can only compare a Circle to another Circle")

# Example usage
c1 = Circle(radius=5)
c2 = Circle(diameter=10)
print(c1.radius)  
print(c1.diameter)  
print(c1.area()) 
print(c1)  
print(repr(c1)) 
print(c1 + c2)  
print(c1 > c2)  
print(c1 == c2)  
print(c1 < c2)  
circles = [Circle(radius=3), Circle(radius=1), Circle(radius=2)]
print(sorted(circles))  