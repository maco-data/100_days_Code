import random
from hangman_art import stages, logo
from hangman_words import word_list


print(logo)
game_is_finished = False
lives = len(stages) - 1

# Choses a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
# Adds the blank spaces to show the lenght of the word
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    
    # If this letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # When a letter is guessed this displays the letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # If the guess is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1 # removes one life (increase negative index)
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display: # When all letters have been guessed
        game_is_finished = True
        print("You win.")

    print(stages[lives])