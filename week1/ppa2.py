class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def Is_valid(self):
        if self.a + self.b <= self.c:
            return "Invalid"
        if self.b + self.c <= self.a:
            return "Invalid"
        if self.a + self.c <= self.b:
            return "Invalid"
        return "Valid"

    def Side_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"

        if self.a == self.b == self.c:
            return "Equilateral"

        if self.a == self.b or self.b == self.c or self.c == self.a:
            return "Isosceles"

        return "Scalene"

    def Angle_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"

        side = sorted([self.a, self.b, self.c])
        x, y, z = side

        if x * x + y * y > z * z:
            return "Acute"

        if x * x + y * y == z * z:
            return "Right"

        if x * x + y * y < z * z:
            return "Obtuse"

    def Area(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"

        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


a = int(input())
b = int(input())
c = int(input())

T = Triangle(a, b, c)

print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
