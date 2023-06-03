class User:
    # * Attributes of User Instance
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
        # Default attributes:
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    
    # * METHODS
    def display_self( self ):
        print(f'-- { self.first_name } --')
        print(f'First Name: { self.first_name }')
        print(f'Last Name: { self.last_name }')
        print(f'Email: { self.email }')
        print(f'Age: { self.age }')
        print(f'Membership: { self.is_rewards_member }')
        print(f'Gold Card Points: { self.gold_card_points }')
        print('')
        return self
    
    def enroll( self ):
        if self.is_rewards_member:
            print('This user is already a member.')
            # self.is_rewards_member = False
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print('~ membership status ~'.upper())
            print(f'Enrollment Status: {self.is_rewards_member}')
            print(f'Gold Card Points: {self.gold_card_points}')
            print(f'Congratulations {self.first_name} {self.last_name} for joining the Membership!')
            print('')
        return self
    
    def spend_points( self, amount_spent ):
        if not self.is_rewards_member:
            print(f'Sorry, {self.first_name}. You do not have any points at this time.')
            
        elif amount_spent > self.gold_card_points:
            print('Amount exceeds limit.')
            
        else:
            self.gold_card_points -= amount_spent
            print(f'Thank you, {self.first_name}. You\'ve spent {amount_spent} gold card points.')
        return self


""" CODE TESTING """
# User Instances
janedoe = User('Jane', 'Doe', 'jdoe@mail.com', 24)
t_arr19 = User('Tiz', 'Arrior', 'tizarr19@bd.com', 19)
jsmithy = User('John', 'Smith', 'jsmith@test.com', 35)
# print(f'Users: {janedoe.first_name}, {t_arr19.first_name}, {jsmithy.first_name}')
print('')

janedoe.spend_points(50).display_self().enroll().enroll().display_self().spend_points(40)
""" Output for Jane:
    Sorry, Jane. You do not have any points at this time.

    -- Jane --
    First Name: Jane
    Last Name: Doe
    Email: jdoe@mail.com
    Age: 24
    Membership: False
    Gold Card Points: 0

    ~ MEMBERSHIP STATUS ~
    Enrollment Status: True
    Gold Card Points: 200
    Congratulations Jane Doe for joining the Membership!

    This user is already a member.
"""
print('=======')

t_arr19.enroll().spend_points(80).display_self()
""" Output for Tiz:
    ~ MEMBERSHIP STATUS ~
    Enrollment Status: True
    Gold Card Points: 200
    Congratulations Tiz Arrior for joining the Membership!
    
    Thank you, Tiz. You've spent 80 gold card points.
    
    -- Tiz --
    First Name: Tiz
    Last Name: Arrior
    Email: tizarr19@bd.com
    Age: 19
    Membership: True
    Gold Card Points: 120
"""
print('=======')

jsmithy.spend_points(40).display_self().enroll().spend_points(100).spend_points(150).display_self().spend_points(100)
""" Output for John:
    Sorry, John. You do not have any points at this time.
    -- John --
    First Name: John
    Last Name: Smith
    Email: jsmith@test.com
    Age: 35
    Membership: False
    Gold Card Points: 0

    ~ MEMBERSHIP STATUS ~
    Enrollment Status: True
    Gold Card Points: 200
    Congratulations John Smith for joining the Membership!

    Thank you, John. You've spent 100 gold card points.
    Amount exceeds limit.
    -- John --
    First Name: John
    Last Name: Smith
    Email: jsmith@test.com
    Age: 35
    Membership: True
    Gold Card Points: 100

    Thank you, John. You've spent 100 gold card points.
"""