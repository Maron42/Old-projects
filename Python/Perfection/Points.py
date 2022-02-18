choice = None
point = 10
Strenght = 0
Health = 0
Agility = 0
Wisdom = 0
Z = 0
while choice != "0" and point != 0:
    print(
 """
Hello! Please create your hero.
 0 - Quit
 1 - Add to strength
 2 - Add to health
 3 - Add to agility
 4 - Add to wisdom
 """
 )
    print("You have" , point, "points")
    choice = input("Choice: ")
    if choice == "0":
        print("Good-bye.")
    elif choice == "1":
        print("You add 1 point to strenght")
        Strenght += 1
    elif choice == "2":
        print("You add 1 point to health")
        Health += 1
    elif choice == "3":
        print("You add 1 point to agility")
        Agility += 1
    elif choice == "4":
        print("You add 1 point to wisdom")
        Wisdom += 1
    point -= 1
while Z != "1":
    if Strenght == 0:
        print("You so weak!")
    elif Health == 0:
        print("You so sick!")
    elif Agility == 0:
        print("You so clumsy!")
    elif Wisdom == 0:
        print("You so stupid!")
    else:
        print("It's ok!")
    Z = input("Please, enter the '1'")
input("Enter")
