from Transaction import * 

class BankAccount():
    """ Transaction Data hold to store transactions for each account """
    Transactions = {}

    def __init__(self, name, date_created, account_number, initial_starting_amount):
        self.name = name
        self.date = date_created
        self.account_number = account_number
        self.starting_amount = initial_starting_amount


    """ Method to print account info """
    def viewAccountInfo(self):
        print('------Account Info-------')
        print('Name: {}'.format(self.name))
        print('Date Created: {}'.format(self.date))
        print('Account Number: {}'.format(self.account_number))
        print('Balance: {}'.format(self.starting_amount))


    """ Method to withdrawal money from account """
    def withdrawal(self):
        user_input = int(input('How much money would you like to take out? '))
        if user_input <= self.starting_amount:
            self.starting_amount = self.starting_amount - user_input
            print('New Balance: {}'.format(self.starting_amount))
        else:
            print('You do not have enough money for that withdrawl')


    """ Method to deposit money into account """
    def deposit(self):
        user_input = int(input('How much would you like to deposit? '))
        user_date = input('Whats the date? ')
        user_trans_number = int(input('Input Transaction Number '))
        self.starting_amount = self.starting_amount + user_input
        Trans = Transaction(user_date, user_input, self.starting_amount)
        self.Transactions[user_trans_number] = Trans 
        self.Transactions[user_trans_number].print_transactions()
        # print('New Balance: {}'.format(self.starting_amount))
