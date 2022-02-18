#The user print all value a car and program adds taxes

Price = int(input("What price your car?\n"))
shipping = 200
shipping = int(shipping)
print("Shipping: " , shipping)
agent_c = 100
agent_c = int(agent_c)
print("Agent: " , agent_c)
input("Press Enter so as go next.")
A = agent_c + shipping + Price
A = int(A)
print("Fix tax with car" , A);
input("Enter to continue")
tax = Price // 100
tax = int(tax)
collection = Price // 10
collection = int(collection)
B = A + tax + collection
B = int(B)
print("All sum with the rest tax" , B)
input("\n\nEnter")
