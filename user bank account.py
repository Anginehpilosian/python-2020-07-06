
# Create a file with the User class, including the __init__ and make_deposit methods
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
    	self.account_balance += amount

#  Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount

#  Add a display_user_balance method to the User class
    def display_user_balance(self):
        print (f"{self.name} balance is {self.account_balance}")

#  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self, amount, other_user):
        self.display_user_balance()
        other_user.display_user_balance()
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


#  Create 3 instances of the User class
# 1
ani = User("ani pilosian", "a@p.gmail.com")
print (ani.name , ani.email)

#  Have the first user make 3 deposits and 1 withdrawal and then display their balance
ani.make_deposit(100)
ani.make_deposit(500)
ani.make_deposit(50)
ani.make_withdrawal(200)
print(ani.name, ani.account_balance)

# #  Have the second user make 2 deposits and 2 withdrawals and then display their balance
# # 2

ara = User("ara pilosian", "a@p.gmail.com")

ara.make_deposit(100)
ara.make_deposit(500)
ara.make_withdrawal(50)
ara.make_withdrawal(200)
print(ara.name, ara.account_balance)

# 3
#  Have the third user make 1 deposits and 3 withdrawals and then display their balance
vana = User("vana pilosian", "v@p.gmail.com")


vana.make_deposit(500)
vana.make_withdrawal(50)
vana.make_withdrawal(200)
vana.make_withdrawal(20)
print(vana.name, vana.account_balance)

ani.transfer_money(30, vana)

ani.display_user_balance()
