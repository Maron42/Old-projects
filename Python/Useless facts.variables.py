#Useless facts
#Asks the person about his personal facts and write some facts
#It's true facts, but very useless
name = input("Hi,what is your name?\n")
age = input("How are you old?\n")
age = int(age)
weight = int(input("OK. Last question. How much do you weight?\n"))
print("\nHi, this simple test, " , name.lower())
print("Or not, i'm not shure, " , name.upper())
called = name * 5
print("\nAnd your name * 5: ")
print(called)
seconds = age * 365 * 24 * 60 * 60
print("\nYour age in seconds: " , seconds)
moon_weight = weight / 6
print("\nYour weigt on moon: " , moon_weight, "kg")
sun_weight = weight * 27.1
print("\nYour weight on sun: " , sun_weight, "kg")
input("\n\nPress Enter.")
