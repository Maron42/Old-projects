# ?
import random
Z = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "O", "P",
     "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
k = "E"
print(k, "<--now")
input("Enter so as continue")
while k != 0:
    k += random.choice(Z)
    
    print(k)
print(k, "end")
input("Press Enter key to exit")
