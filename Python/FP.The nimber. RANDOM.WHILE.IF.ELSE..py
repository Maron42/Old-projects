#Guess the number
#The Computer choose a random number from one to one hundred
#The User try to guess this number. The Computer says more or less or user right.
import random
print("Hello, guess the number!")
print("This number from one to one hundred")
print("The fewer attempts, the better")
#Primary value
the_number = random.randint(1, 100)
guess = int(input("Your turn:\n"))
tries = 1
#The Cycle
while guess != the_number:
    if guess > the_number:
        print("Less...")
    else:
        print("More...")
    guess = int(input("Your tyrn:\n"))
    tries += 1
print("You right! Congratulations! The number = " , the_number)
print("You spent " , tries, " effort.\n")
input("Enter")
