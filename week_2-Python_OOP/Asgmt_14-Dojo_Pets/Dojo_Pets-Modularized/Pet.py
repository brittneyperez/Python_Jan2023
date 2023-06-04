class Pet:
    def __init__( self, name, animal_type, tricks, noise ):
        self.name = name 
        self.animal_type = animal_type 
        self.tricks = tricks 
        self.noise = noise 
        
        self.health = 100 
        self.energy = 50  
    
    def sleep( self ):
        self.energy += 25
        print(f'{self.name} is sleeping (.zzZ Gained 25 energy).')
        return self
    
    def eat( self ):
        self.energy += 5
        self.health += 10
        print(f'(=^x^=) {self.name} is eating ( *munch* *munch* ). {self.name} just gained 5 energy and 10 health.')
        return self # will execute with .feed()
    
    def play( self ):
        self.health += 5
        print(f'(=^x^=) {self.name} played! {self.name} just gained 5 health.')
        return self
    
    # ? Naming this as noise() will cause a TypeError as functions and variable can't share the same name, so it is changed to make_noise()
    def make_noise( self ):
        print('(=^x^=) {}: "{}".'.format(self.name, self.noise))
        return self