import BankAccount

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # Acessing... BankAccount file -> BankAccount class
        self.account = BankAccount.BankAccount( interest_rate=0.1, balance=0 )
        
        # * Dictionary for accounts when display_user_balance() is called, where indexes are user's accounts.
        self.accounts = {} # (variable) accounts: dict
    
    # * SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to.
    def create_account(self, interest_rate=0.1, balance=0, account_name='checking'):
        if account_name in self.accounts:
            print('Account of this name already exists.')
            return self
        else:
            new_account = BankAccount.BankAccount(interest_rate, balance)
            self.accounts[account_name] = new_account
            return self
    
    # * make_deposit method - calls on it's bank account's instance methods.
    def make_deposit(self, amount, account_name='checking'): # account_name = 'checking'
        self.accounts[account_name].deposit(amount)
        return self
    
    # * make_withdrawal method - calls on it's bank account's instance methods.
    def make_withdrawal(self, amount, account_name='checking'): # account_name = 'checking'
        self.accounts[account_name].withdraw(amount)
        # print(f'You\'ve withdrawed ${amount}. Your balance has been updated to: ${self.balance}.')
        return self
    
    
    # * display_user_balance method - displays user's account balance.
    def display_user_balance(self, account_name='checking'): # account_name = 'checking'
        # self.account.display_account_info()    => NA; only for single user
        display_str = ''
        print(self.first_name.upper() + '\'s - Accounts Summary'.upper())
        for account_name, account in self.accounts.items():  # access keys & values of acc dict
            display_str += f'{account_name}: ${account.balance}\n'  # add key & value index
        print(display_str)
        print('')
        return self
    
    # * SENPAI BONUS: Add a transfer_money(self, amount, other_user) method that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
    def transfer_money(self, account_name, amount, other_user, to_account):
        print('Money Transfer Processing...'.upper())
        
        if account_name.lower() == 'checking':
            self.accounts[account_name].withdraw(amount)
            other_user.accounts[account_name].deposit(amount)
            print(f'Transferring ${amount} from {self.first_name}\'s {account_name} to {other_user.first_name}\'s {to_account}.')
            return self
        
        if account_name.lower() == 'savings':
            if self.last_name != other_user.last_name:  # Check if last names match
                print('Action cannot be performed. Last names do not match.')
                return self
            else:
                self.accounts[account_name].withdraw(amount)
                other_user.accounts[account_name].deposit(amount)
                print(f'Transferring ${amount} from {self.first_name}\'s {account_name} to {other_user.first_name}\'s {to_account}.')
                return self



''' CODE EXECUTION Pt 1 '''
# jane = User('Jane Doe', 'jdoe@mail.com')
# jane.make_deposit(1600).make_deposit(160).display_user_balance()
# print(jane.account.balance)   # prints current balance

# joe = User('Joe Smith', 'joes23@mail.com')
# joe.make_deposit(500).display_user_balance().make_withdrawal(275).display_user_balance()

''' CODE EXECUTION Pt 2: SENSEI & SENPAI'''

janedoe = User('Jane', 'Doe', 'jdoe@mail.com')
janedoe.create_account(0.02, 300) # this will auto make a "checking" account
janedoe.make_deposit(600).make_withdrawal(10).display_user_balance()
janedoe.create_account(0.80, 2000, 'savings').display_user_balance()
# print(' ')  #terminal spacer

jsmithy = User('Joe', 'Smith', 'joes23@mail.com')
jsmithy.create_account(0.02, 150).display_user_balance()
jsmithy.make_deposit(2000).display_user_balance()
jsmithy.create_account(0, 1000, 'savings').display_user_balance()
# joe.transfer_money(500, jane, 'checking', 'tuition')

jsmithy.transfer_money('savings', 50, janedoe, 'checking')
janedoe.display_user_balance()

not_your_fam = User('Rebecca', 'Purple', 'j@s.com')
not_your_fam.create_account(0.1, 100).display_user_balance().make_deposit(360)
not_your_fam.create_account(0.1, 100, 'savings').display_user_balance().make_deposit(25).make_withdrawal(75)
jsmithy.transfer_money('savings', 25, not_your_fam, 'savings') # Action cannot be performed. Last names do not match.

not_your_fam.create_account(0.02, 1000, 'savings') # Account of this name already exists.