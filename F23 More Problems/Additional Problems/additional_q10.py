# Get word
word = input("Enter a word: ")
while len(word) < 6:
    word = input("Enter a word: ")

# Get guesses
guess = input("Input a letter: ")
guesses = 0
while len(guess) != 1 or guess in word:
    # Don't count invalid guesses
    if len(guess) != 1:
        guesses -= 1

    guess = input("Input a letter: ")
    guesses += 1

# Count the previous guess where it's wrong
guesses += 1

print(f"Guesses made: {guesses}, secret word: {word}")