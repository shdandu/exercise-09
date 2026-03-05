"""Wordle game"""

__author__ = "730705811"


def main(secret: str) -> None:
    """Entrypoint of the program"""
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:
        # Provides output for each turn
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(secret_word=secret, guess=guess))
        if secret == guess:
            won = True
            print(f"You won in {turn}/6 turns!")
        if turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn += 1


def input_guess(secret_word_len: int) -> str:
    # Asks user to enter word
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # Keeps asking for input until guess has correct length
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Looks for guess character in secret word"""
    assert len(char_guess) == 1
    x: int = 0
    while x < len(secret_word):
        if secret_word[x] == char_guess:
            return True
        x += 1
    return False


def emojified(secret_word: str, guess: str) -> str:
    """Returns a string of emojis showing correct guesses"""
    assert len(secret_word) == len(guess)
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    idx: int = 0
    wordle: str = ""
    # Figures out what emojis to use
    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            wordle += GREEN_BOX
        elif contains_char(secret_word, guess[idx]):
            wordle += YELLOW_BOX
        else:
            wordle += WHITE_BOX
        idx += 1
    return wordle


if __name__ == "__main__":
    main(secret="codes")
