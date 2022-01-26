# BASIC PRINT STATEMENTS
print("\nThis is a script about strings.\n")

text_1 = "strings, strings, "
text_2 = "such wonderful things."
print(f"{text_1}\n\t{text_2}\n")


# STRINGS, FUNCTIONS,M AND VARIABLE STORAGE
def print_this():    
    text_a = "But what about\n "
    text_b = "\ttrying something\n "
    text_c = "\t\tcompletely different?" 
    print(f"{text_a + text_b + text_c}\n") 
print_this()

# MORE STRING COUNTING
count_holder_1 = str(len(text_1))
print("\nThe first string is: \n")
print("\t" + text_1)
print("\nThe second string is: \n")
print("\t" + text_2)


# BASIC STRING SPLITTING AND ARRAYS IN PYTHON 3
print("\n\nThe length of the first string is:")
print((len(text_1)))


count_holder_2 = str(len(text_2))
print(f"\nThe length of the second string is {count_holder_2}.\n")


# STRINGS FROM FUNCTIONS
def print_that():
    print("\nNow for trying to do the same thing a different way.\n")
    print("\nThis time it will be called from within a function.\n")
    print("\nThe third string is: \n")
    
    text_3 = "\tTHIS_IS_A_LOT_OF_LETTERS!"
    
    print(text_3)
    count_holder_3 = str(len(text_3))
    print(f"\n\nThe count of the third string is {count_holder_3}.\n")
    
print_that()


# multiple printouts
def print_twice():
    print("This creates a duplicate printing")
    print("This creates a duplicate printing")
    print("\nEND FUNCTION.\n")
   
print_twice()
 
def cloneman():
    text_1 = "\n\tThis also creates a duplicate printing" * 3
    print(text_1)
   
cloneman()
cloneman()
cloneman()
    
print("\n\nSo, how did that turn out?\n")
    
print("\nThis is a basic message printed out.\n")

# second line
text_alpha = "Hello World"
print(f"\tI just have to say {text_alpha} just once.\n")


# MORE FUNCTIONS, VARIABLES, AND PRINT STYLES
text_beta = "Fred's message"
print("\t" + text_beta + " will be delivered tomorrow at noon" + ".\n")

# triple quotes

print('''
	"and it all crashes down,
		and you break your crown,
			and you point your finger but there's no one around."
''')

#printing string length
print("\nfirst string, string length: ", len(text_alpha))

print("\nOUTPUT (from hello world variable): " + (text_alpha[4]))


# SPLITTING AND REARRANGEMENT

name_box = "JIMMORRISON"

print("\n\nJim Morrison's spiritual name is:\n")

print("\t" + name_box[2] + name_box[5] + " " + name_box[3] +name_box[4] +name_box[0] +name_box[9] + " " + name_box[6] + name_box[1] + name_box[8] + name_box[7] + name_box[10] + "\n")
 
leaving = "GOODBYE."
 
print(leaving +"\n")
   
