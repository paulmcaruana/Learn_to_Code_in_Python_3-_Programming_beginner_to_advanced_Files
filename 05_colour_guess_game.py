import random

color = ["red", "blue", "yellow", "white", "black"]

while True:
    chosenColor = random.choice(color)
    guess = input("I'm thinking about a primary color. Can you guess it? ")

    while True:
        if guess == chosenColor:
            break
        else:
            guess = input("Nope! Try again: ")

    print("You guessed it. I was thinking about", chosenColor)

    play_again = input("Would you like to try again? (yes or no) ")

    if play_again.lower() == "no":
        break

print("Thank you for playing. Goodbye!")
        
    
    
