# Write a Python program to implement a class named Numbers with the following specifications:
# - The class should contain one instance variable:
#       - Value
# - Define a constructor(__init__) that accepts a number from user and initializes Value
# - Implement an instance methods:
#       - ChkPrime() - returns True if the number is prime, otherwise returns False
#       - ChkPerfect() - returns True if the number is perfect, otherwise returns False
#       - Factors() - display all factors of the number
#       - SumFactors() - returns the sum of all factors
#.           (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.
# ------------------------------------------------------------------------------------------------------------

class Numbers:

    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print(f"Factors of {self.Value} are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total = total + i
        return total

    def ChkPerfect(self):
        return (self.SumFactors() - self.Value) == self.Value

obj1 = Numbers()
print("Number:", obj1.Value)
print("Is Prime:", obj1.ChkPrime())
print("Is Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())
print("--------------------------------")

obj2 = Numbers()
print("Number:", obj2.Value)
print("Is Prime:", obj2.ChkPrime())
print("Is Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())

# ------------------------------------------------------------------------------------------------------------
# Output -
# Enter a number: 28
# Number: 28
# Is Prime: False
# Is Perfect: True
# Factors of 28 are:
# 1 2 4 7 14 28 
# Sum of Factors: 56
# --------------------------------
# Enter a number: 17
# Number: 17
# Is Prime: True
# Is Perfect: False
# Factors of 17 are:
# 1 17 
# Sum of Factors: 18