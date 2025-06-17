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

    def deposite(self):
