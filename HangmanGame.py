# Hangman Game
import random

# Word list
word_list = ["Mango", "Apple", "Banana", "Orange", "Grapes"]

# trial inputs
incorrect_guesses = 6
# Randomly select a word from the list
word = random.choice(word_list)

# Initialize the display with underscores
display = "_" * len(word)

# Game loop
print("Welcome to Hangman!")
print("Guess the word: " + display)


while incorrect_guesses > 0 and "_" in display:
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in word.lower():
        print("Good guess!")
        display = "".join([word[i] if word[i].lower() == guess else display[i] for i in range(len(word))])
    else:
        incorrect_guesses -= 1
        print(f"Incorrect guess! You have {incorrect_guesses} guesses left.")
    
    print("Current word: " + display)




