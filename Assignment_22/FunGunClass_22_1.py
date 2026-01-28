# Write a python program to implement a class named Demo with the following specifications:
# - The class should contain two instance variables: no1 and no2.
# - The class should contain one class variable named Value.
# - Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# - Implement two instance methods:
#   Fun() - displays the values of instance variables no1 and no2.
#   Gun() - displays the values of instance variables no1 and no2.
# Create two objects of the Demo class as follows:
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)
# Call the instance methods in the given sequence:
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()
# ---------------------------------------------------------------------------------------------------------

class Demo:
    Value = 10

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print("Inside instance method Fun",self.No1, self.No2)

    def Gun(self):
        print("Inside instance method Gun",self.No1, self.No2)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

# ---------------------------------------------------------------------------------------------------------
# Output -
# Inside instance method Fun 11 21
# Inside instance method Fun 51 101
# Inside instance method Gun 11 21
# Inside instance method Gun 51 101