# ?
import random
Z = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "O", "P",
     "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
k = "E"
j = 0
print(k, "<--now")
input("Enter so as continue")
while k != 0:
    k += random.choice(Z)
    j += 1
    if j == 1000:
        break
    else:
        print(k)
print(k, "end")
input("Press Enter key to exit")
