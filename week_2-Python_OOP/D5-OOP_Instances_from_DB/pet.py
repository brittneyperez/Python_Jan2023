import db
from user import User

class Pet:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.species = data['species']
        self.age = data['age']
        self.owner = None
    
    #CREATE
    # READ
    @classmethod
    def get_pet_by_id( cls, id ):
        for pet in db.pets:
            if pet['id'] == id:
                return cls.instantiate_pet(pet)
    
    # UPDATE
    # DELETE
    
    # Helper Functions
    @classmethod
    def instantiate_pet( cls, pet_data ):
        this_pet = cls(pet_data)
        this_pet.owner = User.get_user_by_id(pet_data['user_id'])
        return this_pet
    



# * Code Testing....

print(Pet.get_pet_by_id(123123123).name) # Fluffy