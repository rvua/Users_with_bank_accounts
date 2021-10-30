class BankAccount:
    accounts = []
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) > 0:
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

class User: 
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0, 0.3)
    
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        print(self.account.balance)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}.")

richard = User("Richard")
richard.make_deposit(100)
richard.make_deposit(150)
richard.make_deposit(20)
richard.make_withdrawal(30)
richard.display_user_balance()