# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel
#-------------------------------------------------------------------------------------------------------

def VowelConsonant(Value):                                    
    return Value in ['a', 'e', 'i', 'o', 'u']                                       
           
def main():
    CharValue = input("Enter Any Character : ").lower()

    if len(CharValue) != 1 or not CharValue.isalpha():
        print("Please enter valid value")
        return
    
    Result = VowelConsonant(CharValue)                          

    if Result:
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter Any Character : A
#Vowel

#Enter Any Character : a
#Vowel

#Enter Any Character : 1
#Please enter valid value

#Enter Any Character : @
#Please enter valid value

#Enter Any Character : b
#Consonant