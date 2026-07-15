from project.player import Player


class Guild:
    def __init__(self, name:str):
        self.name = name
        self.players = []
        
    def assign_player(self, player: Player) -> str:
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."
        elif self.name != player.guild and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name:str) -> str:
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = "\n".join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n{result}"

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
