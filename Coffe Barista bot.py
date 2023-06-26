# First code i ever made. (Networckchuck python tutorial)

print("Hello! Welcome to Starbocks Coffee shop!")

name = input("What is your name?\n")

print("Hello " + name + ", thank you for coming in today.")

menu = "\nBlack Coffee\nEspresso\nLatte\nCappuchino\nFrappuchino"

print("Here is the menu " + menu)

order = input("What would you like to order?\n")

if order == "Frappuchino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Latte":
    price = 6
elif order == "Cappuchino":
    price = 9
elif order == "Espresso":
    price = 7

amount = input("How many would you like? ")

total = price * int(amount)

print("Sounds good " + name + ". Your " + amount + " " + order + " will be ready for you in a moment")

print("Thank you. Your total is: " + str(total) + " $")