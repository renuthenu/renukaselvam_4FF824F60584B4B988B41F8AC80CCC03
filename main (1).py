class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account balance for {self._account_holder_name}: ${self._account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    account = BankAccount("12345", "John Doe", 1000)

    account.display_balance()  # Display initial balance
    account.deposit(500)       # Deposit $500
    account.withdraw(200)      # Withdraw $200
    account.display_balance()  # Display updated balance