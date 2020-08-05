class BankAccount:
    def __init__(self, int_rate= 0.01, balance=0):
        self.interest_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        # print(f"Balance is {self.account_balance}")
        print("Balance is " + str(self.account_balance))
        return self
        
    def yield_interest(self):
        self.account_balance += self.account_balance * self.interest_rate
        return self

account1= BankAccount(0.01, 100)
account1.deposit(1000).deposit(1500).deposit(2500).withdraw(1000).yield_interest().display_account_info()
# account1.deposit(200)
# print(account1.account_balance)
# account1.display_account_info()
# account1.yield_interest()
# account1.display_account_info()
# account1.withdraw(50)


account2= BankAccount(0.01, 0)
account2.deposit(1000).deposit(1500).deposit(2500).withdraw(1000).yield_interest().display_account_info()
# # print(account1.account_balance)
# account2.display_account_info()
# account2.yield_interest()
# account2.display_account_info()
