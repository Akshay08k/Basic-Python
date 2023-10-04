import sys

class bank(object):
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdrawls(self,amount):
        if amount > self.balance:
            print("Insufficient Balance..")
        else:
            self.balance -= amount
            return self.balance
        
name = input("Enter Number Of Customer : ")
b = bank(name)


while True:
    print("d/D-deposit,w/W-Withdraw,e/E-exit")
    choice = input("Enter Your Choice : ")
    if choice == "e" or choice == "E":
        sys.exit()
    if choice == "d" or choice == "D":
        amount = float(input("Enter Your Amount : "))
        print("Balance after depositing account = ",b.deposit(amount))
    elif choice == "w" or choice == "W":
           amount = float(input("Enter Your Amount : "))
           print("Balance after withdrawinig account = ",b.withdrawls(amount))
       
