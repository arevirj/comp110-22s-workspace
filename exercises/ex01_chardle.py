"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730488173"

match: int = 0
word_ans: str = input("Enter a 5-character word: ")
if len(word_ans) != 5:
    print("Error: Word must contain 5 characters")
    quit()

chr_ans: str = input("Enter a single character: ")
if len(chr_ans) != 1:
    print("Error: Character must be a single character.")
    quit()
 
print("Searching for " + chr_ans + " in " + word_ans) 

if word_ans[0] == chr_ans:
    print(chr_ans + " found at index 0 ")
    match = match + 1
if word_ans[1] == chr_ans:
    print(chr_ans + " found at index 1 ")
    match = match + 1
if word_ans[2] == chr_ans:
    print(chr_ans + " found at index 2 ")
    match = match + 1
if word_ans[3] == chr_ans:
    print(chr_ans + " found at index 3 ")
    match = match + 1
if word_ans[4] == chr_ans:
    print(chr_ans + " found at index 4 ")
    match = match + 1

if match == 1:
    print(str(match) + " instance of " + chr_ans + " found in " + word_ans)
if match > 1:
    print(str(match) + " instances of " + chr_ans + " found in " + word_ans)
if match == 0:
    print("No instances of " + chr_ans + " found in " + word_ans)
                                    
