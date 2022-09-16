import random

# A list of tuples which winning hands comming first
RULES: list[tuple[str, str]] = [
    ("scissors", "paper"),
    ("paper", "rock"),
    ("rock", "scissors"),
]
HANDS = ["rock", "scissors", "paper"]

print("==========================================================")
print("=============== Rock Scissors Paper Game =================")
print("==========================================================\n")


def get_num_players() -> int:
    while True:
        num_players = int(input("Please enter number of players. ex) 1, 2 : "))
        if num_players in [1, 2]:
            return num_players
        else:
            print("Select between 1 and 2")


def get_num_rounds() -> int:
    while True:
        num_rounds = int(input("Select how many rounds to play. ex) 1, 3, 10... : "))
        if num_rounds >= 1:
            return num_rounds
        else:
            print("Enter a number greater than 0.")


def get_single_player_hand() -> tuple[str, str]:
    hand1 = input("Select rock, scissors, paper : ")
    hand2 = HANDS[random.randint(0, 2)]
    print(f"Player choosed '{hand1}', computer choosed '{hand2}'.")
    return hand1, hand2


def get_double_player_hand() -> tuple[str, str]:
    hand1 = input("**Player1** Select rock, scissors, paper : ")
    hand2 = input("**Player2** Select rock, scissors, paper : ")
    print(f"Player1 choosed '{hand1}', hand2 choosed '{hand2}'.")
    return hand1, hand2


def play(rounds: int, num_player: int) -> None:
    score1 = score2 = 0

    for _ in range(rounds):
        if num_player == 1:
            hand1, hand2 = get_single_player_hand()
        else:
            hand1, hand2 = get_double_player_hand()

        if (hand1, hand2) in RULES:
            score1 += 1
            print("Player1 win")
        elif (hand2, hand1) in RULES:
            score2 += 1
            print("player2 win")
        else:
            print("Draw")
        print(f"Player1 choosed {hand1}, Player2 choosed {hand2}")
        print(f"Player1 : {score1}, Player2 : {score2}")

    print("\nGame finished!")
    print(f"Player : {score1}, Computer : {score2}")


def main() -> None:
    num_player = get_num_players()
    print(num_player)
    rounds = get_num_rounds()
    print(rounds)
    play(rounds, num_player)


if __name__ == "__main__":
    main()
