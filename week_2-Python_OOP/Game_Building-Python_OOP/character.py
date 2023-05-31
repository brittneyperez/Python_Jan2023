# Class Names are ALWAYS Capitalized
class Character:
    all_characters = [] #? to track characters
    # see weapon.py to understand what are constructors
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.health = 1000
        self.is_alive = True
        self.carry_weight = 0
        self.weight_limit = 90
        Character.all_characters.append(self) #? go to weapon.py to understand how we append objects to a list
        self.perks = []
        self.weapons = [] #? this is the inventory of all the weapons
        self.equipped_weapons_index = 0  #? the weapon currently in a character's disposal
    
    
    def equip_weapon(self, weapon):
        if self.carry_weight + weapon.weight > self.weight_limit:
            print(f'{self.name} is carrying too much...')
        else:
            self.weapons.append(weapon)
            self.carry_weight += weapon.weight
            print(f'{self.name} has acquired {weapon.name}! Ready to attack!')
    
    def attack(self, enemy): #? self is needed so the method knows the character "attacking"
        if not self.equipped_weapons_index:
            print("You need a weapon!")
        elif len(self.weapons)-1 < self.equipped_weapons_index: # if the character has no weapons in their inventory...
            print(f'{self.name} has no weapon. Run away!!!') # ...no attack, only run away
        else:
            Character.adjust_health(enemy, self.weapons[self.equipped_weapons_index].damage)
            """ Why Character.adjust_health(param_1, param_2)?
            ? We need to call the Character class before
            ? accessing the adjust_health() method and applying
            ? the arguments to consider for it parameters
            """
            """ Changes made...
            We no longer need the bottom two lines since we'll be adjusting
            health with the line above and the method adjust_health().
            # enemy.health -= self.weapons[self.equipped_weapons_index].damage
            # print(f'{enemy.name} is hit! {enemy.name}\'s health is now at {enemy.health} health.')
            """
    
    def put_away_weapon(self):
        self.equipped_weapons_index = None
        # pass
    
    @staticmethod
    def adjust_health(player, hp):
        player.health -= hp
        if player.health <= 0:
            player.health = 0
            player.is_alive = False
            print(f'{player.name} is dead. Current Status: is_alive: {player.is_alive}, hp: {player.health}.')
            # if player.is_alive == False:
            #     print(f'{player.name} is already dead. Stop beating a dead horse.')
            return
        else:
            print(f'{player.name} is hit! {player.name}\'s health is now at {player.health} health.')