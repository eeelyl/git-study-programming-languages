class Account:
    def __init__(self, bank, name, total=0):
        self.name = name
        self.total = total
        self.bank = bank

    def __str__(self):
        return '{} : {}'.format(self.name, self.total)


class Transaction:
    def __init__(self, bank,  sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.bank = bank
        bank.transactions.append(self)

# В идеале в Bank должен быть словарь, который как ключ принимает имя аккаунта
# а значение будет его счетом
# тогда будет пиздатая инкапсуляция
# TODO!


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def add_account(self, *accounts):
        self.accounts.extend(accounts)

    def remove_account(self, *accounts):
        for account in accounts:
            if account in self.accounts:
                self.accounts.remove(account)

    def add_transaction(self, *transactions):
        self.transactions.extend(transactions)
        for tr in transactions:
            if tr.bank == self:
                if tr.sender.bank != self or tr.receiver.bank != self:
                    if tr.sender.total - tr.amount >= 0 and tr.receiver.total + tr.amount >= 0:
                        tr.sender.total -= tr.amount
                        tr.receiver.total += tr.amount
                    else:
                        print(
                            'Транзакция {} --> {} : {} не прошла. Недостаточно средств'.format(tr.sender, tr.receiver, tr.amount))
                else:
                    print('Клиент не принадлежит этому банку')
            else:
                print('Транзакция не принадлежит этому банку')

    def remove_transaction(self, *transactions):
        for tr in transactions:
            if tr in self.transactions:
                self.transactions.remove(tr)

    def __str__(self):
        res = f'Bank name: {self.name}\nAccounts:\n'
        for account in self.accounts:
            res += account.__str__() + '\n'
        return res


sber = Bank('sber')
account_Alex = Account(sber, 'Alex', 5000)
account_San = Account(sber, 'San', 3000)
sber.add_account(account_Alex, account_San)
sber.add_transaction(Transaction(sber, account_Alex, account_Alex, 5000))
print(sber)
sber.add_transaction(Transaction(sber, account_Alex, account_San, -3000))
print(sber)
