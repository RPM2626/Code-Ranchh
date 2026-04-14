class GameResult:
    def __init__(self, bulls: int, cows: int):
        self.bulls = bulls
        self.cows = cows


def evaluate_guess(secret: str, guess: str) -> GameResult:
    bulls = sum(1 for i in range(len(secret)) if secret[i] == guess[i])

    cows = 0
    for g in guess:
        if g in secret:
            cows += 1

    cows -= bulls

    return GameResult(bulls, cows)
