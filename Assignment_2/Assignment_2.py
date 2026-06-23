import random

game_Start = input("Welcome to Lady Luck's game of Craps! Care to try your fortune today? [Type 'Roll' to start or 'Quit' to exit.]")


while game_Start == "roll" or game_Start == "Roll" or game_Start == "ROLL":
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    print(f"Dice 1: {dice_1}")
    print(f"Dice 2: {dice_2}")
    total = dice_1 + dice_2
    print(f"Total: {total}")
    if total == 7 or total == 11:
        print("You win this time! But will Lady Luck smile on you again?")
        game_Start = input("Welcome to Lady Luck's game of Craps! Care to try your fortune today? [Type 'Roll' to start or 'Quit' to exit.]")
    elif total == 2 or total == 3 or total == 12:
        print("Awh Craps! You lose...")
        game_Start = input("Welcome to Lady Luck's game of Craps! Care to try your fortune today? [Type 'Roll' to start or 'Quit' to exit.]")
    else:
        game_Start = input("Oh, one more round! Type 'Roll' to play agian or 'Quit' to exit:")