#How dictionary
Man = {("Greg": "Michael"),
       "Lili" : "Megan",
       "Sigurd" : "Ragnar"}
choice = None
while choice != "0":
    print(
 """
 0 - Quit
 1 - Name
 2 - Add a Name
 3 - Redefine a Name
 4 - Delete a Name
 """
 )
    choice = input("Choice: ")
    if choice == "0":
        print("Good-bye.")
    elif choice == "1":
        Name = input("About Name are you asking for me?: ")
        if Name in Man:
            definition = Man[Name]
            print("\n", Name, "means", definition)
        else:
            print("\nSorry, I don't know", Name)
    elif choice == "2":
        Name = input("What name do you want me to add?: ")
        if Name not in Man:
            definition = input("\nWhat's the definition?: ")
            Man[Name] = definition
            print("\n", Name, "has been added.")
        else:
            print("\nThat Name already exists! Try redefining it.")
    elif choice == "3":
        Name = input("What Name do you want me to redefine?: ")
        if Name in Man:
         definition = input("What's the new definition?: ")
         Man[Name] = definition
         print("\n", Name, "has been redefined.")
     #else:
         #print("\nThat term doesn't exist! Try adding it.")
    elif choice == "4":
        Name = input("What term do you want me to delete?: ")
        if Name in Man:
         del Man[Name]
         print("\nName" , Name, "deleted.")
     #else:
         #print("\nI can't do that!" , Name, "doesn't exist in the dictionary.")
#Some unknown choise
 #else:
     #print("\nSorry, but", choice, "isn't a valid choice.")
input("Enter")
