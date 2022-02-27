import random

counter = 0


print("\nWelcome to the hardcore guessing game.\n")
print("The computer will generate an integer number from one to ten.")
print("You have five guess attempts to guess the number.\n")
print("If you fail to guess the number in five attempts, the game ends.\n")


for i in range (0,5):
    computer_num = random.randint(0,9)
    guess = input("Please enter a number:\n")
    
    if int(computer_num) == int(guess):
        print("That's Correct! YOU WIN!")
        quit()
    else:
        counter +=1
        if counter == 5:
            print("\nGame Over. You took too many tries. Better luck next time.\n")
            quit()
        else:
            print("Please try again.\n")
            continue
            
        
   
   
   
   
   
   
   
   
   
   
    

