import random
import time
from abc import ABC, abstractmethod

from hands import Hands


class UI(ABC):
    """
    User Interface
    Handles all inputs and outputs
    """

    ########################## Output ##########################
    @abstractmethod
    def start_game(self) -> None:
        ...

    @abstractmethod
    def finish_game(self, final_score1: int, final_score2: int) -> None:
        ...

    @abstractmethod
    def start_round(self) -> None:
        ...

    @abstractmethod
    def finish_round(self) -> None:
        ...

    @abstractmethod
    def print_winner(self, winner: str | None) -> None:
        ...

    @abstractmethod
    def print_score(self, score1: int, score2: int) -> None:
        ...

    @abstractmethod
    def print_hands(self, hand1: Hands, hand2: Hands) -> None:
        ...

    ########################## Input ##########################
    @abstractmethod
    def get_num_players(self) -> int:
        ...

    @abstractmethod
    def get_num_rounds(self) -> int:
        ...

    @abstractmethod
    def get_player_hand(self, player: str) -> Hands:
        ...

    def get_computer_hand(self) -> Hands:
        time.sleep(0.5)
        return random.choice(list(Hands))


if __name__ == "__main__":
    print("This is abstract class ui from module UI")
