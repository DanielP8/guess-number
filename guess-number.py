# Guess the Number
# Room 5 - David Osei Antwi, Deirdre Boland, Nora Ishmael, Daniel Popowych Jan 2025

# Import random module
import random

# Define minimum and maximum
minimum=1
maximum=100

# Function to generate random integer
def number_generator(minimum=1, maximum=100):
    """ Generates a random integer """
    generated_int = random.randint(minimum, maximum)
    return generated_int

# Function to check if input is an integer
def is_number(user_input):
    """ Checks if input is a integer """
    try:
        int(user_input)
        return True
    except ValueError:
        print("Please enter a integer.")
        return False

# Store random number as a variable
generated_number = number_generator()

# Ask user to guess an integer on repeat until they guess it correctly
while True:
    user_input = input(f'Enter an integer between {minimum} and {maximum}: ')
    # Call is_number function to check user input
    if is_number(user_input):
        # Store function output in new variable
        user_number = int(user_input)
        # Give user feedback on difference between their guess and desired number
        if (user_number < minimum) or (user_number > maximum):
            print(f"Not between {minimum} and {maximum}")
        elif user_number == generated_number:
            print(f'You guessed the {generated_number}!')
            break
        elif user_number > generated_number:
            print(f"{user_input} is too high!")
        else:
            print(f'{user_input} is too low!')