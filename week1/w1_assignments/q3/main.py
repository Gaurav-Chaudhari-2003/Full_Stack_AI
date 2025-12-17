# 3)Simple Bank Account Class
# Topics: Class, Member Functions, Data Members
# Problem:
# Create a BankAccount class with:
# deposit()
# withdraw()
# check_balance()
# Create an object and perform all operations, printing results.



class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f'Withdrew: {amount}'
        return f"Withdraw of {amount} unsuccessful"

    def deposit(self, amount):
        if 0 < amount:
            self.balance += amount
            return f'Deposited: {amount}'
        return 'Deposit Failed'

    def show_balance(self):
        return f'Balance: {self.balance}'


acc1 = BankAccount(100)
print(acc1.show_balance())
print(acc1.withdraw(101))
print(acc1.deposit(1))
print(acc1.show_balance())
print(acc1.withdraw(101))
print(acc1.show_balance())

