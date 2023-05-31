from character import Character
from weapon import Weapon

player_1 = Character('Keqing', 'female')
player_2 = Character('Tartaglia', 'male')
lions_roar = Weapon("Lion's Roar", 15, "Elemental Buff", 42)
polar_star = Weapon("Polar Star", 20, "CRIT DMG", 46)
# print(lions_roar)

# print('')
player_1.equip_weapon(lions_roar)
player_1.put_away_weapon()
print(player_1.equipped_weapons_index)
player_1.attack(player_2)
"""
! This will not work. Attacking without weapon now will turn
! object into NoneType and break attack() method. Adjust attack()
! method to consider this action if there is no weapon equipped.
"""
player_1.equip_weapon(lions_roar)
player_1.attack(player_2)

# player_1.attack(player_2)
"""
! This code will still run fine BUT we shouldn't be having negative health.
! How can we fix this? By creating a method to evaluate if the Player is
! alive and if there hp is below 0 yet. Otherwise, they can still fight.
* Now that we have a method, let's continue the battle
"""

# player_2.equip_weapon(polar_star)
# player_2.attack(player_1)
# player_1.attack(player_2)
# player_1.attack(player_2)
