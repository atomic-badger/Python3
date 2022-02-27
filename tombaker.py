import random

# uses a counter to randomly activate an option in an if/elif/else loop

counter = random.randint(0,7)

if counter == 0:
    print("\nTom Baker quote of the Day:")
    print("You may be a doctor. But I am the Doctor. The definite article, you might say!\n")

elif counter == 1:
    print("\nTom Baker quote of the Day:") 
    print("\nWould you like a jellybaby?\n")     

elif counter == 2:
    print("\nTom Baker quote of the Day:\n") 
    print("I can feel my hair curling, and that can mean either that it's going to rain, or that I'm on to something!\n")

elif counter == 3:
    print("\nTom Baker quote of the Day:\n") 
    print("\nThe very powerful and the very stupid have one thing in common - they don't change their views to fit the facts.\n")
    print("They change the facts to fit their views, which can be uncomfortable if you happen to be one of the facts\n")
    print("that needs changing.\n")

elif counter == 4:
    print("\nTom Baker quote of the Day:\n") 
    print("You see, if someone who knew the future pointed out a child to you and told you that that child would grow up")
    print("totally evil, to be a ruthless dictator who would destroy millions of lives,\n")
    print("could you then kill that child?\n")
    
elif counter == 5:
    print("\nTom Baker Quote of the Day:\n")
    print("Well Horologist, actually. And chronomotrist. I just love clocks.\n")
    
elif counter == 6:
    print("\nTom Baker Quote of the Day:\n")
    print("\nI don't know yet. That's the trouble with ideas - they only come a bit at a time.\n")
    
else:
    print("\nTom Baker Quote of the Day:\n")
    print("You don't understand the implications... I'm not a human being; I walk in eternity...\n") 
