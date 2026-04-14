class GameRecord:
    def init(self, guess, bulls, cows):
        self.guess = guess
        self.bulls = bulls
        self.cows = cows

def to_dict(self):
    return {
        "guess": self.guess,
        "bulls": self.bulls,
        "cows": self.cows
    }
