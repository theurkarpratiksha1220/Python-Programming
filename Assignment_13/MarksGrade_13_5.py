# Write a program which accepts marks and displays grade.
# Condition Example:
# -	>= 75  Distinction
# -	>= 60  First Class
# -	>= 50  Second Class
# -	< 50  Final
#-------------------------------------------------------------------------------------------------------

def GradeDisplay(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Final"  

def main():

    marks = float(input("Please Enter your Marks: "))
        
    if marks < 0 or marks > 100:
        print("Please enter valid Marks! Range should be 0  to 100")
    else:
        Grade = GradeDisplay(marks)
        print("Your Grade is : ", Grade)

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Please Enter your Marks: 75
#Your Grade is :  Distinction

#Please Enter your Marks: 67
#Your Grade is :  First Class

#Please Enter your Marks: 59
#Your Grade is :  Second Class

#Please Enter your Marks: 49.8
#Your Grade is :  Final

