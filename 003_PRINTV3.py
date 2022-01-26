# \n and \t are for spacing purposes

print("\nInteresting note: any time you print out a variable it is initially \n\tconverted to a string.\n")


print("\nSo if you calculate a variable at all you have to add the variable type.")


print("\tIf you don't do this Python 3 interrupts with a type error \n\tand the program won't run.\n")




#SO EVEN THOUGH THESE FIRST TWO VARIABLES ARE INTS
#PYTHON WILL TRY TO PRINT THEM AS STRINGS
# UNLESS YOU SAY OTHERWISE
bikes = 3
bikes_2 = 7

garage_1 = "Dave's shop"
garage_2 = "Tom's shop"


print(f"\n\nThere are {bikes} bikes in {garage_1}.\n")
print(f"\nThere are {bikes_2} bikes in {garage_2}.\n")

# IMPORTANT PART:CHANGE DATA TYPE
xbikes = int(bikes) + int(bikes_2)
print("\nThere are", xbikes, "bikes in the neighborhood.\n")

print("""
	done by the following:
	
	bikes = 3
	bikes_2 = 7

	print(f"There are {bikes} bikes in {garage_1}.")
	print(f"There are {bikes_2} bikes in {garage_2}.")

	xbikes = int(bikes) + int(bikes_2)
	print("There are ", xbikes, "bikes in the neighborhood.")

""")
	
