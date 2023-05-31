class Guild:
    guilds_list = []
    def __init__(self, name, perk):
        self.name = name
        self.perk = [perk] # this gives the ability to add more perks at will
        self.member = []
        self.level = 1
        Guild.guilds_list.append(self)
    
    # def join_guild(self, player):
    #     self.member.append(player)
    #     for perk in self.perks:
    #         player.perks.append(perk)
        # ! this function is incomplete.
        # ! we need a way of knowing which guilds each player is a member of,
        # ! how is the player themself going to know, rather than just the guild
        # ! perks will need a class as well, where the perks come so that we can
        # ! take them away from players when they leave a guild and such