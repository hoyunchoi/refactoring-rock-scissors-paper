from game import Game
from score_board import ScoreBoard
from ui.cli import CLI


def main() -> None:
    ui = CLI()
    # ui = GUI()
    score_board = ScoreBoard()

    game = Game(ui, score_board)
    game.run()


if __name__ == "__main__":
    main()
