#Text analyzer
#Demonstrates work function 'len()' and operator 'in'
message = input("Enter the text:\n")
print("\nThe lenght of your text is: " , len(message))
print("\nThe most frequent english letter, 'e' ,")
if "e" in message:
    print("Occus")
else:
    print("Doesn't occus")
input("\n\nEnter")
