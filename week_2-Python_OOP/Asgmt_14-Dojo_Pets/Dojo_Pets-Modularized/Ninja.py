# TODO NINJA BONUS: Use modules to separate out the classes into different files.
import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet.Pet( pet['name'], pet['type'], pet['tricks'], pet['noise'] )
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        print(f'You are playing with {self.pet.name}.')
        self.pet.play()
        print('')
        return self
    
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f'You are feeding {self.pet.name} {food}.')
            self.pet.eat()
            print('')
        else:
            print("Oh no! You need more pet food!")
        return self
    
    def bathe(self):
        print(f'You are bathing {self.pet.name}.')
        self.pet.make_noise()
        return self
    
    def display_pet_status(self):
        print('[ {}\'s Status: {} health, {} energy ]'.format(self.pet.name, self.pet.health, self.pet.energy))
        return self



my_treats = ['Friskies', 'Temptations', 'Tuna Flakes', 'Churu']
my_pet_food = ['Hills', 'Arcana']

neko_chan = { # turn instance into dictionary/object
    'name': 'Neko-Chan',
    'type': 'cat',
    'tricks': ['roll over', 'flip', 'mice catch'],
    'noise': 'meow meow'
}

janedoe = Ninja('Jane', 'Doe', neko_chan, my_treats, my_pet_food)
janedoe.feed().walk().bathe().display_pet_status()
