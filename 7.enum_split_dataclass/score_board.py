from dataclasses import dataclass

@dataclass
class ScoreBoard:
    """Score board for recording scores"""
    score1: int = 0
    score2: int = 0
    def update(self, winner: str | None) -> None:
        if winner == "player1":
            self.score1 += 1
        elif winner == "player2":
            self.score2 += 1

    def get_score(self) -> tuple[int, int]:
        return self.score1, self.score2


if __name__ == "__main__":
    print("This is module Score Board")