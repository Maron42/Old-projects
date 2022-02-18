#Hero's inventory
#Demonstrates tuple creation

#Create an empty tuple
inventory = ()
#Treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")
input("\nPress Enter so as find something")
#Create a tuple with some items
inventory = ("Sword",
             "armor",
             "shield",
             "healing potion")
#Print the tuple
print("\nThe tuple inventory is: ")
print(inventory)
#Print each element in the tuple
print("\nYour items: ")
for item in inventory:
    print(item)
input("\n\nEnter")
