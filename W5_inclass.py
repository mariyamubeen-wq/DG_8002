name = input("Enter Your Name:")

print(f"Hello {name}")
color = input("What is your favorite color?")


num1 = input("Enter 1st Number:")
num2 = input("Enter 2st Number:")
print(num1+num2)

print("All numbers are stored as string hahahahaha")
print("Let's do it agian>>>")
num1 = float(input("Enter 1st Number:"))
num2 = float(input("Enter 2st Number:"))
print(num1+num2)


# int = integer (whole numbers)
# float = numbers with decimals
# + Addition
# - Subtraction
# * Multiplication
# / Division

print("So, you wanna convert miles to Kilometers eh...?")
print("Americans...")

speed_in_miles = float(input("Alright, what is it in Freedom Units?"))
speed_in_km = speed_in_miles * 1.6
print(f"The speed in normal units is: {speed_in_km}")
print("You're Welcome...")

#Conditional:
num = int(input("Enter 1st number:"))
if num > int(50):
    print("YAY!")
else:
    print("Boooooo!")

#If more than one conditon:
num = int(input("Enter 1st number:"))
if num > int(50):
    print("YAY!")
elif num == int(50):
    print("Balanced, as all things should be...")
else:
    print("Boooooo!")

