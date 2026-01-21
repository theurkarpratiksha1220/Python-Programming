# Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5
#-------------------------------------------------------------------------------------------------------

def Divisible(Value):     
    Ans = 0
    Ans = (Value % 3 == 0) and (Value % 5 == 0)            
    return Ans

def main():
    No = 0                               
    No = int(input("Enter Number : "))        

    if Divisible(No):                            
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
# Enter Number : 15
# Divisible by 3 and 5

# Enter Number : 9
# Not Divisible by 3 and 5