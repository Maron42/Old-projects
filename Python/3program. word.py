#This program jumble your text
#RANDOM
word = input("Hi, enter the word: ")
import random
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("The random jumble is:", jumble)
input("\n\nEnter so as continue")
#Not random
number = input("Hi, enter the word again: ")
import random
xyz = ""
while number:
    position = random.randrange(len(word))
    number += xyz[position]
    xyz = xyz[:position] + xyz[(position + 1):]
print("The jumble is:", xyz)
input("\n\nPress Enter so as exit")
