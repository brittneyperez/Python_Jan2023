from state import State
import db

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.height = data['height']
        self.gender = data['gender']
        self.age = data['age']
        self.money = data['money']
        self.email = data['email']
        self.state = None # this is set to none so it is not a requirement upon user creation
    
    # CREATE
    
    # READ
    @classmethod
    def get_all_users(cls):
        # * The more advance, proper way
        all_users = []
        for person in db.users:
            all_users.append(User.instantiate_user(person))

        # * Class Association
        # ? Now this person is associated with an isntance of a State
        # for person in all_users:
        #     print(f'User: {person.name} | State: {person.state.name}')
        #     person.state.say_hello()
        
        # * Below is the first, and simple way to get all users
        # for person in db.users:
        #     all_users.append(cls(person))
        #     print( person['name'], person['state'] )
        
        return all_users
    
    @classmethod
    def get_user_by_id(cls, id):
        for person in db.users:
            if person['id'] == id:
                return User.instantiate_user(person)
    
    @classmethod
    def get_user_by_email(cls, email):
        for person in db.users:
            if person['email'] == email:
                return User.instantiate_user(person)
    
    @classmethod
    def instantiate_user( cls, user_data ):
        this_user = cls(user_data) # this is what we are expecting for each user
        #                                     key: person['state']
        this_user.state = State.get_state_by_id(user_data['state']) # return the object of the person
        return this_user
    
    # UPDATE
    # DELETE
    # HELPER FUNCTIONS




# * Code Testing...
# User.get_all_users() # output: <state.State object at location_digits>
# all_these_users = User.get_all_users()
# print(all_these_users[0].state.say_hello())

# * Flow of Data: user obj -> state attr => state's name
# print(User.get_user_by_id(3).state.name)

print(User.get_user_by_email('jsmith@mail.com').name)