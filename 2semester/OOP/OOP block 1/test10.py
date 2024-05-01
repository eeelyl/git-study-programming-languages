class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with initial balance {initial_balance}")
        else:
            print("Account already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} to account {account_number}. New balance: {self.accounts[account_number]}")
        else:
            print("Account does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account does not exist.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account] >= amount:
                self.accounts[from_account] -= amount
                self.accounts[to_account] += amount
                print(f"Transferred {amount} from account {from_account} to account {to_account}.")
                print(f"New balance for {from_account}: {self.accounts[from_account]}")
                print(f"New balance for {to_account}: {self.accounts[to_account]}")
            else:
                print("Insufficient funds.")
        else:
            print("One or both accounts do not exist.")

# Пример использования:
bank = Bank()
bank.create_account("12345", 1000)
bank.create_account("67890", 500)

bank.deposit("12345", 200)
bank.withdraw("12345", 300)
bank.transfer("12345", "67890", 400)
