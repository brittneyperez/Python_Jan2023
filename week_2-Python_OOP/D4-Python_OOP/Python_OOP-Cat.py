class Human: #* This exists to learn about Class Associations
    def __init__(self, name):
        self.name = name
        self.pets = [] # this is for a human to adopt pets
        self.spouse = None # bc every human is born single
        # We can learn class association

class Cat:
    
    """Bracket Notation
    When passing in a dictionary, we use bracket notation
    to grab the key—in this case, data.
    #! Dot Notation is for classes.
    """
    def __init__(self, data):
        self.name = data['name']
        self.breed = data['breed']
        self.fur = data['fur']
    


# * With this format, it will come back as the following dictionary upon form submission:
cat_details = {
    'name' : 'クニ',
    'breed' : 'Domestic Shorthair',
    'fur' : 'short, purple/white',
}
second_cat_details = {
    'name' : 'カズハ',
    'breed' : 'Maine Coon',
    'fur' : 'long, white',
}

# * Or we can even see the data like this:
# my_kitty_cat = Cat({'name' : 'Loki', 'breed' : 'Domestic Shorthair', 'fur' : 'short',})

my_cat = Cat(cat_details)
second_cat = Cat(second_cat_details)
# print(my_cat) # <__main__.Cat object at 0x102688e90>
# print(my_cat.name) # Loki

person_x = Human('Lumi')
person_y = Human('Xiao')
person_x.spouse = person_y
person_y.spouse = person_x
print(f'{person_x.spouse.name} is {person_x.name}\'s spouse.')

person_x.pets.append(my_cat)
person_x.pets.append(second_cat)
print(f'{person_x.name}\'s first pet cat: {person_x.pets[0].name}.')
print(f'{person_x.name}\'s cats: {person_x.pets[0].name} & {person_x.pets[1].name}.')