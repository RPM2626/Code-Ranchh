import random
from datetime import date, datetime, timedelta

from app.models.game_model import GameResult, LeaderboardEntry

history = []
leaderboard = []
current_day = None
secret_number = ""


def generate_secret_for_day(day_value):
    random.seed(str(day_value))
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])


def ensure_daily_game():
    global current_day, secret_number, history

    today = date.today()

    if current_day != today:
        current_day = today
        secret_number = generate_secret_for_day(today)
        history = []


def evaluate_guess(guess: str):
    global history
    ensure_daily_game()

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    result = GameResult(guess, bulls, cows)
    history.append(result)
    return result


def get_history():
    ensure_daily_game()
    return history


def reset_game():
    global history
    ensure_daily_game()
    history = []


def get_today():
    ensure_daily_game()
    return current_day.strftime("%Y-%m-%d")


def get_time_until_next_challenge():
    now = datetime.now()
    tomorrow = datetime.combine(
        date.today() + timedelta(days=1),
        datetime.min.time()
    )
    remaining = tomorrow - now

    total_seconds = int(remaining.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def record_win():
    ensure_daily_game()

    entry = LeaderboardEntry(
        get_today(),
        len(history),
        "Won"
    )

    if not any(item.date == entry.date for item in leaderboard):
        leaderboard.append(entry)


def get_leaderboard():
    return leaderboard

   
