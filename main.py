# Author: @TheSarfaraz
# Date: 6th February 2021
# Project: Number Guessing Game
#100 Days Of Code Python Course by Angela

from random import randint
from art import logo

def checkAnswer(Guess, Answer):
  if Guess == Answer:
    return 0
  elif Guess > Answer:
    return -1
  elif Guess < Answer:
    return 1

def game():
  print(logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100! Guess it!")

  answer = randint(1, 100)

  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  TurnsAvailable = 10
  if level == 'hard':
    TurnsAvailable //= 2

  while TurnsAvailable > 0:
    print(f"You have {TurnsAvailable} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if checkAnswer(guess, answer) == 0:
      print(f"You got it! The answer was {guess}")
      return
    elif checkAnswer(guess, answer) == -1:
      print("Too high!")
    elif checkAnswer(guess, answer) == 1:
      print("Too low!")

    TurnsAvailable -= 1
  
  print("You've run out of guesses, you lose.")


game()