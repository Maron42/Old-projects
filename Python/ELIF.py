#Mood sensor
#Demonstrates use command 'elif'
import random
print("I know your mood. From my screen are not hidden your feelings")
print("So, your mood...")
mood = random.randint(1, 4)
if mood == 1:
    #We randomly choose a number
    print("Funny")
elif mood == 2:
    print("Medium")
elif mood == 3:
    print("Badly")
else:
    print('Insane')
input("Enter")
