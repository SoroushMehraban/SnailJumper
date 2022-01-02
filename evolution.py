import copy

from player import Player


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def generate_new_population(self, num_players, prev_players=None):
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            new_players = prev_players
            return new_players

    def next_population_selection(self, players, num_players):
        return players[: num_players]

    def clone_player(self, player):
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player

    def mutate(self, child):
        pass
