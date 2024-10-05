# The random module is a built in Python module
import random
import json
import os

DATA_FILE = 'users_data.json'

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_user_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)


def get_user_name():
    user_name = input("Enter your name: ").strip()
    return user_name


def update_user_record(user_name, user_data, won):
    if user_name not in user_data:
        user_data[user_name] = {'wins': 0, 'losses': 0}

    if won:
        user_data[user_name]['wins'] += 1
        print(f"{user_name}, you won! Total wins: {user_data[user_name]['wins']}")
    else:
        user_data[user_name]['losses'] += 1
        print(f"{user_name}, you lost. Total losses: {user_data[user_name]['losses']}")

    save_user_data(user_data)


# Define a function
def play_game(user_name, user_data):
  # randint() - random integer is a built-in function in Python. It takes two arguments
  number = random.randint(1, 100)
  guesses_left = 10
  won = False

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
      won = True
      break
    
    guesses_left -= 1

  if not won:
    print(f"You ran out of guesses. The number was {number}.") # Python version of interpolation

  update_user_record(user_name, user_data, won)

def main():
    user_data = load_user_data()
    user_name = None

    while True:
        if not user_name:  # Ask for name only if user_name is not set
          print("\nWelcome to the Guessing Game!")
          user_name = get_user_name()

          if user_name in user_data:
            print(f"Welcome back, {user_name}! Wins: {user_data[user_name]['wins']}, Losses: {user_data[user_name]['losses']}")
          else:
            print(f"Welcome, {user_name}! Let's start playing.")

        play_game(user_name, user_data)

        # Ask if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()


# if __name__ == "__main__": # Ensures the game runs only if the script is executed directly, not when imported.
#     play_game()