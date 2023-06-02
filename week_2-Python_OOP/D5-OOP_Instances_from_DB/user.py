from state import State
import db

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.gender = data['gender']
        self.money = data['money']
        self.age = data['age']
        self.email = data['email']
        self.state = None
    
    @classmethod
    def get_all_users(cls):
        # * Below is the first, and simple way to get all users
        # for person in db.users:
        #     all_users.append(cls(person))
        #     print( person['name'], person['state'] )
        
        # * The more advance, proper way
        all_users = []
        for person in db.users:
            new_person = cls(person)
            new_person.state = State.get_state_by_id(person['state'])
            all_users.append(new_person)
        # * Class Assiciation
        # ? Now this person is associated with an isntance of a State
        
        for person in all_users:
            print(f'User: {person.name} | State: {person.state.name}')
            person.state.say_hello()

# * Code Testing...
User.get_all_users()