from enum import Enum, auto


class Hands(Enum):
    ROCK = auto()
    SCISSORS = auto()
    PAPER = auto()
    LIZARD = auto()
    SPOCK = auto()

if __name__ == "__main__":
    print("This is module hands")