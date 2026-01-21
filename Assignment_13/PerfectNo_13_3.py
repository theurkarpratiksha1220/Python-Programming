# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number
#-------------------------------------------------------------------------------------------------------

def PerfectNo(Value):                                   
    if Value <= 0:
         return False
    
    SumofDivisors = 0
    for i in range(1, Value):
         if Value % i == 0:
              SumofDivisors = SumofDivisors + i
    
    return SumofDivisors == Value

def main():

        No = int(input("Enter Any Number : ")) 

        if PerfectNo(No):
             print("Perfect Number")
        else:
             print("Not a Perfect Number")

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
#Enter Any Number : 6
#Perfect Number

#Enter Any Number : 12
#Not a Perfect Number