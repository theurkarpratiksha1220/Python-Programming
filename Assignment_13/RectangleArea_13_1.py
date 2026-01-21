# Write a program which accepts length and width of rectangle and prints area.
#-------------------------------------------------------------------------------------------------------

def AreaRectangle(Value1, Value2):                                   
    Ans = 0.0
    Ans = Value1 * Value2                         
    return Ans

def main():

        Length = float(input("Enter Length of a Rectangle : ")) 
        Width = float(input("Enter Width of a Rectangle  : ")) 

        PrintArea = AreaRectangle(Length,Width)                       
        print("Area of a Rectangle is : ", PrintArea)

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
#Enter Length of a Reactangle : 12
#Enter Width of a Reactangle  : 12
#Area of a Rectangle is :  144.0
