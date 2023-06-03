# TODO: Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    accounts = []
    def __init__( self, interest_rate, balance ):
        self.interest_rate = interest_rate
        self.balance = balance
        # in the class -> access the list -> and append object to list
        BankAccount.accounts.append(self)
    
    # TODO: Add a deposit method to the BankAccount class
    def deposit( self, amount ):
        self.balance += amount
        print(f'You\'ve deposited ${ amount }. Your balance has been updated to: ${ self.balance }')
        return self
    
    # TODO: Add a withdraw method to the BankAccount class
    def withdraw( self, amount ):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f'You\'ve withdrawed ${ amount }. Your balance has been updated to: ${ self.balance }')
        else:
            print('You have insufficient funds. Charging a $5 fee.')
            self.balance -= 5
        return self
    
    # TODO: Add a display_account_info method to the BankAccount class
    def display_account_info( self ):
        print(f'Balance: ${ self.balance }.')
        return self
    
    # TODO: Add a yield_interest method to the BankAccount class
    def yield_interests( self ):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        print(f'Balance after yield: ${ self.balance }.')
        return self
    
    # TODO: NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod #          cls = for accessing everything within this class
    def display_all_accounts( cls ):
        for account in cls.accounts:
            account.display_account_info()


# * Code Testing...
# TODO: Create 2 accounts
main_account = BankAccount(0.1, 1000)
savings = BankAccount(0.075, 4500)

# TODO: To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
main_account.deposit(850).deposit(455).deposit(100).withdraw(290).yield_interests().display_account_info()

print('')
# TODO: To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
savings.display_account_info().deposit(90).deposit(180).withdraw(45).deposit(270).deposit(360).withdraw(225).yield_interests().display_account_info()

print('')
print('Displaying All Accounts')
BankAccount.display_all_accounts()
# ? Call on the class first to access the @classmethod that displays all accounts