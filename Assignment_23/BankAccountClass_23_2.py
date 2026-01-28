# Write a Python program to implement a class named BankAccount with the following requirements:
# - The class should contain two instance variables:
#       - Name (Account Holder Name)
#       - Amount (Account balance)
# - The class should contain one class variable:
#       - ROI (Rate of Interest, initialize to 10.5
# - Define a constructor(__init__) that accepts Name and initial Amount
# - Implement an instance methods:
#       - Display() - displays account holder name and current balance
#       - Deposit() - accepts an amount from the user and adds it to balalnce
#       - Withdraw() - accepts an amount from the user and subtracts it from balance 
#                      (ensure withdrawal is alloed only if sufficient balance exists)
#       - CalculateInterest() - calculates and return interest using formula:
#                   Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.
# ------------------------------------------------------------------------------------------------------------

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder Name: ", self.Name)
        print(f"Current Balance: ", self.Amount)

    def Deposit(self):
        Value = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + Value
        print(f"Deposited Amount: ", Value)

    def Withdraw(self):
        Value = float(input("Enter amount to withdraw : "))
        if Value <= self.Amount:
            self.Amount = self.Amount - Value
            print("Withdrawn Amount :", Value)
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest 

Obj1 = BankAccount("Prats", 10000)
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())
print("------------------------")

Obj2 = BankAccount("Venks", 15000)
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())
print("------------------------")

Obj2 = BankAccount("Rucha", 6000)
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())

# ------------------------------------------------------------------------------------------------------------
# Output -
# Account Holder Name:  Prats
# Current Balance:  10000
# Enter amount to deposit: 2000
# Deposited Amount:  2000.0
# Enter amount to withdraw : 3000
# Withdrawn Amount : 3000.0
# Interest: 945.0
# ------------------------
# Account Holder Name:  Venks
# Current Balance:  15000
# Enter amount to deposit: 1500
# Deposited Amount:  1500.0
# Enter amount to withdraw : 7000
# Withdrawn Amount : 7000.0
# Interest: 997.5
# ------------------------
# Account Holder Name:  Rucha
# Current Balance:  6000
# Enter amount to deposit: 1500
# Deposited Amount:  1500.0
# Enter amount to withdraw : 9000
# Insufficient balance
# Interest: 787.5