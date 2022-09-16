import getpass
import random

# A list of tuples leading up to winning
RULES: list[tuple[str, str]] = [
    ("scissors", "paper"),
    ("paper", "rock"),
    ("rock", "scissors"),
]
HANDS = ["rock", "scissors", "paper"]
WIDTH = 60
print("=" * WIDTH)
print(" Rock Scissors Paper Game ".center(WIDTH, "="))
print("=" * WIDTH)


def get_num_players() -> int:
    while True:
        try:
            num_players = int(input("Please enter number of players. ex) 1, 2 : "))
        except ValueError:
            num_players = 0

        if num_players in [1, 2]:
            return num_players
        else:
            print("Select between 1 and 2")


def get_num_rounds() -> int:
    while True:
        try:
            num_rounds = int(input("Select how many rounds to play. ex) 1, 3, 5... : "))
        except ValueError:
            num_rounds = 0

        if num_rounds >= 1:
            return num_rounds
        else:
            print("Enter a number greater than 0.")


def get_player_hand(player: str) -> str:
    while True:
        hand = getpass.getpass(f"**{player}** Select rock, scissors, paper : ")
        if hand in HANDS:
            return hand
        else:
            print("Select rock, scissors, paper : ")


def get_computer_hand() -> str:
    return random.choice(HANDS)


def play(num_rounds: int, num_players: int) -> None:
    score1 = score2 = 0

    for _ in range(num_rounds):
        if num_players == 1:
            hand1 = get_player_hand("player")
            hand2 = get_computer_hand()
        else:
            hand1 = get_player_hand("player1")
            hand2 = get_player_hand("player2")
        print(f"Player1 choosed {hand1}, Player2 choosed {hand2}")

        if (hand1, hand2) in RULES:
            score1 += 1
            print("Player1 win")
        elif (hand2, hand1) in RULES:
            score2 += 1
            print("player2 win")
        else:
            print("Draw")
        print(f"Player1 : {score1}, Player2 : {score2}")

    print("\nGame finished!")
    print(f"Player1 : {score1}, Player2 : {score2}")


def main() -> None:
    num_player = get_num_players()
    print(num_player)
    rounds = get_num_rounds()
    print(rounds)
    play(rounds, num_player)


if __name__ == "__main__":
    main()
