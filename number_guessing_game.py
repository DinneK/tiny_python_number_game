# The random module is a built in Python module
import random

# Define a function
def play_game():
  # randint() - random integer is a built-in function in Python. It takes two arguments
  number = random.randint(1, 100)
  guesses_left = 10

  # Python version of a while loop, it will exicute everything within the loop before rerunning, order is very important.
  while guesses_left > 0:
    try:
      #input() is a built in function in Python, it will prompt and input, everything put into input is read as a string, so it must be converted.
      guess = int(input("Guess a number between 1 and 100"))
    except ValueError: #ValueError is built-in, catches if anything other than a number is put in.
      print("Invalid input. Please enter a number")
      continue # Skips to next iteration of the loop

    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    else:
      print(f"Congratulations! You guessed the number {number} in {10 - guesses_left} tries.")
      return
    
    guesses_left -= 1

  print(f"You ran out of guesses. The number was {number}.") # Python version of interpolation

if __name__ == "__main__": # Ensures the game runs only if the script is executed directly, not when imported.
    play_game()