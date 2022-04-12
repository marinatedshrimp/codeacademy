class BankAccount:
    def __init__(self, accNum, name, balance):
        self.accNum = accNum
        self.name = name
        self.balance = balance

    def deposit(self, damount):
        print(f"Deposited Amount: {damount}")
        self.balance += damount
        print(f"Current Balance: {self.balance + damount}\n")

    def withdraw(self, wamount):
        print(f"Withdrawn Amount: {wamount}")
        self.balance -= wamount
        print(f"Current Balance: {self.balance + wamount}\n")

    def bankFees(self, fee = 0.05):
        return self.balance * (1 - fee)

    def display(self):
        print("Account Information:")
        print(f"Account Number: {self.accNum}")
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")

a = BankAccount("0989789", "Roxy Coxy", 17800)
a.deposit(4000)
a.display()
