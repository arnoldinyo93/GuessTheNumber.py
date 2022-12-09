# Import the random module
import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Print an introduction
print("Welcome to the Guess the Number game!")
print("I am thinking of a number between 1 and 100.")
print("Try to guess the number and I will tell you if your guess is too high or too low.")

# Start the game loop
while True:
  # Get the player's guess
  guess = int(input("Enter your guess: "))

  # Check if the guess is correct
  if guess == number:
    print("Congratulations! You guessed the correct number!")
    break
  # Check if the guess is too high
  elif guess > number:
    print("Your guess is too high. Try again.")
  # The guess must be too low
  else:
    print("Your guess is too low. Try again.")