#Hero's inventory
#Demonstrates work with tuples
#Create a tuples with some items and display with a 'for' loop

inventory = ("Sword" ,
             "armor" ,
             "shield" ,
             "healing potion")
print("Your items:")
for item in inventory:
    print(item)
input("\n\nEnter so as continue")

#Get the length of a tuple
print("You have" , len(inventory), "items in your possession.")
input("\n\nEnter so as continue")

#Test for membership with 'in'
if "healing potion" in inventory:
    print("You will live to fight another day.")

#Display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index" , index, "is" , inventory[index])

#Display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print('inventory[' , start, ':' , finish, '] is' , end=" ")
print(inventory[start:finish])
input("\n\nEnter so as continue")

#Concatenate two tuples
chest = ("gold" , "gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
input("\n\nPress Enter so as exit")
