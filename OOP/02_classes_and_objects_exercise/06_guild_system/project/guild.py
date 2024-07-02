from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player not in self.players:
            self.players.append(player)
            player.guild = self.name

            return f"Welcome player {player.name} to the guild {self.name}"

        elif player in self.players:
            return f"Player {player.name} is already in the guild."

        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        player = next((p for p in self.players if p.name == player_name), None)

        if player not in self.players:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = "Unaffiliated"

        return f"Player {player.name} has been removed from the guild."

    def guild_info(self) -> str:
        players = '\n'.join(p.player_info() for p in self.players)

        return f"Guild: {self.name}\n{players}"


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
