count = int(input("How many times do you want to run the loop?"))

while count > 0:
    print("are we there yet?")
    count = count - 1



# Exercise 1: Print star symbol 40 times.
count = int(40)

while count > 0:
    print("*")
    count = count - 1


# Exercise 2: Change the pattern.
count = int(10)

while count > 0:
    print("****")
    count = count - 1

# Example:
count=6
while count>0:
    print("Are we there yet?")
    count=count-1
    if count == 3:
        print("Halfway through!")

# Exercise 3: 
count = int(10)
while count > 0:
    print("****")
    count = count - 1
    if count == 5:
        print("$$$HUZAAAH$$$")

# Exercise 4: Make a Staircase!

count = 0
while count < 10:
    print("****" + ("*"*count))
    count = count + 1
    if count == 5:
        print("$$$HUZAAAH$$$")


# Loop with exit:
carname = input("What is the Car's Brand?")

while carname != "quit":
    print(carname)
    carname = input("What is the Car's Brand?")

# Exercise 5 Car Loop:

carname = input("What is the Car's Brand?")

while carname != "quit":
    if carname == "Honda":
        print ("$10K")
    elif carname == "BMW":
        print ("$30K")
    else:
        print ("Dunno that Brand :/")
        
    carname = input("What is the Car's Brand?")

# Break!
correctnum = 4
num = int(input("Guess a number between 1-10, or 0 to quit:"))

while num !=0:
    if num == correctnum:
        print("YAY! You get a Cake!")
        break
    else:
        num = int(input("Womp Womp :C Try again LOL:"))

# Lists are made by naming a variable and then adding values in "[]" square brackets
fruits = ["apple", "banana", "cantalope"]
fruits.append("durian")
fruits.remove("apple")

# Printing elements of a list:

grades =[75, 71, 82, 90, 68, 65, 88, 73, 77, 51]
i=0
while i < len(grades):
    print(grades[i])
    i = i+1

# Exercise 6:
grades =[75, 71, 82, 90, 68, 65, 88, 73, 77, 51]
i=0
while i < len(grades):
    if grades[i] >= 80:
        print (grades[i], "A")
    else:
        print (grades[i], "B")
    i = i+1
# OR

grades =[75, 71, 82, 90, 68, 65, 88, 73, 77, 51]
i=0
while i < len(grades):
    if grades[i] >= 80:
        print ("A")
    else:
        print ("B")
    i = i+1

# Randomness

import random

correctnum = random.randint(1,10)

num = int(input("Guess a number between 1-10, or 0 to quit:"))

while num !=0:
    if num == correctnum:
        print("YAY! You get a Cake!")
        break
    else:
        num = int(input("Womp Womp :C Try again LOL:"))
