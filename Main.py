from Bank import BankAccount

""" Accounts data holder to store all user accounts """
Accounts = {}

""" Simple Heading To display to user """
def heading():
    print('Welcome to the Bank')


""" Menu Method to allow user to pick a choice from 4 options """
def menu():
    print('Please choose one of the options from below')
    print('1.) Open a new account')
    print('2.) View Account')
    print('3.) Admin Log In')
    print('4.) Exit')
    menu_Choice()


""" menu_choice allows user to choose 1 of the 4 options from menu. menu_choice is called from menu """
def menu_Choice():
    try:
        user_input = int(input())
        if user_input == 1:
            open_account()
            menu()
        elif user_input == 2:
            view_account()
            menu()
        elif user_input == 3:
            view_all_accounts()
            menu()
        elif user_input == 4:
            pass
        else:
            print('Wrong input please try again')
            menu()
    except:
        print('Wrong Input please try again')
        menu()


""" Open New User Accounts - Add Account to Accounts Dic.. """
def open_account():
    name = input('What is your full name? ')
    date = input('What is the date? ')
    account_number = int(input('What is the account number? '))
    starting_balance = int(input('What is the starting amount? '))
    newAccount = BankAccount(name, date, account_number, starting_balance)
    Accounts[account_number] = newAccount


"""View Accounts in Accounts Dic """
def view_account():
    account_number = int(input('What is your account number? '))
    Accounts[account_number].viewAccountInfo()
    view_account_menu(account_number)


""" The menu inside of the view account to allow user to add and subtract money from account """
def view_account_menu(number):
    print('1.) Withdraw')

    print('2.) Deposit')
    print('3.) Exit')
    user_input = int(input('What is your choice? '))
    if user_input == 1:
        Accounts[number].withdrawal()
    elif user_input == 2:
        Accounts[number].deposit()
    elif user_input == 3:
        print("Thank you please come again")


""" Admin Use to view all Accounts """
def view_all_accounts():
    for keys, val in Accounts.items():
        print(keys, "=>", val.viewAccountInfo())


""" Simple Starter Code """
if __name__ == "__main__":
    heading()
    menu()
