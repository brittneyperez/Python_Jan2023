import db

class State:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.abbreviation = data['abbreviation']
        
    # * Instance Method
    def say_hello(self):
        print(f'I am the state of {self.name}. My abbreviation is {self.abbreviation}.')
    
    @classmethod
    def get_state_by_id(cls, id):
        for entry in db.states:
            if entry['id'] == id:
                print(cls(entry))
                return(cls(entry)) # return the object of the state <state.State object at location_digits>

# * Code Testing...
# State.get_state_by_id(2)