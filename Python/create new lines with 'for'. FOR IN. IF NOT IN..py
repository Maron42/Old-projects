#Only consonants
#Demonstrates how create new lines from the original with help cucle 'for'
message = input("Enter text: ")
new_message = ""
vowels = "aeiouy"
print()
for letter in message:
    if letter.lower() not in vowels:
    new_message += letter
    print("Created a new line: " , new_message)
print("\nThis is your text without vowels letter: " , new_message)
input("\n\nEnter, please.")
