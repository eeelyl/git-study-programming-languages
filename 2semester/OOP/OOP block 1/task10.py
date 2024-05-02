class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return "Transaction('{}', '{}', {})".format(self.sender, self.receiver, self.amount)

    def __str__(self):
        return '{} --> {} : {}'.format(self.sender, self.receiver, self.amount)


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def add_account(self, *accounts):
        for acc in accounts:
            if acc not in self.accounts.keys():
                self.accounts[acc] = 0

    def add_transaction(self, *transactions):
        for tr in transactions:
            if tr.sender in self.accounts.keys() and tr.receiver in self.accounts.keys():
                if self.accounts[tr.sender] - tr.amount >= 0:
                    self.transactions.append(tr)
                    self.accounts[tr.sender] -= tr.amount
                    self.accounts[tr.receiver] += tr.amount
                else:
                    print(f'Недостаточно средств на счете {tr.sender}')
            else:
                print('Не являются клиентами банка')

    def remove_transaction(self, *transactions):
        for tr in transactions:
            if tr in self.transactions and self.accounts[tr.receiver] - tr.amount >= 0:
                self.accounts[tr.sender] += tr.amount
                self.accounts[tr.receiver] -= tr.amount
                self.transactions.remove(tr)

    def deposit(self, account, amount):
        self.accounts[account] += amount

    def withdraw(self, account, amount):
        if self.accounts[account] - amount >= 0:
            self.accounts[account] -= amount
        else:
            print(f'Недостаточно средств на счете {account}')

    def print_transactions(self):
        print(self.transactions)

    def print_accounts(self):
        print(self.accounts)

    def print_all(self):
        print(f'Bank: {self.name}')
        print('_'*10)
        print('Accounts:')
        self.print_accounts()
        print('Transactions:')
        self.print_transactions()


sber = Bank('sber')
sber.add_account('Van')
sber.add_account('Joe')
sber.print_all()
sber.deposit('Van', 5000)
sber.print_all()
tr1 = Transaction('Van', 'Joe', 3000)
sber.add_transaction(tr1)
sber.print_all()
sber.remove_transaction(tr1)
sber.print_all()
