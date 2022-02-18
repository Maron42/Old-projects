#High scores
#Demonstrates list methods
score = []
choise = None
while choise != "0":
    print(
        """
        High Scores
             0 - Exit
             1 - Show Scores
             2 - Add a Score
             3 - Delete a Score
             4 - Sort Scores
        """
        )
    choise = input("Your choise: ")
    print()
    #exit
    if choise == "0":
        print("Good-bye.")
    # list high-score table
    elif choise == "1":
        print("High scores")
        for score in scores:
            print(score)
    # add a score
    elif choise == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)
    #remove a score
    elif choise == "3":
        score = int(input('Remove which score?: '))
        if score in scoes:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")
    #Sort scories
    elif choise == "4":
        scores.sort(reverse=True)
    # some unknown choice
    else:
         print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
