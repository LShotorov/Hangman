import random
from .gallows import gallow_builder

# Reading words from "Words.csv" and picking a random word
words = open("Words.csv", "r").read().split(",")
random_word = words[random.randint(0, len(words) + 1)]
# Initializing the hidden word with "_" for each letter
hidden_random_word = ["_"] * len(random_word)

print("Wellcom to the game Hangman!")
print(f"The word is: {' '.join(hidden_random_word)}")
tries = 11

while random_word.count("1") != len(random_word) and tries > 0:

    print(f"You have {tries} tries.")
    guess = input("Enter a letter: ").lower()

    # If the guess is present in the word, replace "_" with the correct letter
    if guess in random_word:
        for _ in range(random_word.count(guess)):
            hidden_random_word[random_word.index(guess)] = guess
            # Replacing the guess in the random_word with "1" so we can check if all letters were guessed
            random_word = random_word[:random_word.index(guess)] + "1" + random_word[random_word.index(guess) + 1:]
    else:
        print(f"There is no {guess} in the word.")
        # Displaying the hangman
        print("".join(gallow_builder(11 - tries)))
        tries -= 1
    # Dispalying the current status of the hidden word
    print(" ".join(hidden_random_word))
    
# If the player has no tries left, it means he didn't guessed the word
if tries == 0:
    print("\nSorry, you are dead.")
    print(f"The word was {random_word}")
else:
    print("Congratulations! You WON!")