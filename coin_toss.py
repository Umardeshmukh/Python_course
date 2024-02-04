import random

# Generate a random number between 0 and 1
random_side = random.randint(0, 1)  # Corrected the typo in "randit"

# Check the random number and print the corresponding message
if random_side == 1:
    print("Heads")  # Removed unnecessary semicolon and curly braces
else:
    print("Tails")

