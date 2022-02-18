#Bones
#Demonstrates the generation of random numbers
import random
#create random numbers
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2
print("when throwing dropped:" , die1, "and" , die2, "points. Their sum:" , total)
input("\nPress Enter, but you already know about it")
