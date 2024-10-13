class circle:
    def __init__(self,radius):
        self.radius = radius

    def  area(self):
        return 3.14* (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


radius = float(input("Enter the radius of the circle:"))


circle = circle(radius)


print(f"Area of the circle: {circle.area()}")
print(f"Area of the perimeter: {circle.perimeter()}")