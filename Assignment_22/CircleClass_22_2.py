# Write a python program to implement a class named Circle with the following requirements:
# - The class should contain three instance variables: Radius, Area and Circumference.
# - The class should contain one class variable named PI, initialized to 3.14.
# - Define a constructor (__init__) that initializes all instance variables to 0.0.
# - Implement the following instance methods:
#   Accept() - accepts the radius of the circle from the user.
#   CalculateArea() - calculate the area of the circle and stores it in the Area variable.
#   CalculateCircumference() - calculate the circumference of the circle and stores it in the Circumferenece variable.
#   Display() - displays the values of Radius, Area, and Circumference. 
# Create multiple objects of the Circle class and invoke all the instance methods for each object.
# ---------------------------------------------------------------------------------------------------------

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius of the Circle : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of a Circle : ", self.Radius)
        print("Area of a Circle : ", self.Area)
        print("Circumference of a Circle : ", self.Circumference)
        print("----------------------------------")

Obj1 = Circle()
Obj2 = Circle()

Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()

# ---------------------------------------------------------------------------------------------------------
# Output -
# Enter Radius of the Circle : 2.5
# Radius of a Circle :  2.5
# Area of a Circle :  19.625
# Circumference of a Circle :  15.700000000000001
# ----------------------------------
# Enter Radius of the Circle : 5
# Radius of a Circle :  5.0
# Area of a Circle :  78.5
# Circumference of a Circle :  31.400000000000002
