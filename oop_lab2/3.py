
class Account:
    def __init__(self, accNo, accHolder, amount):
        self.accountNumber = accNo
        self.accountHolder = accHolder
        self.accountAmount = amount

    def deposit(self):
        depAmount = int(input("Enter the amount to deposit : "))
        self.accountAmount += depAmount
        print(f"Amount deposited : {depAmount}")
        print(f"New Balance : {self.accountAmount}")

    def withdraw(self):
        withAmount = int(input("Enter the amount to withdraw : "))
        if withAmount > self.accountAmount:
            print("Your Account don't have sufficient ammount !!")
            return -1
        self.accountAmount -= withAmount
        print(f"Amount withdraw : {withAmount}")
        print(f"New Balance : {self.accountAmount}")
        return withAmount

    def checkBalance(self):
        print(f"Balance : {self.accountAmount}")
        return self.accountAmount

    def getDetails(self):
        print(f"Account Number : {self.accountNumber}")
        print(f"Account Holder : {self.accountHolder}") 
        print(f"Balance : {self.accountAmount}")
        return self.accountNumber, self.accountHolder, self.accountAmount

N = Account(711, "tushar", 30000)
N.deposit()
withdraw = N.withdraw()
balance = N.checkBalance()
details = N.getDetails()