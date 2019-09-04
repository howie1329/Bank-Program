
class Transaction():

    def __init__(self, date, amount, new_balance):
        self.date = date
        self.amount = amount
        self.balance = new_balance


    """ Method to print Transaction """
    def print_transactions(self):
        print('Transaction:')
        print('Date: {}'.format(self.date))
        print('Amount: {}'.format(self.amount))
        print('Balance: {}'.format(self.balance))
