class Money:
    def __init__(self): #init is a default method for a class
        self.balance = 0 # cuz ur initializing it so it starts from 0
    
    def withdraw(self, wAmount): #every def needs self to access the init method
        if wAmount < self.balance:
            self.balance -= wAmount
            return self.balance
        else:
            return f"balance is missing {wAmount - self.balance}"
        
    def deposit(self, dAmount):
        self.balance += dAmount
        return self.balance

user1 = Money()
print(user1.withdraw(80))
