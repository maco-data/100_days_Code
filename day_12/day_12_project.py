from random import randint
from art import logo


# Global variables to set the amount of turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! I had {answer} in my mind! Your are a true Wizard!.")


def set_difficulty():
  """Ask user to set the game difficulty"""
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  """Game engine"""
  print(logo)
  
  print("Welcome to the Number Guessing Game!")
  
  print("Guess what number from 1 to 100 I have in mind!?!")
  
  # Choosing a random number between 1 and 100
  answer = randint(1, 100)
  turns = set_difficulty()
  
  # Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    # Let the user guess a number
    guess = int(input("Make a guess: "))

    # Track the number of turns and reduce by 1 if they get it wrong
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("Oops! you ran out of guesses, you lose!")
      return
    elif guess != answer:
      print("Guess again.")


game()



