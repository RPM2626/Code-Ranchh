class GameResult:
    def __init__(self, guess, bulls, cows):
        self.guess = guess
        self.bulls = bulls
        self.cows = cows


class LeaderboardEntry:
    def __init__(self, date, attempts, status):
        self.date = date
        self.attempts = attempts
        self.status = status

