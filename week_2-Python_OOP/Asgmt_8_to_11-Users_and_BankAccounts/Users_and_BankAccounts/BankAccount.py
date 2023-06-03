# TODO: Create a BankAccount class with the attributes interest rate and balance
# This is the same file that is in the assignments directory but with the specific use case for this project
class BankAccount:
    accounts = []
    
    def __init__( self, interest_rate, balance ):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit( self, amount ):
        self.balance += amount
        print(f'You\'ve deposited ${ amount }. Your balance has been updated to: ${ self.balance }.')
        return self
    
    def withdraw( self, amount ):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f'You\'ve withdrawed ${ amount }. Your balance has been updated to: ${ self.balance }.')
        else:
            print('You have insufficient funds. Charging a $5 fee.')
            self.balance -= 5
        return self
    
    def display_account_info( self ):
        print(f'Balance: ${ self.balance }.')
        return self
    
    def yield_interests( self ):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        print(f'Balance after yield: ${ self.balance }.')
        return self
    
    @classmethod
    def display_all_accounts( cls ):
        for account in cls.accounts:
            account.display_account_info()


# * Code Testing...
# main_account = BankAccount(0.1, 1000)
# savings = BankAccount(0.075, 4500)

# main_account.deposit(850).deposit(455).deposit(100).withdraw(290).yield_interests().display_account_info()

# print('')
# savings.display_account_info().deposit(90).deposit(180).withdraw(45).deposit(270).deposit(360).withdraw(225).yield_interests().display_account_info()

# print('')
# print('Displaying All Accounts')
# BankAccount.display_all_accounts()