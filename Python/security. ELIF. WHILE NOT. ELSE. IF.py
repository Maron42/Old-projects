#Exclusive net
#Demonstrates conditions and logical operators
print("\t\tExclusive net")
print("Only for registered users!!\n")
security = 0
username = ""
while not username:
    username = input("Login: ")
password = ""
while not password:
    password = input("Password: ")
if username == "Greg" and password == "Greg":
    print("Hi, Greg!")
    security = 3
elif username == "Dan" and password == "Padaleki":
    print("Hi, creater")
    security = 5
elif username == "Guest" or password == "Guest":
    print("Hello, no name")
    security = 1
else:
    print("Sorry, get out.\n")
input("\n\nPress Enter so as quit")
