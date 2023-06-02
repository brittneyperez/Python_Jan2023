class Pet:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.species = data['species']
        self.age = data['age']
        
        