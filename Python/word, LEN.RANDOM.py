#Random letters
#Demonstrates lines indexation
import random
word = "index"
print("In variable 'word' kept letter: " , word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[" , position, "]\t" , word[position])
input("Press Enter so as to quit")
