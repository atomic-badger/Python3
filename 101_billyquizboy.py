print("\nWelcome to Billy Quizboy.\n")


# the three variables in the game are play, answer, and points

points = 0	# tracks score by question, each question is worth 20 points

play = input("Do wish to play the game?\n")

if play.lower() == "no":
    print("The game will now close. Have a nice day :) :) :)\n")
    quit()
    
else:
    print("Excellent. Now the game will begin.\n")


# this program primarily works by running if else statements in linear series one time each
# this is question 1 of the quiz

answer = input("(two words) Who is Hank and Dean Venture's Father?\n")

if answer.lower() == "rusty venture":
    print("That is correct. The answer is Rusty Venture.\n")
    points += 20
    print("\nYour current score is " + str(points) + ".")

else:
   print("That answer is incorrect. The answer is Rusty Venture.\n") 
   print("\nYour current score is " + str(points) + ".")
   print("We will now go onto the next question.\n")


# this is question 2 of the quiz

answer = input("\n(one word) What is the all powerful artifact Rusty Venture uses as a paperweight?\n")

if answer.lower() == "orb":
    print("That is correct. The answer is the Orb.\n") 
    points += 20
    print("\nYour current score is " + str(points) + ".")
    print("We will now go onto the next question.\n")

else: 
    print("That answer is incorrect. the answer is Orb.\n") 
    print("\nYour current score is " + str(points) + ".")
    print("We will now go onto the next question.\n")

# this is question 3 of the quiz

answer = input("\n(three words) Who is Rusty Venture's archvillain in The Venture Brothers?\n")

if answer.lower() == "the mighty monarch":
    print("That is correct. The answer is the The Mighty Monarch.\n") 
    points += 20
    print("\nYour current score is " + str(points) + ".")
    print("We will now go onto the next question.\n")

else: 
   print("That answer is incorrect. The answer is the The Mighty Monarch.\n")
   print("\nYour current score is " + str(points) + ".")
   print("We will now go onto the next question.\n")
   
   
# this is question 4 of the quiz

answer = input("\n(two words) Who is the Mighty Monarch's love interest?\n")

if answer.lower() == "doctor girlfriend":
    print("That is correct. The answer is Doctor Girlfriend.\n") 
    points += 20
    print("\nYour current score is " + str(points) + ".")
    print("We will now go onto the next question.\n")

else: 
   print("That answer is incorrect. The answer is Doctor Girlfriend.\n")
   print("\nYour current score is " + str(points) + ".")
   print("We will now go onto the next question.\n")
   
   
# this is question 5 of the quiz

answer = input("\n(two words) Who is Rusty Venture's bodyguard at the beginning of The Venture Brothers?\n")

if answer.lower() == "brock sampson":
    print("That is correct. The answer is Brock Sampson.\n") 
    points += 20
    print("\nYour current score is " + str(points) + ".")
    print("That was the final question of the quiz.")

else: 
   print("That answer is incorrect. The answer is Brock Sampson\n") 
   print("\nYour current score is " + str(points) + ".")
   print("That was the final question of the quiz.\n")
   
print("\nYour final game score is: " + str(points) + ".")
print("The game is now over. Have a fantastic day :) :) :)\n")
   
       
