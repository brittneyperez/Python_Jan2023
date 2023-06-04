class Player:
    # TODO: Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary
    def __init__( self, player_data ):
        self.name = player_data['name'] 
        self.age = player_data['age'] 
        self.position = player_data['position'] 
        self.team = player_data['team'] 
    
    def __repr__( self ):
        return 'Player: {}, {} y/o, Position: {}, Team: {}.'.format( self.name, self.age, self.position, self.team )
    
    # TODO: Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
    @classmethod
    def get_team(cls, team_list):
        player_objects_team = []
        for player_data in team_list:
            player_objects_team.append(cls(player_data))
        return player_objects_team



players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]


# * Code Testing...

""" Challenge 2: Create instances using individual player dictionaries. 
* Given these variables, create Player instances for each of the following dictionaries.
* Be sure to instantiate these outside the class definition, in the outer scope.
# TODO: Complete challenge 2: Create 3 instances of the Player class using the given dictionaries
"""

print('-- JOEL EMBIID --')
# print(players[4]) # ? output: Joel's stats as a dictionary/object
player_joel = Player(players[4])
print(player_joel) 
print('')

# print(player_joel.name) # output: Joel Embid
    # prints the data as an object: <__main__.Player object at 0x105ffd090>
    # make a __repr__(self) method to fix this - instantiate

print('-- DAMIEN LILLARD --')
player_damien = Player(players[3])
print(player_damien)
print('')


print('-- JASON TATUM --')
player_jason = Player(players[1])
print(player_jason)
print(' ')


""" Challenge 3: Make a list of Player instances from a list of dictionaries.
* Write a for loop that will populate an empty list with Player objects from the original list of dictionaries.
# TODO: Complete challenge 3: Populate a new list with Player instances from the list of players.
"""
# new_team = []
# for player_dict in players:   # for player_dict in players_list:
#     player = Player(player_dict)
#     new_team.append(player)
# ? this is abandoned for the @classmethod

print('using @classmethod to create a Player List'.upper())

team = Player.get_team(players)
print(team)
# print('')
