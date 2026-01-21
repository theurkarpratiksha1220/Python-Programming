# Write a program which accepts one number and prints cube of that number
#-------------------------------------------------------------------------------------------------------

def Cube(Value):                                  
    Ans = 0.0
    Ans = Value ** 3                                    
    return Ans

def main():
    No = 0
    Result = 0

    No = float(input("Enter Number : "))         

    Result = Cube(No) 
    print(Result)

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
# Enter Number : 5
# 125.0

# Enter Number : 5.5
# 166.375
