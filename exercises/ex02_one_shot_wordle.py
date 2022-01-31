"""Making a wordle with emojis."""

__author__: str = "730488173"

secret: str = "python"
guess: str = str(input("What is your " + str(len(secret)) + "-letter guess? "))
index: int = 0
yellowcheck: int = 0
whichbox: bool = False
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

result: str = ""
while len(guess) != len(secret):
    guess = str(input("That was not " + str(len(secret)) + "letters! Try again: "))

while index < len(secret):
    if guess[index] == secret[index]:
        result = result + GREEN_BOX 
    else:
        while whichbox is False and yellowcheck < len(secret):
            if guess[index] == secret[yellowcheck]:
                whichbox = True
            yellowcheck = yellowcheck + 1
        if whichbox is True:
            result = result + YELLOW_BOX
        if whichbox is False:
            result = result + WHITE_BOX
            """This is checking each index of the secret word with the current guess index to look for yellow squares"""
    index = index + 1
    yellowcheck = 0
    whichbox = False

print(result)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
