# Write a python program to implement a class named Arithmetic with the following characteristics:
# - The class should contain two instance variables: Value1 and Value2.
# - Define a constructor (__init__) that initializes all instance variables to 0
# - Implement the following instance methods:
#   Accept() - accepts values for Value1 and Value2 from the user.
#   Addition() - returns the addition of Value1 and Value2.
#   Subtraction() - returns the Subtraction of Value1 and Value2.
#   Multiplication() - returns the Multiplication of Value1 and Value2.
#   Division() - returns the division of Value1 and Value2(handle division by zero properly)
# Create multiple objects of the Arithmetic class and invoke all the instance methods.
# ---------------------------------------------------------------------------------------------------------

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number : "))
        self.Value2 = int(input("Enter Second Number : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not allowed"
        return self.Value1 / self.Value2

Obj1 = Arithmetic()
Obj2 = Arithmetic()

Obj1.Accept()
print("Addition is :", Obj1.Addition())
print("Subtraction is:", Obj1.Subtraction())
print("Multiplication is:", Obj1.Multiplication())
print("Division is :", Obj1.Division())
print("-----------------------------")

Obj2.Accept()
print("Addition is :", Obj2.Addition())
print("Subtraction is:", Obj2.Subtraction())
print("Multiplication is:", Obj2.Multiplication())
print("Division is :", Obj2.Division())
print("-----------------------------")

# ---------------------------------------------------------------------------------------------------------
# Output -
# Enter First Number : 15
# Enter Second Number : 5
# Addition is : 20
# Subtraction is: 10
# Multiplication is: 75
# Division is : 3.0
# -----------------------------
# Enter First Number : 100
# Enter Second Number : 52
# Addition is : 152
# Subtraction is: 48
# Multiplication is: 5200
# Division is : 1.9230769230769231