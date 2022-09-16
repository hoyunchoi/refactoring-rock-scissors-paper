import getpass

from hands import Hands
from ui.ui import UI


class CLI(UI):
    """
    Comamnd Line Interface
    Handles all inputs and outputs that occur in terminal
    """

    def __init__(self) -> None:
        self.CHAR = "="
        self.WIDTH = 60

    ########################## Output ##########################
    def _print_line(self) -> None:
        print(self.CHAR * self.WIDTH)

    def start_game(self) -> None:
        """Start game with introduction"""
        self._print_line()
        print("Rock Scissors Paper Game".center(self.WIDTH, self.CHAR))
        self._print_line()

    def finish_game(self, final_score1: int, final_score2: int) -> None:
        """Finish game with final score"""
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

    def print_hands(self, hand1: Hands, hand2: Hands) -> None:
        print(
            f"Player1 choosed {hand1.name.lower()}, Player2 choosed {hand2.name.lower()}"
        )

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

    def get_player_hand(self, player: str) -> Hands:
        while True:
            hand = getpass.getpass(
                f"**{player}** Select {', '.join(hands.name.lower() for hands in Hands)} :"
            )
            try:
                return Hands[hand.upper()]
            except KeyError:
                print("Select rock, scissors, paper : ")

    def get_computer_hand(self) -> Hands:
        print("**Computer** Selecting...")
        return super().get_computer_hand()


if __name__ == "__main__":
    print("This is class gui from module UI")
