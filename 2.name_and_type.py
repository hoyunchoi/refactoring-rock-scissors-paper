import random

print("==========================================================")
print("=============== Rock Scissors Paper Game =================")
print("==========================================================\n")


HANDS = ["rock", "scissors", "paper"]


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


def play(num_rounds: int, num_players: int) -> None:
    score1 = score2 = 0

    for _ in range(num_rounds):
        if num_players == 1:
            hand1, hand2 = get_single_player_hand()
        else:
            hand1, hand2 = get_double_player_hand()

        if hand1 == "scissors":
            if hand2 == "rock":
                print("Computer win")
                score2 += 1
            elif hand2 == "paper":
                print("Player win")
                score1 += 1
            else:
                print("Draw")

            print(score1, score2)

        elif hand1 == "rock":
            if hand2 == "paper":
                print("Computer win.")
                score2 += 1
            elif hand2 == "scissors":
                print("Player win")
                score1 += 1
            else:
                print("Draw")

            print(score1, score2)

        else:
            if hand2 == "scissors":
                print("Computer win")
                score2 += 1
            elif hand2 == "rock":
                print("Player win")
                score1 += 1
            else:
                print("Draw")

            print(score1, score2)

    print(f"Player : {score1}, Computer : {score2}")


num_players = get_num_players()
print(num_players)
num_rounds = get_num_rounds()
print(num_rounds)
play(num_rounds, num_players)
