# TODO: (1) Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

class User:
    # TODO: Attributes: On instantiation of a user, the following attributes should be passed in as arguments: first_name, last_name, email, age
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
        # * Default attributes:
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    # * METHODS
    # TODO: Add the display_info(self) method to the User class
    # ? Have this method print all of the users' details on separate lines.
    def display_self( self ):
        print(f'-- { self.first_name } --')
        print(f'First Name: { self.first_name }')
        print(f'Last Name: { self.last_name }')
        print(f'Email: { self.email }')
        print(f'Age: { self.age }')
        print(f'Membership: { self.is_rewards_member }')
        print(f'Gold Card Points: { self.gold_card_points }')
    
    # TODO: Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
    # ? Have this method change the user's member status to True and set their gold card points to 200.
    def enroll( self ):
        if self.is_rewards_member:
            print('This user is already a member.')
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print('~ membership status ~'.upper())
            print(f'Enrollment Status: {self.is_rewards_member}')
            print(f'Gold Card Points: {self.gold_card_points}')
            print(f'Congratulations {self.first_name} {self.last_name} for joining the Membership!')
    
    # TODO: Implement the spend_points(self, amount) method
    # ? Have this method decrease the user's points by the amount specified.
    def spend_points( self, amount_spent ):
        if amount_spent > 200:
            print('Amount exceeds limit.')
            
        elif amount_spent > self.gold_card_points:
            print(f'Sorry, {self.first_name}. You do not have any points at this time.')
            
        else:
            self.gold_card_points -= amount_spent
            print(f'Thank you, {self.first_name}. You\'ve spent {amount_spent} gold card points.')


""" CODE TESTING """
print(' ~ Users [ Python OOP ] ~')

# TODO: In the outer scope, create a user instance and call the display_info method to test.
janedoe = User('Jane', 'Doe', 'jdoe@mail.com', 24)

# TODO: Make 2 more instances of the User class.
t_arr19 = User('Tiz', 'Arrior', 'tizarr19@bd.com', 19)
jsmithy = User('John', 'Smith', 'jsmith@test.com', 35)
print(f'Users: {janedoe.first_name}, {t_arr19.first_name}, {jsmithy.first_name}')
print('')

# TODO: Have the first user spend 50 points
janedoe.spend_points(50) # Sorry, Jane. You do not have any points at this time.
print('')

# TODO: Have the second user enroll.
t_arr19.enroll() # Enrollment Status: True; Gold Card Points: True; Congratulations Tiz Arrior for joining the Membership!
print('')

# TODO: Have the second user spend 80 points
t_arr19.spend_points(80)
print('')

# TODO: Call the display method on all the users.
print('display all users'.upper())
janedoe.display_self()
print('')
t_arr19.display_self()
print('')
jsmithy.display_self()
print('')


# * Ninja Bonuses
# TODO: BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
janedoe.enroll()
print('')
janedoe.enroll() # This user is already a member.

print('')
# TODO: BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
jsmithy.spend_points(40)
print('')
jsmithy.enroll()
print('')
jsmithy.spend_points(100)
jsmithy.spend_points(150)
jsmithy.spend_points(100)
jsmithy.display_self()
