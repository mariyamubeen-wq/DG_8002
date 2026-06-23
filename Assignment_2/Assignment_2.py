import random

game_Start = input("Welcome to Lady Luck's game of Craps! Care to try your fortune today? [Type 'Roll' to start or 'Quit' to exit.]")
game_round = 0
while game_Start == "roll" or game_Start == "Roll" or game_Start == "ROLL":
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    print(f"Dice 1: {dice_1}")
    print(f"Dice 2: {dice_2}")
    total = dice_1 + dice_2
    print(f"Total: {total}")
    game_round = game_round + 1
    if total == 7 or total == 11:
        print(f"You played {game_round} rounds!")
        print("You win this time! But will Lady Luck smile on you again?")
        game_Start = input("Welcome to Lady Luck's game of Craps! Care to try your fortune today? [Type 'Roll' to start or 'Quit' to exit.]")
    elif total == 2 or total == 3 or total == 12:
        print("Awh Craps! You lose...")
        print(f"You played {game_round} rounds!")
        game_Start = input("Welcome to Lady Luck's game of Craps! Care to try your fortune today? [Type 'Roll' to start or 'Quit' to exit.]")
    elif game_Start == "quit" or game_Start == "Quit" or game_Start == "QUIT":
        print("*dice clack sadly*")
        print("You may be done with Lady Luck is never done with you...")
        break
    else:
        print(f"You played {game_round} rounds!")
        game_Start = input("Oh, one more round! Type 'Roll' to play again or 'Quit' to exit:")





# while game_Start != "roll" or game_Start != "Roll" or game_Start != "ROLL" or game_Start != "quit" or game_Start != "Quit" or game_Start != "QUIT":
#     game_Start = input("Lady Luck can't understand you gibberish. Try Again... [Type 'Roll' to start or 'Quit' to exit.]")
#     if game_Start == "quit" or game_Start == "Quit" or game_Start == "QUIT":
#         break 
#     else:
#         game_Start == "roll" or game_Start == "Roll" or game_Start == "ROLL"