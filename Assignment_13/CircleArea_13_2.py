# Write a program which accepts radius of circle and prints area of circle.
#-------------------------------------------------------------------------------------------------------

import math

def AreaCircle(Value):                                   
    Ans = 0.0
    Ans = math.pi *  Value * Value                     
    return Ans

def main():

        Radius = float(input("Enter Radius of a Circle : ")) 

        if Radius < 0:
             print("Not accepted!")
        else:
             Area = AreaCircle(Radius)
             print("Area of a Circle is :", Area)

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter Radius of a Circle : 5
#Area of a Circle is : 78.53981633974483