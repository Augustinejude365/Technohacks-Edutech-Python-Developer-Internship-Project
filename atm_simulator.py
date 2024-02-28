#!/usr/bin/env python3

class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"
        else:
            return "Invalid amount. Please deposit a positive number."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid amount. Please withdraw a positive number."


if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")
        if choice == '1':
            print("Your balance is:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
