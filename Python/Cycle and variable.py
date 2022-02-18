#The lost battle
#Cycle and more variable
print("Your hero in trap." \
      + "Big trolls attacked him.\n" \
      + "There are a lot of them.\n" \
      + "Alone hero pulls out his sword, preparing for last battle in his life...\n\n")
health = 100
trolls = 1000
damage = 4
while health > 0:
    trolls -= 2
    health -= damage
    print("Hero chopped with trolls, killing two " \
          + ",but he receives some damage on" , damage , "points")
    print("Health: " , health, "\n")
KILL = 1000 - trolls
print("Hero died, but he managed kill" , KILL , "trolls")

input("\n\nPress 'Enter', so as honor the memory")
