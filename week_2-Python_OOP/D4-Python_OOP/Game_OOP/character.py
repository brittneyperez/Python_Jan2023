# Class Names are ALWAYS Capitalized
class Character:
    all_characters = [] #? to track characters
    
    """
    Pass in the parameters we want the character to include
    first include self, then the attributes/parameters
    that pertains to the specific character.
    """
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.health = 100
        self.carrying_weight = 0
        self.weight_limit = 90
        
        Character.all_characters.append(self)
        """ 
        "Now that I, self—aka Character, exist, I'm  going to
        add myself to the list of characters within my class!"
        ? This will ensure that each character will be added
        ? to a list of characters to be accessed later.
        """
