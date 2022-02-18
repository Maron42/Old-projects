#In this program you need make a guess number and computer must be guess it
print("Hello! Make a guess number.")
import random
number = input("Your number from one to one hundred:\n")
Q = ""
B = ""
while Q != 1 or 2:
    number2 = random.randint(1, 100)
    if number > 100:
        print("Liar")
        break
    else:
        Q == input("Your number bigger(1) than " , number2 , "or no(2)?")
while number2 != number:
    if Q == bigger:
      number2 == random.randint(1, number)
      Q == input("Your number bigger(1) than " , number2 , "or no(2)?")
    elif number2 == random.randint(1, number):
        B == input("Your number bigger(1) than " , number2 , "or no(2)?")
    else:
        print("Wow.So easy!")
        break






input("Enter")
