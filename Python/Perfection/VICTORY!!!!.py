#Guess the number
#The Computer choose a random number from one to one hundred
#The User try to guess this number. The Computer says more or less or user right.
#BUT IF THE USER USE MORE THAN THREE TRIES, THEN HE LOSE!!!!
import random
print("Hello, guess the number!")
print("This number from one to one hundred")
print("The fewer attempts, the better")
print("You have only three try! Be attention")
#Primary value
the_number = random.randint(1, 50)
guess = int(input("Your turn:\n"))
tries = 1
#The Cycle
while guess != the_number:
    if guess > the_number:
        print("Less...")
    else:
        print("More...")
    tries += 1
    if tries == 4:
        break
    guess = int(input("Your tyrn:\n"))
    
    
tries = int(tries)
if tries <= 3:
    print("You right! Congratulations! The number = " , the_number)
    print("You spent " , tries, " effort.\n")
else:
    print("You lose, I'm so sorry(")
input("Enter")
