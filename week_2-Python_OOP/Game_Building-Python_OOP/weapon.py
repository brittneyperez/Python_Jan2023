# Class Names are ALWAYS Capitalized
class Weapon:
    id = 1 #? upon creating a weapon, its id = 1; this acts as the counter
    weapons_list = []
    
    """
    Pass in the parameters we want the weapon to include
    first include self, then the attributes/parameters
    that pertains to the specific weapon.
    """
    def __init__(self, name, weight, type, damage):
        self.name = name
        self.weight = weight
        self.type = type
        self.damage = damage
        self.id = Weapon.id 
        """ Where is Weapon.id coming from???
        #? This is referring to the "id" in the Weapon class
        #? outside of the constructor (def __init__)
        """
        
        Weapon.id += 1
        """ #? What is happening here? Why Weapon.id += 1?
        After successful creation of a weapon, the id
        is automatically incremented by 1. This will
        increment automatically. ONLY upon weapon creation.
        """
        
        self.standard_stat = "ATK" # every weapon made will come with this attribute
        Weapon.weapons_list.append(self)
        """ 
        "Now that I, self—aka Weapon, exist, I'm  going to
        add myself to the list of weapons within my class!"
        ? This will ensure that each weapon will be added
        ? to a list of weapons to be accessed later.
        """

sword = Weapon("Lion's Roar", 15, "Elemental Buff", 42)
# print(sword) 
""" >>> <__main__.Weapon object at 0x102954650>
#? Printing "sword" will return us the line above.
#? This is an object of class: Weapon in the place of memory.
"""
# print(sword.name) # Lion's Roar

# print(sword.id)
""" >>> <built-in function id>
#? We don't have a built-in function id, or not that we know of...
#? This is referring to the presence of: self.id = id.
#? Instead, that should be written as self.id = Weapon.id
"""

# print(Weapon.id)
"""(per line) >>> 1, 2
#? This prints the existing ids within the class, Weapon.
"""
bow = Weapon("Thundering Pulse", 25, "CRIT DMG 14.4%", 46)
# print(bow.name)
# print(Weapon.id) # 3  #? At this point, the next available id for the weapon yet to be created

# print('')
# print(Weapon.weapons_list)
""" >>> [<__main__.Weapon object at 0x1024f8750>, <__main__.Weapon object at 0x102497250>]
#? Sent back is an list of objects. We can't keep track of the weapons like this.
#? 
#?
#?
"""