#This program throw up coin and calculates how many eagles and tails fell out.
import random
print("Hi! This program calculated eagles and tails. This is very funny!")

how = 0
eagle = 0
tail = 0
while how != 100:
  R = random.randint(1, 2)
  if R == 1:
      eagle += 1
  else:
      tail += 1
  how += 1
print("Eagles = " , eagle)
print("Tails = " , tail)
input("Press 'Enter' so as to go quit")
