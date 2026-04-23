from project.player import Player

class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        try:
            current_player=  next(filter(lambda player: player.name == player_name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"
        self.__players.remove(current_player)
        return current_player