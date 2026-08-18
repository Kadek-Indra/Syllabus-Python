def log_transaction(func):
    def wrapper(*args, **kwargs):
        print("\n--- Transaction Started ---")
        result = func(*args, **kwargs)
        print("--- Transaction Completed ---\n")
        return result
    return wrapper


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value <= 0:
            raise ValueError("Balance cannot be less than or equal to zero.")
        self._balance = value

    @log_transaction
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

        print(f"Deposited: {amount}")
        print(f"New balance: {self.balance}")

    @log_transaction
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount

        print(f"Withdrew: {amount}")
        print(f"New balance: {self.balance}")


account = BankAccount("Budi", 1_000_000)

print(f"Owner: {account.owner}")
print(f"Initial balance: {account.balance}")

account.deposit(500_000)

account.withdraw(300_000)

print(f"Final balance: {account.balance}")