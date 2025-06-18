# 🔸 2. Bank Account Class
# Question:
# Create a class BankAccount with attributes: account_holder, balance.
# Add methods to:
#
# deposit(amount)
#
# withdraw(amount)
#
# display_balance()
#
# Make sure withdrawal doesn't allow balance to go negative.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        # return self.balance

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            # return self.balance
        else:
            print("You don't have enough money!")
    def display_balance(self):
        print(f"Your current balance is : {self.balance}")


bankaccount=BankAccount("Sudesh",20000)
# bankaccount.deposit(10000)
bankaccount.withdraw(200000)
bankaccount.display_balance()
