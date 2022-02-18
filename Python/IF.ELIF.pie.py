#Random numbers selection simulator
print("You take one pie")
print("Inside it...")
import random
pie = random.randint(1, 4)
if pie == 1:
    print("Poison")
elif pie == 2:
    print("Remedy")
elif pie == 3:
    print("Hell")
else:
    print("Paradise")
input("\n\nEnter")
