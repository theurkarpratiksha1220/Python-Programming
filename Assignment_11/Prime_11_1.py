# Write a program which accepts one number and checks whether it is prime or not. 
# Input: 11
# Output: Prime Number
#-------------------------------------------------------------------------------------------------------

def Prime(Value):                                     
    if Value <= 1:
        return False
    for i in range(2, Value):
            if Value % i == 0:
                return False
    return True
           
def main():
    No = 0
                                              
    No = int(input("Enter Number : "))            
        
    if Prime(No):                              
        print("Prime Number")
    else:
        print("Not a prime Number")
        
if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
#Output
#Enter Number : 4
#Not a prime Number

#Enter Number : 11
#Prime Number

