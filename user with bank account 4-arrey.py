class BankAccount:
    def __init__(self, int_rate= 0.02, balance=0):
        self.interest_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insuficient funds")
        return self

    def display_account_info(self):
        print("Balance is " + str(self.account_balance))
        return self
        
    def yield_interest(self):
        self.account_balance += self.account_balance * self.interest_rate
        return self

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
        # self.add_account["saving"]


    def add_account(self, account_number, int_rate=0.02, balance=0):
        newAccount = BankAccount(int_rate, balance)
        self.accounts.append(newAccount)  # if using a list
        return self

    def make_deposit(self, account_number, amount):
        self.accounts[account_number].deposit(amount)
        self.display_user_balance(account_number)
        return self

    def make_withdrawal(self, account_number, amount):
        self.accounts[account_number].withdraw(amount)

    def display_user_balance(self, account_number):
        print ( f"{self.name}, account number: {account_number}, balance: {self.accounts[account_number].account_balance}" )


ani = User("ani pilosian", "a@p.gmail.com")
ani.add_account(0, 0.02, 0)
ani.make_deposit(0, 500)
# print(ani.accounts[0])
ani.display_user_balance(0)
# ani.display_user_balance
# ani.add_account(int_rate=0.01, balance=5000)
# print(ani.accounts)
# print(ani.display_user_balance[0])





