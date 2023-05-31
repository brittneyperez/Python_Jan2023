# A dog, in a pack, owned by a dog sledder.
# What makes up a dog?

class Dog:
    pack = []
    """
    Above is a class attribute. For each dog created,
    it will be added to the above list.
    """
    
    """
    Self is absolutely the first thing we pass in inside the Constructor.
    Nothing can happen without the self. After self, then follows the attributes.
    """
    def __init__(self, name, breed, size, weight):
        self.name = name
        self.breed = breed
        self.size = size
        self.weight = weight
        
        """
        ? For attributes that are always consistent,
        ? we can just assign a value instead of passing
        ? a parameter with a custom value upon creation.
        """
        self.has_fur = True
        self.is_alive = True
        self.legs = 4
        self.energy = 100
        Dog.pack.append(self) #? automatically adds dog to list
    
    # * This is our first method
    def eat(self): # everytime a dog eats
        self.energy += 5 # dog gains 5 energy
        print(f'This dog now has {self.energy} energy.')
        return self #* this will fix error on line47
    
    # What does a pack do?
    """ Class Methods
    A class method has access to everything in a class.
    Do this by adding the class decorator: @classmethod.
    Also add "cls" as the parameter in a @classmethod function.
    """
    @classmethod
    def print_pack(cls):
        for dog in cls.pack:
            print(dog.name)
    
    


# * TESTING OUR CODE

dog_1 = Dog('Marley', 'Labrador Retriever', 'Large', 72.5)
dog_2 = Dog('Brandy', 'Shi Tzu', 'Small', 13)
# print(dog_1) # <__main__.Dog object at 0x1022c8710>
"""
When we print(dog_1), we don't get the attributes
we set for it under the dog_1. We get the name
of the object and it's place in memory.
"""

dog_1.eat() # This dog now has 105 energy.
# print(dog_1.energy) # 105
# dog_1.eat().eat() #! AttributeError: 'NoneType' object has no attribute 'eat'
"""
The resulting error is due to dog_1.eat() turning into a NoneType object.
In other words, it becomes None.eat(). To fix this, we use the function
call "return self" so that after executing the method, the object will
revert back to its original state to be reused again.

To illustrate... For dog_1.eat().eat(), if we were to return "cat"
in the method eat() after executing the method once, the object
will return as such: "cat".eat(). So we need to return dog_1 as self
so it can keep being reused.
"""
dog_1.eat().eat() # +10 energy... This dog now has 115 energy.

# * Using @classmethod
Dog.print_pack()


# What makes up a person?
# A dog sledder person?
# What actions do all of them do?
