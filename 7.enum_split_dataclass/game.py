from functools import partial

from hands import Hands
from score_board import ScoreBoard
from ui.ui import UI


class Game:
    """Rock Scissors Paper game"""

    def __init__(self, ui: UI, score_board: ScoreBoard) -> None:
        # A list of tuples leading up to winning
        self.RULES: list[tuple[Hands, Hands]] = [
            (Hands.SCISSORS, Hands.PAPER),
            (Hands.PAPER, Hands.ROCK),
            (Hands.ROCK, Hands.SCISSORS),
        ]

        self.ui = ui
        self.score_board = score_board

        self.ui.start_game()
        self.num_players = self.ui.get_num_players()
        self.num_rounds = self.ui.get_num_rounds()

        if self.num_players == 1:
            self.get_player1_hand = partial(self.ui.get_player_hand, "player")
            self.get_player2_hand = self.ui.get_computer_hand
        else:
            self.get_player1_hand = partial(self.ui.get_player_hand, "player1")
            self.get_player2_hand = partial(self.ui.get_player_hand, "player2")

    def _play_single_round(self) -> None:
        self.ui.start_round()

        # Get hands
        hand1 = self.get_player1_hand()
        hand2 = self.get_player2_hand()

        # Decide winner
        if (hand1, hand2) in self.RULES:
            winner = "player1"
        elif (hand2, hand1) in self.RULES:
            winner = "player2"
        else:
            winner = None

        # Update score board
        self.score_board.update(winner)

        # Print results and score
        self.ui.print_hands(hand1, hand2)
        self.ui.print_winner(winner)
        self.ui.print_score(*self.score_board.get_score())
        self.ui.finish_round()

    def run(self) -> None:
        for _ in range(self.num_rounds):
            self._play_single_round()

        # Print final result and finish the game
        self.ui.finish_game(*self.score_board.get_score())


if __name__ == "__main__":
    print("This is module Game")
