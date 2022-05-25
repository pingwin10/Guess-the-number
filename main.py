# Guess the number game

import random

# Randomization

peng = random.randint(1, 10000)
print("Guess the number I'm thinking of")

# Input

running = True
while running:
    guess_str = input("Guess the number: ")
    guess = int(guess_str)
    if guess == peng:
        print("GG! =]")
        running = False
    elif guess < peng:
        print("It's a bigger number!")    
    else:
        print("It's a smaller number!")    