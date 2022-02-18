#Demonstrates the work of the commands 'break' and 'continue'
count = 0
while True:
    count += 1
    #End cycle, if count takes value as big as ten
    if count > 10:
        break
    #Lose five
    if count == 5:
        continue
    print(count)
input("Enter")
