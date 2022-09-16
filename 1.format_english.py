import random

print("==========================================================")
print("=============== Rock Scissors Paper Game =================")
print("==========================================================\n")


choice = ["rock", "scissors", "paper"]


def number_player():
    while True:
        num_player = int(input("Please enter number of players. ex) 1, 2 : "))
        if num_player in [1, 2]:
            return num_player
        else:
            print("Select between 1 and 2")


def scoreboard():
    while True:
        rounds = int(input("Select how many times to play. ex) 1, 3, 10... : "))
        if rounds >= 1:
            return rounds
        else:
            print("Enter a number greater than 0.")


def single_player():
    player1 = input("Select rock, scissors, paper : ")
    player2 = choice[random.randint(0, 2)]
    print(f"Player choosed '{player1}', computer choosed '{player2}'.")
    return player1, player2


def double_player():
    player1 = input("**Player1** Select rock, scissors, paper : ")
    player2 = input("**Player2** Select rock, scissors, paper : ")
    print(f"Player1 choosed '{player1}', player2 choosed '{player2}'.")
    return player1, player2


def play(rounds, num_player):
    score_player1 = score_player2 = 0

    for i in range(rounds):
        if num_player == 1:
            player1, player2 = single_player()
        else:
            player1, player2 = double_player()

        if player1 == "scissors":
            if player2 == "rock":
                print("player2 win")
                score_player2 += 1
            elif player2 == "paper":
                print("User win")
                score_player1 += 1
            else:
                print("Draw")

            print(score_player1, score_player2)

        elif player1 == "rock":
            if player2 == "paper":
                print("Computer win.")
                score_player2 += 1
            elif player2 == "scissors":
                print("Player win")
                score_player1 += 1
            else:
                print("Draw")

            print(score_player1, score_player2)

        else:
            if player2 == "scissors":
                print("Computer win")
                score_player2 += 1
            elif player2 == "rock":
                print("Player win")
                score_player1 += 1
            else:
                print("Draw")

            print(score_player1, score_player2)

    print(f"Player : {score_player1}, Computer : {score_player2}")


num_player = number_player()
print(num_player)
rounds = scoreboard()
print(rounds)
play(rounds, num_player)
