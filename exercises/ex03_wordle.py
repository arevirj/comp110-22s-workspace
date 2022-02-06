"""Program that gives the player six guesses at secret word."""


__author__: str = "730488173"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret: str, one_char: str) -> bool:
    """Checks if a certain character is contained in a word."""
    assert len(one_char) == 1
    count_contains: int = 0
    check_contains: bool = False
    while count_contains < len(secret) and check_contains is False:
        if one_char == secret[count_contains]:
            check_contains = True
        count_contains = count_contains + 1
    if check_contains is True:
        return True
    if check_contains is False:
        return False


def emojified(guess: str, secret: str) -> str:
    """Tells the user which letters match and which don't through emojis."""
    assert len(secret) == len(guess)
    count_emoji: int = 0
    result: str = ""
    while count_emoji < len(secret):
        if contains_char(secret, guess[count_emoji]) is True:
            if guess[count_emoji] == secret[count_emoji]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        count_emoji += 1
    return result


def input_guess(guess_amt: int) -> str:
    """Prompts the user to guess the secret word, ensures it is the correct amount of characters."""
    question: str = input(str(f"Enter a {guess_amt} character word: "))
    while len(question) != guess_amt:
        question = input(f"That wasn't {guess_amt} chars! Try again: ")
    return question


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turncount: int = 1
    wincheck: bool = False
    while turncount <= 6 and wincheck is False:
        print(f"=== Turn {turncount}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        print(result)
        if guess == secret:     
            wincheck = True
        else:
            turncount += 1
    if wincheck is True:
        print(f"You won in {turncount}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()