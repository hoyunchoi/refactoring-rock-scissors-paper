import getpass
import random

HANDS = ["rock", "scissors", "paper"]


class CLI:
    """
    Comamnd Line Interface
    Handles all inputs and outputs that occur in terminal
    """

    def __init__(self) -> None:
        self.CHAR = "="
        self.WIDTH = 60

    def _print_line(self) -> None:
        """Print line with default width"""
        print(self.CHAR * self.WIDTH)

    ########################## Output ##########################
    def start_game(self) -> None:
        """ Start game with introduction """
        self._print_line()
        print(" Rock Scissors Paper Game ".center(self.WIDTH, self.CHAR))
        self._print_line()

    def finish_game(self, final_score1: int, final_score2: int) -> None:
        """ Finish game with final score """
        self._print_line()
        print("Game finished!")
        self.print_score(final_score1, final_score2)
        self._print_line()

    def start_round(self) -> None:
        self._print_line()

    def finish_round(self) -> None:
        print()

    def print_winner(self, winner: str | None) -> None:
        if winner is None:
            print("Draw")
        else:
            print(f"{winner} win")

    def print_score(self, score1: int, score2: int) -> None:
        print(f"Player1 : {score1}, Player2 : {score2}")

    def print_hands(self, hand1: str, hand2: str) -> None:
        print(f"Player1 choosed {hand1}, Player2 choosed {hand2}")

    ########################## Input ##########################
    def get_num_players(self) -> int:
        while True:
            try:
                num_players = int(input("Please enter number of players. ex) 1, 2 : "))
            except ValueError:
                num_players = 0

            if num_players in [1, 2]:
                return num_players
            else:
                print("Select between 1 and 2")

    def get_num_rounds(self) -> int:
        while True:
            try:
                num_rounds = int(
                    input("Select how many rounds to play. ex) 1, 3, 5... : ")
                )
            except ValueError:
                num_rounds = 0

            if num_rounds >= 1:
                return num_rounds
            else:
                print("Enter a number greater than 0.")

    def get_player_hand(self, player: str) -> str:
        while True:
            hand = getpass.getpass(f"**{player}** Select rock, scissors, paper : ")
            if hand in HANDS:
                return hand
            else:
                print("Select rock, scissors, paper : ")

    def get_computer_hand(self) -> str:
        return random.choice(HANDS)


class ScoreBoard:
    """Score board for recording scores"""

    def __init__(self, score1: int = 0, score2: int = 0) -> None:
        self.score1 = score1
        self.score2 = score2

    def update(self, winner: str | None) -> None:
        if winner == "player1":
            self.score1 += 1
        elif winner == "player2":
            self.score2 += 1

    def get_score(self) -> tuple[int, int]:
        return self.score1, self.score2


class Game:
    """Rock Scissors Paper game"""

    def __init__(self) -> None:
        # A list of tuples leading up to winning
        self.RULES: list[tuple[str, str]] = [
            ("scissors", "paper"),
            ("paper", "rock"),
            ("rock", "scissors"),
        ]

        self.ui = CLI()
        self.score_board = ScoreBoard()

        self.ui.start_game()
        self.num_players = self.ui.get_num_players()
        self.num_rounds = self.ui.get_num_rounds()

    def play_single_round(self) -> None:
        self.ui.start_round()

        # Get hands
        if self.num_players == 1:
            hand1 = self.ui.get_player_hand("player")
            hand2 = self.ui.get_computer_hand()
        else:
            hand1 = self.ui.get_player_hand("player1")
            hand2 = self.ui.get_player_hand("player2")
        self.ui.print_hands(hand1, hand2)

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
        self.ui.print_winner(winner)
        self.ui.print_score(*self.score_board.get_score())
        self.ui.finish_round()

    def run(self) -> None:
        for _ in range(self.num_rounds):
            self.play_single_round()

        # Print final result and finish the game
        self.ui.finish_game(*self.score_board.get_score())


def main() -> None:
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
