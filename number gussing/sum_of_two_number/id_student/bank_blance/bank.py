class BankAccount:
    def __init__(self, account_number, name, balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.pin:
            print("Incorrect PIN! Withdrawal denied.")
            return

        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")

    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


# Example usage
acc1 = BankAccount(24362783, "Vivek", 1000, 350034)

acc1.deposit(67887)            # Deposit money
acc1.withdraw(300, 350034)    # Correct PIN
acc1.withdraw(200, 1111)    # Wrong PIN
acc1.show_balance()         # Show balance