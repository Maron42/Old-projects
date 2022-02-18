#In this program you need make a guess number and computer must be guess it
print("Hello! Make a guess number.")
import random
number = int(input("Your number from one to ten:\n"))
number2 = " "
while number != number2:
    number2 = random.randint(1, 10)
    if number2 == number:
        print("It's your number " , number2 , "?")
        input("Yep?\n")
    elif number > 10:
        print("Liar")
        break
    else:
        print("Hmm.It's dificult!")

        
print("So easy! Try again!")
input("Enter")
