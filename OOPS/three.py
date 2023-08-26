from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.date_of_opening = datetime.now().date()
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Please enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Please enter a valid amount to withdraw.")

    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nCustomer Name: {self.customer_name}\nBalance: ${self.balance}\nDate of Opening: {self.date_of_opening}"

account1 = BankAccount("12345678", "John Doe", 1000)
print(account1)

account1.deposit(500)
account1.withdraw(200)
print(f"Current Balance: ${account1.check_balance()}")
