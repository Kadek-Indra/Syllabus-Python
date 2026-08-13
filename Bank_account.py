class BankAccount:
    def __init__(self, balance, account_info):
        self.balance = balance
        self.account_info = account_info

    def display_info(self):
        print(f"Account Number : {self.account_info.account_number}")
        print(f"Owner Name     : {self.account_info.owner_name}")
        print(f"Balance        : {self.balance}")

    class AccountInfo:
        def __init__(self, account_number, owner_name):
            self.account_number = account_number
            self.owner_name = owner_name

account1 = BankAccount(1000, BankAccount.AccountInfo("123456789", "John Doe"))
print("=== BANK ACCOUNT INFORMATION ===")
account1.display_info()
