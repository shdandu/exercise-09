"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730705811"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    # Asks user to enter word
    word: str = input("Enter a 5-character word: ")
    # Stops program if word isn't 5 characters
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    # Asks user to enter letter
    letter: str = input("Enter a single character: ")
    # Stops program if letter isn't 1 character
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    # Says if the letter is in the word
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    # Says how many times the character is in the word
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
